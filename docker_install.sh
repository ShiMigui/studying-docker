#!/bin/bash

sudo pacman --noconfirm -S docker

sudo systemctl enable docker.service
sudo systemctl start docker.service
sudo systemctl enable docker.socket
sudo systemctl start docker.socket