# Docker Registry Service
This repository contains a django web application that can handle docker files and builds and push them to local registry automatically.

## Authentication
Use docker_registry_service as both user and password to django admin to manage docker files.
Remember to add root user to the machine like this to ensure docker commands work:

    sudo useradd -m -s /bin/bash docker_registry_service
    sudo usermod -aG sudo docker_registry_service
    sudo passwd docker_registry_service
    
and setting password to docker_registry_service