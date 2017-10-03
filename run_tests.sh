#!/bin/bash
apt-get update
apt-get install -y python3-pytest
cd lxdock
py.test
