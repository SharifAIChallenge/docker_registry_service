#!/bin/sh
mkdir working_directory
mkdir working_directory/$1
mv $2 working_directory/$1/dockerfile
cd working_directory/$1
exec > docker_registry_service.log 2>&1
docker build  -t=$1 .