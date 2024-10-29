# !/bin/bash
set -e

## Create necessary folders and files
echo "Creating Necessary directories"
sudo mkdir -p /opt/log-repository/{config,certs,packages}
sudo chown -R "$USER":"$USER" /opt/log-repository

## Check if python is installed and install if not
echo "Check and install python3"
if ! command -v python3 &> /dev/null
then
    sudo apt-get update
    sudo apt-get install python3 -y
fi

## Install UV as a global dependency
python3 -m pip install uv 

## Create a virtual environment
uv venv

