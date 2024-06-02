#!/usr/bin/env bash
# This script installs MySQL 5.7 on both web-01 and web-02 servers.

# Define the servers
servers=("100.26.50.5" "52.3.243.190")

# Function to install MySQL 5.7
install_mysql() {
    ssh ubuntu@"$1" << 'EOF'
        sudo apt-get update
        sudo apt-get install -y wget lsb-release gnupg
        wget https://dev.mysql.com/get/mysql-apt-config_0.8.10-1_all.deb
        sudo dpkg -i mysql-apt-config_0.8.10-1_all.deb
        sudo apt-get update
        sudo apt-get install -y mysql-server
        rm mysql-apt-config_0.8.10-1_all.deb
EOF
}

# Install MySQL on each server
for server in "${servers[@]}"; do
    install_mysql "$server"
done
