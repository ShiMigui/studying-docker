# Volumes
To see the project, [click here](./volumes)!

To ensure persistent storage for directories or files in a Docker container, we can create a **volume**. Without a volume, any data generated within a container, such as new files in the `messages` directory, will be lost if the container is removed. Using a volume prevents this, allowing us to save data across container restarts or removals. Here’s an example command:

```bash
sudo docker run -d --rm -p 80:80 --name msgs -v v_msgs:/var/www/html/messages shimigui/duckmsgs:v0.1
```

### Command Breakdown

- `sudo`: Elevates permissions for commands that require root access.
- `docker run`: Initiates a new container.
- `-d`: Runs the container in detached mode, allowing it to run in the background.
- `-p 80:80`: Maps port 80 on the host to port 80 on the container, enabling access to services within the container via `localhost:80`.
- `--name msgs`: Assigns a custom name (`msgs`) to the container for easy identification.
- `-v v_msgs:/var/www/html/messages`: Creates a Docker volume named `v_msgs` and mounts it to the `messages` directory within the container. This means any files written to `messages` inside the container will persist in `v_msgs` on the host, even if the container is removed.
- `shimigui/duckmsgs:v0.1`: Specifies the image and version (`v0.1`) used to create the container.