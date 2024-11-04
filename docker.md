# Docker

## Lifecycle
In Docker, you can perform various operations to manage containers on your PC.

### Fetch & Run Containers
To pull and run a container, use `docker run <name>`. If the image is not already on your PC, this command will fetch it from Docker Hub and then [start the container](#start-container). Each time you run this command, it creates a new container from the specified image, unlike [docker start](#start-container), which only restarts an existing, stopped container.

| Attribute | Description                                                                       |
| --------- | --------------------------------------------------------------------------------- |
| `-d`      | Runs the container in the background (detached mode).                             |
| `-p`      | Maps a port on the host to a port in the container (e.g., `-p 80:80`).            |
| `--name`  | Assigns a specific name to the container (otherwise, a random name is generated). |
| `--rm`    | Automatically removes the container when it stops.                                |

### List Containers
To list all containers (running and stopped), use `docker ps -a`. To show only running containers, use `docker ps`.

### Start Containers
To start an existing container, use `docker start <id>`. You can also use flags like `docker start -it <id>`, which starts the container in interactive mode.

### Stop Containers
To stop a running container, use `docker stop <id_or_name>`.

### Remove Containers
To remove a container, use `docker rm <id>`. If the container is still running, you can force its removal with `docker rm -f <id>`.

## Building Images
To build a Docker image, use `docker build <directory>` or the more recent `docker buildx build <directory>`. This creates an image that can later be run with the [Docker Run Command](#fetch--run-containers).

## Examples
### `sudo docker run -d -p 80:80 --name nginx_app nginx`
- `docker run`: This command starts a container. If the image is already on your PC, it will use that; otherwise, it will pull the image from Docker Hub.
- `-d`: Runs the container in the background.
- `-p 80:80`: Maps port **80** on the host to port **80** in the container.
- `--name nginx_app`: Assigns a name to the container, making it easier to identify and manage.
- `nginx`: Specifies the image to use, which could be any available image on Docker Hub.