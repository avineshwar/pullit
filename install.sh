#!/usr/bin/env bash

########################
# Create a virutal env #
########################
function create_env() {
    LOCATION="~/venv/pullit"
    if [[ -d "$LOCATION" ]]; then
        echo "Activating $LOCATION/bin/activate"
        $(source $LOCATION/bin/activate)
    else
        echo "Creating $LOCATION environment"
        $(virtualenv $LOCATION)
    fi
}

########################
# Exit a virutal env   #
########################
function exit_env() {
    EXISTS="$(which deactivate)"
    if [[ -e $EXISTS ]]; then
        $(deactivate) > /dev/null
    fi
}

########################
# Install requirements #
########################
function install() {
    $(pip install requirements)
}

########################
# Run installation     #
########################
function main() {

    echo "Cleaning up your environment..."
    exit_env

    echo "Creating a virtual environment..."
    create_env

    echo "Installing requirements..."
    install

    echo "You're good to go. Run pullit (./pullit.py)"
}

main