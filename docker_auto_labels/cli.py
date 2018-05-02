# -*- coding: utf-8 -*-

"""Console script for docker_auto_labels."""
import sys
import click

from . import docker_auto_labels


@click.command()
@click.argument('docker-file-path')
def main(docker_file_path):
    """Read a Docker Compose / Docker Stack file.
    Extract the node label constraints for each service.
    Check that all the labels exist in the Docker Swarm mode cluster.
    For each label that doesn't exist, create it in a random
    node in the cluster.

    Adding label constraints helps you ensure that all the "stateful"
    Docker services (like databases) are always deployed to the same
    node (specially useful in a multi-node cluster).
    This program will ensure that those labels exist in one node
    in the cluster, if they don't exist, they are created in one
    node chosen randomly."""
    docker_auto_labels.process(docker_file_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
