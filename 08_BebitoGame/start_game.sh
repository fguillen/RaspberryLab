#!/bin/bash

# Navigate to the project directory
cd /home/td/Development/RaspberryLab/08_BebitoGame/

# Pull the latest code
git checkout main
git pull origin main

# Activate the virtual environment
source /home/td/Development/RaspberryLab/.venv/bin/activate

# Run the Python script
/home/td/Development/RaspberryLab/.venv/bin/python3 game.py
