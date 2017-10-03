#!/bin/bash
apt-get update
apt-get install -y python3-pip
pip3 install -U pytest
cd lxdock
py.test
