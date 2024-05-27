#!/usr/bin/env bash
# Install MySQL 5.7.x on web servers

# Update apt package index
sudo apt-get update

# Install MySQL server
sudo apt-get install -y mysql-server-5.7

# Check MySQL version
mysql --version
