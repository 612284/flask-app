#!/bin/sh
echo "public ip: "  >> /usr/src/app/templates/index.html
curl https://checkip.amazonaws.com >> /usr/src/app/templates/index.html
echo "<br>" >> /usr/src/app/templates/index.html
echo "private ip: "  >> /usr/src/app/templates/index.html
curl curl http://169.254.169.254/latest/meta-data/local-ipv4  >> /usr/src/app/templates/index.html
echo "<br>" >> /usr/src/app/templates/index.html
echo "random string: "  >> /usr/src/app/templates/index.html
head -c 500 /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 30 | head -n 1 >> /usr/src/app/templates/index.html
echo "<br>" >> /usr/src/app/templates/index.html
python /usr/src/app/app.py
