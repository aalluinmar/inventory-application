# Inventory-Application

> Inventory-Application

## Tech Stack

- Vue.js
- Python Django framework
- PostgreSQL ([download](https://www.pgadmin.org/download/))

## Setup Development Environment

    sudo apt-get -y update
    sudo apt-get -y install git python-pip postgresql postgresql-contrib wkhtmltopdf libcurl4-openssl-dev libssl-dev xvfb
    sudo pip install virtualenv

## Clone the code

    cd ~/
    git clone git@github.com:aalluinmar/inventory-application.git
    cd inventory-application

## Install Application Requirements for Development.

- For Backend Setup, go through ([Backend README](https://github.com/aalluinmar/inventory-application/tree/master/inventory_backend/README.md))

- For Frontend Setup, go through ([Frontend README](https://github.com/aalluinmar/inventory-application/tree/master/inventory_frontend/README.md))

## Start App Server by using following Commands

- For Backend Setup, after configuring Docker Desktop in your local Environment, just switch to inventory_backend directory and up the Docker Container.

    `cd inventory_backend/`

    `docker-compose up --build`

- For Frontend Setup, just switch to inventory_frontend directory and up the Docker Container.

    `cd inventory_frontend/`

    `docker-compose up --build`
    
- Open the Application using ([localhost](http://localhost:8080/))

## For Checking Backend Code Coverage and Unit Tests

- First Up the backend container and then use the following command to login into Docker Container.

- Switch to backend directory.

    `cd inventory_backend/`

- List the running containers using following Command.

    `docker ps`

- To login to Docker Container, use following command with the Backend Docker Container Id.

    `docker exec -it 'Container_Id' bash`

- Source the env file for running tests and checking coverage.

    `source dev.env`

- To run all Unit tests

    `coverage run manage.py test`

- To check Code Coverage and Unit Test Report.

    `coverage report -m --omit=manage.py`

## In production server, Create virtual environment and activate and Install Application Requirements regarding Backend.


    virtualenv -p python3 ~/env/inventory
    source ~/env/idso/bin/activate
    cd inventory_backend/
    pip3 install -r ./requirements/base.txt

    `Configure the supervisor inorder to make Containers up every time.`

## In production server, Create virtual environment and activate and Install Application Requirements regarding Frontend.

    Install Node and Vue CLI Service and build the project for production environment setup and configure within the `S3` bucket.
