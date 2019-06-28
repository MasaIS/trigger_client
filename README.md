# Trigger message test tool

## Overview
Test tool with FTP. 

## Setup
- Pre-install
```sh
sudo yum install -y gcc wget git
sudo yum install -y zlib-devel libffi-devel bzip2-devel \
openssl-devel ncurses-devel sqlite-devel readline-devel \
tk-devel gdbm-devel libuuid-devel xz-devel
```
OS: CentOS Linux release 7.6.1810

- Compile and install
```sh
wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
tar zxvf Python-3.7.3.tgz
cd Python-3.7.3
./configure
make
sudo make altinstall
```
Could you check up to date version by [this site](https://www.python.org/downloads/).

- Download script
```sh
git clone https://github.com/MasaIS/trigger_client.git
```

## Usage
- Basic
```sh
python trigger.py -a <IP address(FTP server)> -u <Login username> -p <Login password>
```

- Custom
```sh
python trigger.py -a <IP address(FTP server)> -u <Login username> -p <Login password> \
 -d <Change directory> -f <Transfer filename> \
 -M <Maximum number minutes> -S <Maximum number seconds> -I <Maximum number modules>
```

## Author
[masaIS](https://github.com/MasaIS)
