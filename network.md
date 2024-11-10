# Network
To see the project, [click here](./network/).

## Description
To enable communication between our application and an API, plugins, or containers, we need to set up a network. Two primary network types commonly used are: **Host** and **Bridge**.

### Host vs. Bridge Networks
#### Host
The host network operates as if it is running directly on the host machine, sharing the same network stack. This means it uses the host's ports directly, so careful ports management is essential—each port can only be used by one service by time.
#### Bridge
The bridge network operates in a "sandbox" (an isolated and virtual environment). Ports exposed in the container, such as 3000, correspond to a unique port 3000 within this virtual environment. If you launch multiple instances of a project, each instance will have it's own port 3000 exposed, without conflicts.

### Network commands
**Note**: All commands begins with `docker network` (with `sudo` on arch linux).
- `list`: Lists all networks in Docker.
- `create`: Creates a network using `create <network_name>`. Optionally, add `-d <network_type>` to specify Host or Bridge.
- `rm`: Removes a network using `rm <network_name_or_id>`.
- `prune`: Clears unused networks using `prune`.
- `connect`: Connects a container to a network using `connect <network_name> <container_id>`.