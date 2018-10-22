# perfect-blog


By abdirahman mahat

## Specifications

[SPECS.md](https://github.com/abdirahman-mahat/perfect-blog//master/specs.md)

### Set-UP and Installation
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.

* Python 3.6

### Cloning the repository

```git clone https://github.com/abdirahman-mahat/Perfect-blog.git```


### Database migrations

```bash
# first initialize the database if the migrations folder does not exist
python manage.py db init
# create  a migration
python manage.py db migrate -m "initial migration"
# upgrade
python manage.py db upgrade
# insert initial data
python manage.py insert_initial_data
```

### Installing dependencies

```
pip3 install -r requirements
```

### Prepare environmet variables

In start.sh file, in the root folder

```bash
 export MAIL_USERNAME=YOUR EMAIL
 export MAIL_PASSWORD=EMAIL PASSWORD
```



### Creating a virtual environment

```
python3.6 -m virtualenv virtual
source virtual/bin/activate
```
### Running Tests

```bash
python3.6 manage.py test
```


# Known Bugs
No bugs known.

## Live Demo

The web app can be accessed from the following link
[click here](https://perfect-blog.herokuapp.com/)


## Technology used

* [Python3.6](https://www.python.org/)

* [Flask](http://flask.pocoo.org/)

* [Heroku](https://heroku.com)

* [Bootstrap](https://bootstrapcdn.com)





## License

MIT License

&copy;  abdirahman mahat
