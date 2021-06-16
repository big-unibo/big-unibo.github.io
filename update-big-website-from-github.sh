#!/bin/bash
wget https://github.com/big-unibo/big-website/releases/latest/download/big-website.zip
sudo find /var/www/html/big/* -maxdepth 0 ! \( -name 'downloads' -o -name 'old' -o -name 'projects' \) -type d -exec rm -rf {} +
sudo unzip -d /var/www/html/big big-website.zip
rm big-website.zip
