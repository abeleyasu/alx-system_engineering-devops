s script installs MySQL 5.7.x on an Ubuntu 16.04 server

# Update the package index
sudo apt-get update

# Install MySQL 5.7
sudo apt-get install -y mysql-server-5.7

# Check MySQL version
mysql --version
