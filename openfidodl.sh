#!/bin/bash
#
# Standard Script call to install and setup node
# and to download all files in provided urls
#

curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
apt-get -q -y install nodejs > /dev/null


node urldownload.js $OPENFIDO_INPUT || error

cd $OPENFIDO_INPUT

wget --input-file=curls.txt

cd /tmp/gitrepo