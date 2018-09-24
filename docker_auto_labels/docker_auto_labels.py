# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import random

import docker
import yaml

# Typings
from docker.models.nodes import Node  # noqa


def get_content(file_name):
    abs_file_name = os.path.abspath(file_name)
    with open(abs_file_name) as docker_file:
        return yaml.load(docker_file)


def get_existing_labels(nodes):
    existing_labels = set()
    for node in nodes:
        node_labels = node.attrs['Spec']['Labels']
        hostname = node.attrs['Description']['Hostname']
        node_id = node.id
        for label, value in node_labels.items():
            existing_labels.add((label, value, hostname, node_id))
    return existing_labels


def get_stack_constraint_labels(content):
    deploy = 'deploy'
    placement = 'placement'
    constraints = 'constraints'
    stack_labels = []
    content['services']
    for _, val in content['services'].items():
        if deploy in val:
            if placement in val[deploy]:
                if constraints in val[deploy][placement]:
                    for cons in val[deploy][placement][constraints]:
                        if cons.startswith('node.labels') and '==' in cons:
                            cons_list = cons.split('==')
                            label = cons_list[0].replace('node.labels.',
                                                         '').strip()
                            value = cons_list[1].strip()
                            stack_labels.append((label, value))
    return set(stack_labels)


def ensure_existing_labels(existing_labels, stack_labels, nodes):
    for label, value in stack_labels:
        this_label_exists = False
        for existing_label, existing_value, existing_host, node_id in existing_labels:
            if label == existing_label:
                this_label_exists = True
                print(
                    '--- \n=== \nExisting label: {existing_label} \nWith existing value: {existing_value} \nIn host: {existing_host} \nWith node ID: {node_id} \nMatches required label: {label} \nDeclared with value: {value} \n--- \n'
                    .format(
                        existing_label=existing_label,
                        existing_value=existing_value,
                        existing_host=existing_host,
                        node_id=node_id,
                        label=label,
                        value=value))
        if this_label_exists:
            continue
        else:
            node = random.choice(nodes)
            node_spec = node.attrs['Spec']
            node_spec['Labels'][label] = value
            node.update(node_spec)
            node.reload()
            hostname = node.attrs['Description']['Hostname']
            node_id = node.id
            print(
                '--- \n+++ \nLabel: {label} \nWith value: {value} \nAssigned to node in hostname: {hostname} \nWith node ID: {node_id} \n--- \n'
                .format(label=label, value=value, hostname=hostname, node_id=node_id))


def process(file_name):
    # file_name
    content = get_content(file_name)
    client = docker.from_env()
    nodes = client.nodes.list()  # type: List[Node]
    existing_labels = get_existing_labels(nodes)
    stack_labels = get_stack_constraint_labels(content)
    ensure_existing_labels(existing_labels, stack_labels, nodes)
