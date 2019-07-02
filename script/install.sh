#!/bin/bash

apt-get install python3 -y
apt-get intall pip3 -y

pip3 install -r module.txt

python3 csvToDb.py