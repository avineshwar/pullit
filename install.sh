#!/usr/bin/env bash

# Some Virtual ENV constants
VENV_LOCATION="$HOME/venv/pullit"
PYTHON_LOCATION="$(which python)"


########################
# Create a virutal env #
########################
function create_env() {
    if [[ -f "$VENV_LOCATION/bin/activate" ]]; then
        echo "Activating $VENV_LOCATION/bin/activate"
        source $VENV_LOCATION/bin/activate
    else
        echo "Creating $VENV_LOCATION environment"
        virtualenv "$VENV_LOCATION"
        source $VENV_LOCATION/bin/activate
    fi
}

########################
# Exit a virutal env   #
########################
function exit_env() {
    if [[ ! $PYTHON_LOCATION == *'pullit'* ]] && [[ ! $PYTHON_LOCATION == *'usr'* ]]; then
        echo "Cleaning up your environment..."
        deactivate > /dev/null
    fi
}

########################
# Install requirements #
########################
function install() {
    echo "Installing requirements..."
    pip install -r requirements.txt
}

########################
# Run installation     #
########################
function main() {
    exit_env; create_env; install
    echo "You're good to go. Run pullit (./pullit.py)"
}

main