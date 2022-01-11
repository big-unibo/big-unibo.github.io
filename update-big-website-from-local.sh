#!/bin/bash
sudo find /var/www/html/big/* -maxdepth 0 ! \( -name 'downloads' -o -name 'old' -o -name 'projects' \) -type d -exec rm -rf {} +
sudo mv -f /home/egallinucci/_site/* /var/www/html/big
