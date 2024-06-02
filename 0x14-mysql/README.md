# MySQL Installation

This project contains a script to install MySQL 5.7 on two servers (web-01 and web-02).

## Files

- `0-install_mysql.sh`: A Bash script to install MySQL 5.7 on both servers.

## Usage

To use the script, make sure it's executable and run it:

```bash
chmod +x 0-install_mysql.sh
./0-install_mysql.sh
The script will log into each server and install MySQL 5.7.

Requirements
The script must be executable.
The script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any errors.
python
Copy code

### Push Changes to GitHub

Make sure your directory structure is correct:
