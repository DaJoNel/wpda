#!/bin/bash

# Set bash variables
BASE_PATH=$PWD
USERNAME=`whoami`

# Dynamically generate the MySQL password
PASSWORD=$(cat /dev/urandom | tr -dc _A-Z-a-z-0-9 | head -c${1:-32})

# Set the MySQL password
sudo debconf-set-selections <<< "mysql-server mysql-server/root_password password $PASSWORD"
sudo debconf-set-selections <<< "mysql-server mysql-server/root_password_again password $PASSWORD"

# Add Node v6 repository
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -

# Install apt dependencies
sudo apt install -y git python-dev python-pip nodejs build-essential \
autoconf apache2 mysql-server libapache2-mod-wsgi libmysqlclient-dev

# Update pip and install pip dependencies
sudo -H pip install --upgrade pip
sudo -H pip install django djangorestframework djangorestframework-jsonapi \
markdown django-filter mysqlclient requests iso8601

# Update npm list and install dependencies
sudo npm install -g npm bower phantomjs-prebuilt ember-cli@2.8

# Install watchman from source and clean up afterword
git clone https://github.com/facebook/watchman.git ~/watchman/
cd ~/watchman/
git checkout v4.7.0
./autogen.sh
./configure --with-python
make && sudo make install
cd ../
sudo rm -rf watchman

# Allow Apache traffic through the firewall
sudo ufw allow in "Apache Full"

# Set up MySQL so Django can use it (password holder is a bit of a hack)
mysql -u"root" -p$PASSWORD -e "create database wpdaDB;"
sudo sed -i -e "s/\<passwd_holder\>/$PASSWORD/g" $BASE_PATH/server_config/my.cnf
sudo /bin/cp -rf $BASE_PATH/server_config/my.cnf /etc/mysql/
sudo chmod 644 /etc/mysql/my.cnf

# Download the WPDA client files
sudo git clone https://github.com/DaJoNel/wpda-client.git /var/www/wpda-client/

# Fix permissions
sudo chown -R $USERNAME:www-data /var/www/
sudo find /var/www/ -type d -exec chmod 775 {} +
sudo find /var/www/ -type f -exec chmod 664 {} +

# Configure Apache to serve Django
sudo /bin/cp -rf $BASE_PATH/server_config/django.conf /etc/apache2/sites-available/
sudo chmod 644 /etc/apache2/sites-available/django.conf
sudo a2ensite django
sudo a2dissite 000-default
sudo service apache2 restart

# Install Ember dependencies
cd /var/www/wpda-client/
bower install
ember install ember-bootstrap
npm install

# Make model migrations for Django
cd /var/www/wpda-server/
python manage.py makemigrations
python manage.py migrate

# Download some Waze Place data (e.g. Hy-Vee; note the use of regex)
python manage.py scrape "hy[ -]?vee"

# Report the MySQL root password to the user
echo -e "\n\n\n  MySQL password (retain for records):"
echo "  |----------------------------------|"
echo "  | $PASSWORD |"
echo -e "  |----------------------------------|\n\n\n"
