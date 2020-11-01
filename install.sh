#!/usr/bin/env bash
# Install Apache, PHP, npm
DEBIAN_FRONTEND=noninteractive sudo apt-get update && \
    sudo apt-get install -y python3 npm apache2 php libapache2-mod-php
npm install --user localtunnel
sudo a2enmod mpm_prefork && sudo a2enmod php7.2
sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && unzip ngrok-stable-linux-amd64.zip && rm ngrok-stable-linux-amd64.zip
# Set up ngrok if needed
while true; do
  read -r -p "Is ngrok configured on this machine?{y/n} " EXISTS
  if [ "$EXISTS" == "y" ]; then
    break
  elif [ "$EXISTS" == "n" ]; then
    ./ngrok authtoken 1jfJy5rqJ78yO5cyT413WF5OPSl_7Ng4UzzJ5Uvwm3cfQkfDQ
    break
  fi
done


sudo service apache2 restart

printf "\n\nTo run, use command:\n\n  \033[94;1msudo python3 webfor.py\n\n"
