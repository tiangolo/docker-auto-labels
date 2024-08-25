## DEPRECATED 🚨

This project is deprecated. I haven't used it in years, I don't recommend using it.

# Docker Auto Labels

Automatically generate Docker Swarm mode node labels for each constraint label in each service in a Docker Compose / Docker Stack file.

## Description

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

## Release Notes

### Latest Changes

#### Internal

* 🔧 Update PDM config. PR [#12](https://github.com/tiangolo/docker-auto-labels/pull/12) by [@tiangolo](https://github.com/tiangolo).

### 0.2.4

#### Refactors

* 👷 Refactor build setup and CI, and deprecate package. PR [#11](https://github.com/tiangolo/docker-auto-labels/pull/11) by [@tiangolo](https://github.com/tiangolo).

#### Internal

* 🔧 Add GitHub templates for discussions and issues, and security policy. PR [#9](https://github.com/tiangolo/docker-auto-labels/pull/9) by [@alejsdev](https://github.com/alejsdev).
* 🔧 Add funding. PR [#8](https://github.com/tiangolo/docker-auto-labels/pull/8) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add latest-changes GitHub Action. PR [#6](https://github.com/tiangolo/docker-auto-labels/pull/6) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add dependabot. PR [#7](https://github.com/tiangolo/docker-auto-labels/pull/7) by [@tiangolo](https://github.com/tiangolo).

### 0.2.3

## License

MIT License
