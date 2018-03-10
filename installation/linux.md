# Setup MongoDB on Ubuntu

Recommended version is via apt

* Visit Ubuntu setup page at mongodb.com
* Add key:  sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
* Add list file, careful on version: echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
* Update: sudo apt-get update
* Install: sudo apt install mongodb-org
* Set permissions:
    * sudo chmod 777 /var/lib/mongodb
    * sudo chmod 777 /var/log/mongodb/
* Start service: sudo service mongod start
    * Review config: /etc/mongod.conf

See MongoDB's full instructions at:

[docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)