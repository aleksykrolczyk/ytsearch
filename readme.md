# YTSearch

Simple app written in Python(flask) that finds videos from YouTube that match given query. In addition it is possible to to create an account and store one's search history.

## Installation
To install simply use pip:

    pip install -r requirements.txt

It is also possible (in case of errors connected to webscrapping) that You will need to run `Install Certificates.command` from Your Python directory.

## Database
Simply run these three commands:

    flask db init
    flask db migrate
    flask db upgrade

## Running

    flask run