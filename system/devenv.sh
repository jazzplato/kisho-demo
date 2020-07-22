#!/bin/bash
NAME="kisho-cinema-dev"
DIR_VOL="/code"
DIR_BASE="$(dirname $(realpath $0))"
PATH_DOCKERFILE="$DIR_BASE/devenv/Dockerfile"
CMD="bash"
HELP="Usage: ./devenv ACTION
Actions:
  create  Create a docker dev env in Ubuntu 18.04
  enter   Enter the docker
  purge   Stop and destroy the docker"

function print_help {
    echo "$HELP"
}

function print_error {
    echo "Error: Invalid option '$1'"
    print_help
}

function create_env {
    if [ -z $(docker images -q $NAME) ]; then
        docker build -t $NAME -f $PATH_DOCKERFILE .
    fi
    docker create \
        -it \
        --name $NAME \
        --security-opt seccomp=unconfined \
        -h $NAME \
        -v $DIR_BASE:$DIR_VOL \
        -p 8000:8000 \
        -p 3306:3306 \
        $NAME $CMD && echo "create done" && \
    docker start $NAME && echo "start done"
}

function enter_env {
    docker exec -it $NAME bash
}

function purge_env {
    docker stop $NAME
    docker rm $NAME
}

if [ $# -lt 1 ]; then
    print_help
    exit 1
fi

case "$1" in
    "create") create_env ;;
    "enter") enter_env ;;
    "purge") purge_env ;;
    "help") print_help ;;
    *) print_error $1; exit 1;
esac