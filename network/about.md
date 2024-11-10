# About
**Note:** I am using Arch Linux. If you're not using a Linux distribution, don't use `sudo`.

This project requires a network. You can create one with the following command:

```bash
sudo docker network create flask_net
```

## Build
To create the images, navigate to the `./studying-docker/network` directory and run:

```bash
sudo docker buildx build -t network/mysql mysql/.
sudo docker buildx build -t network/flask flask/.
```

After building the images, you can run the containers with the following commands:

```bash
sudo docker run -d -p 3306:3306 --name mysql_flask --rm --network flask_net -e MYSQL_ALLOW_EMPTY_PASSWORD=True network/mysql
sudo docker run -d -p 5000:5000 --name flask --rm --network flask_net network/flask
```