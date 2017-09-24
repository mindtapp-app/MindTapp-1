# [MindTapp](http://mindtapp.com/)

## Developing Static Files

To use the source files, you will need to have npm installed globally along with Gulp.js. To start:
* Run `npm install` in the static directory
* Run `gulp dev` and edit the files as needed

If you need to update the plugins included with this template, simply run the following tasks:
* First run `npm update` to update the dependencies
* Then run `gulp copy` to copy the new versions to their proper destinations

Note, if you want to store static files in their own apps, be sure to copy over the gulp.js file and run it there seperately when developing that app

## Theme Creator

Start Bootstrap was created by and is maintained by **[David Miller](http://davidmiller.io/)**, Owner of [Blackrock Digital](http://blackrockdigital.io/).

* https://twitter.com/davidmillerskt
* https://github.com/davidtmiller

Start Bootstrap is based on the [Bootstrap](http://getbootstrap.com/) framework created by [Mark Otto](https://twitter.com/mdo) and [Jacob Thorton](https://twitter.com/fat).

## How to Login

0. Remember to add your IP to the AWS security group for port 22 (ssh)
1. Navigate to the directory that includes the .pem file.
2. chmod 600 keyname.pem  
3. ssh -i keyname.pem ubuntu@serveraddress
4. If a prompt asks you a yes/no question, answer yes.  
5. You should now be in the AWS server via terminal/PuTTY.

## How to update from GitHub repository

1. sudo su
2. cd /srv/MindTapp
3. source MindTappEnv/bin/source
4. git pull
5. systemctl nginx restart
6. systemctl gunicorn restart
7. double check if any changes were added to dev_settings, make sure prod_settings is manually updated appropriately for it

## How to activate the virtualenv

This step is necessary to seperate system and project requirements. All python/pip will be on the local settings, allowing for less of a headache in using python3.
1. sudo su
2. source /srv/MindTapp/MindTappEnv/bin/activate

## How to test locally

1. change directory to manage.py
2. pip install -r requirements.txt
3. python (MAKE SURE THIS IS PYTHON3) manage.py runserver

## Copyright and License

Copyright 2013-2016 Blackrock Digital LLC. Code released under the [MIT](https://github.com/BlackrockDigital/startbootstrap-agency/blob/gh-pages/LICENSE) license.
