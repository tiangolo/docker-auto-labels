#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `docker_auto_labels` package."""
from click.testing import CliRunner
import docker
from docker_auto_labels import cli

service1_label = 'stack-example-com.app-service1-data'
service2_label = 'stack-example-com.app-service2-data'

docker_stack_filename = 'test-docker-stack.yml'

client = docker.from_env()
nodes = client.nodes.list()
node = nodes[0]


def clean_labels():
    for label in [service1_label, service2_label]:
        node_spec = node.attrs['Spec']
        if label in node_spec['Labels']:
            del node_spec['Labels'][label]
            node.update(node_spec)
            node.reload()


def test_clean_labels():
    node.reload()
    node_spec = node.attrs['Spec']
    node_spec['Labels'][service1_label] = 'test'
    node.update(node_spec)
    node.reload()
    node_spec = node.attrs['Spec']
    assert service1_label in node_spec['Labels']
    clean_labels()
    node.reload()
    assert service1_label not in node_spec['Labels']


def test_help():
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_simple_run():
    clean_labels()
    runner = CliRunner()
    result = runner.invoke(cli.main, args=[docker_stack_filename])
    assert result.exit_code == 0
    node.reload()
    node_spec = node.attrs['Spec']
    assert service1_label in node_spec['Labels']
    assert node_spec['Labels'][service1_label] == 'true'
    assert service2_label in node_spec['Labels']
    assert node_spec['Labels'][service2_label] == '1'
