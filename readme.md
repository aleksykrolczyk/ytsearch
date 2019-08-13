# YTSearch

Simple app written in Python(flask) that finds videos from YouTube that match given query. In addition it is possible to to create an account and store one's search history.

## Installation
To install simply use pip:

    pip install -r requirements.txt

## Database
Simply run these two commands:

    flask db init
    flask db migrate
    flask db upgrade

## Running

    flask run