#!/bin/bash
DIR_CURR="$(realpath $(dirname $0))"
DIR_VIRTUALENV="env"
cd $DIR_CURR

# create a virtualenv if not exists
if [ ! -d $DIR_VIRTUALENV ]; then
    virtualenv $DIR_VIRTUALENV
fi

# enter the virtualenv
source $DIR_VIRTUALENV/bin/activate

# install python dependencies for deployment
pip install -r requirements.txt

# install ansible galaxy roles
ansible-galaxy install -r requirements.yml

# exit the virtualenv
deactivate