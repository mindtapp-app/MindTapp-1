# [MindTapp](http://mindtapp.com/)

## Developing Static Files

To use the source files, you will need to have npm installed globally along with Gulp.js. To start:
* Run `npm install` in the static directory
* Run `gulp dev` and edit the files as needed

If you need to update the plugins included with this template, simply run the following tasks:
* First run `npm update` to update the dependencies
* Then run `gulp copy` to copy the new versions to their proper destinations

## Theme Creator

Start Bootstrap was created by and is maintained by **[David Miller](http://davidmiller.io/)**, Owner of [Blackrock Digital](http://blackrockdigital.io/).

* https://twitter.com/davidmillerskt
* https://github.com/davidtmiller

Start Bootstrap is based on the [Bootstrap](http://getbootstrap.com/) framework created by [Mark Otto](https://twitter.com/mdo) and [Jacob Thorton](https://twitter.com/fat).

## How to Login

1. Navigate to the directory that includes the .pem file.  
2. chmod 600 keyname.pem  
3. ssh -i keyname.pem ubuntu@serveraddress
4. If a prompt asks you a yes/no question, answer yes.  
5. You should now be in the AWS server via terminal/PuTTY.

## How to update from GitHub repository

1. cd /var/www/MindTapp  
2. sudo git pull
3. sudo service nginx restart
4. sudo service gunicorn restart

## How to activate the virtualenv

This step is necessary to seperate system and project requirements. All python/pip will be on the local settings, allowing for less of a headache in using python3.
1. sudo su
2. source /srv/MindTapp/MindTappEnv/bin/activate

## Copyright and License

Copyright 2013-2016 Blackrock Digital LLC. Code released under the [MIT](https://github.com/BlackrockDigital/startbootstrap-agency/blob/gh-pages/LICENSE) license.
