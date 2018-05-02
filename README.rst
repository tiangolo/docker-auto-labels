==================
Docker Auto Labels
==================


.. image:: https://img.shields.io/pypi/v/docker-auto-labels.svg
        :target: https://pypi.python.org/pypi/docker-auto-labels

.. image:: https://img.shields.io/travis/tiangolo/docker-auto-labels.svg
        :target: https://travis-ci.org/tiangolo/docker-auto-labels




Automatically generate Docker Swarm mode node labels for each constraint label in each service in a Docker Compose / Docker Stack file.


* Free software: MIT license


Description
-----------

This command line package is made to be used with a Docker Swarm mode cluster.

It will:
* Read a Docker Compose / Docker Stack file.
* Extract the node label constraints for each service.
* Check that all the labels exist in the Docker Swarm mode cluster.
* For each label that doesn't exist, create it in a random node in the cluster.

Adding label constraints helps you ensure that all the "stateful"
Docker services (like databases) are always deployed to the same
node (specially useful in a multi-node cluster).

This program will ensure that those labels exist in one node
in the cluster, if they don't exist, they are created in one
node chosen randomly.

That way, the first time you deploy a stack, a random node will be assigned
to each stateful service (by this command, right before the deployment).

And for all subsequent deployments, the stateful services will go to the
same nodes that they were using.

For examples on how to use it, check: https://github.com/tiangolo/full-stack

Credits
-------

This package was created with Cookiecutter_ and the `elgertam/cookiecutter-pipenv`_ project template, based on `audreyr/cookiecutter-pypackage`_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`elgertam/cookiecutter-pipenv`: https://github.com/elgertam/cookiecutter-pipenv
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
