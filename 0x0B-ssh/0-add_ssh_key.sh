#!/usr/bin/env bash
# Add SSH public key to allow access for ubuntu user

# SSH public key
SSH_PUBLIC_KEY="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN"

# SSH directory
SSH_DIR="/home/ubuntu/.ssh"

# Create .ssh directory if not exists
mkdir -p "$SSH_DIR"

# Add public key to authorized_keys file
echo "$SSH_PUBLIC_KEY" >> "$SSH_DIR/authorized_keys"

# Set correct permissions
chmod 700 "$SSH_DIR"
chmod 600 "$SSH_DIR/authorized_keys"
chown -R ubuntu:ubuntu "$SSH_DIR"

# Output success message
echo "SSH public key added successfully for ubuntu user."
