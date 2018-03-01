# This application works in conjunction with:
* https://github.com/Sergei-vb/async_test
* https://github.com/Sergei-vb/docker_database

# It is necessary to set globally:
1. Docker CE https://docs.docker.com/install/
2. Docker Compose https://docs.docker.com/compose/install/

# You need to go to the directory with the Dockerfile of the cloned repository, then:
1. Create Image: `docker build -t django_alpine .`
2. Run Container: `docker-compose up`

# If you want to run the application in the virtualenv:
* You need to fill in the file `HighHopes/dev.py.template` with your values
* Rename it to `HighHopes/dev.py`
* Run the command: `./manage.py migrate`
* Run the command: `./manage.py runserver`
