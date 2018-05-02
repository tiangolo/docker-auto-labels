# -*- coding: utf-8 -*-
import os
import random

import docker
import yaml

# types
from docker.models.nodes import Node  # noqa
from typing import List  # noqa


def get_content(file_name):
    abs_file_name = os.path.abspath(file_name)
    with open(abs_file_name) as docker_file:
        return yaml.load(docker_file)


def get_existing_labels(nodes):
    existing_labels = set()
    for node in nodes:
        node_labels = node.attrs['Spec']['Labels']
        for label in node_labels:
            existing_labels.add(label)
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
                        if cons.startswith('node.labels'):
                            cons_list = cons.split('==')
                            label = cons_list[0].replace('node.labels.',
                                                         '').strip()
                            stack_labels.append(label)
    return set(stack_labels)


def ensure_existing_labels(existing_labels, stack_labels, nodes):
    for label in stack_labels:
        if label in existing_labels:
            continue
        else:
            node = random.choice(nodes)
            node_spec = node.attrs['Spec']
            node_spec['Labels'][label] = 'true'
            node.update(node_spec)


def process(file_name):
    # file_name
    content = get_content(file_name)
    client = docker.from_env()
    nodes = client.nodes.list()  # type: List[Node]
    existing_labels = get_existing_labels(nodes)
    stack_labels = get_stack_constraint_labels(content)
    ensure_existing_labels(existing_labels, stack_labels, nodes)
