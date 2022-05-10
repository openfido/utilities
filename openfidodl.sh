#!/bin/bash
#
# Standard Script call to install and setup node
# and to download all files in provided urls
#

apt-get -q -y install nodejs > /dev/null

wget https://raw.githubusercontent.com/openfido/utilities/main/urldownload.js

node urldownload.js $OPENFIDO_INPUT || error

wget -P $OPENFIDO_INPUT --input-file=curls.txt
