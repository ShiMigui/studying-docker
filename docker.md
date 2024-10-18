# Docker

## Lifecycle
In Docker, we can do some operations to control containers on our PC.

### Pulling and running an image from docker hub
To pull and run a container, we can use `docker run <name>`. If the container is not yet pulled to our PC, that command will pull the image and run it. 

| Attribute | Description                                                                   |
| --------- | ----------------------------------------------------------------------------- |
| -d        | Tells Docker to run container in background(detached mode).                   |
| -p        | Maps a port on the host to a port in the container(e.g. `-p 80:80`).          |
| --name    | Specifies a name for the container(if not provided, generates a random name). |

### Listing existing containers
To list existing containers, we can use `docker ps -a`, to show only containers that are running, we can use `docker ps`.

### Starting a container
To start an existing container, we can use: `docker start <id>`.

### Stopping a container
To stop an existing container, we can use: `docker stop <id_or_name>`

### Removing a container
To remove a container, we can use `docker rm <id>`. If the container is running, we can force its removal with `docker rm -f <id>`.

