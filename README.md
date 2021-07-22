# Dropbox

## Requirements
- make sure you have python 3.6 above
- install virtualenv ```pip install virtualenv```
- important docs (https://dropbox-sdk-python.readthedocs.io/
)
## The setup

- clone the repo ```git clone git@github.com:nadralia/Dropbox.git  ```
- cd to Dropbox where requirements.txt is located
- using virtualenv create a virtual env ```virtualenv venv ```
- activate your virtualenv, find how to activate for your machine but am using macos here is how to activate it ``` source venv/bin/activate ```.
- run: pip install -r requirements.txt in your shell.
- In order to build on top of Dropbox, you first need a Dropbox account (https://www.dropbox.com/), create one and install the app. After you’ve registered, head over to the developer section (https://www.dropbox.com/lp/developers).On the lefthand side click AppConsole.  Choose My apps on the lefthand side of the dashboard and click Create app, follow all the steps given.

## Grant Permission
Now you need to accept the file permissions
 - files.metadata.write
 - files.metadata.read
 - files.content.write
 - files.content.read

## Generate access token
After accepting all file permission go back to the setting tab, scroll down to OAuth 2 section
you will see the "Generated access token" button. Click on it to generate your access token

- copy the token and paste it in you .env file .. you have a .envsample file, make sure you rename it to .env

- inside the .env feel free to change the directory name ..but i advice you leave it the same way.

- make source the variable are there in the terminal ``` source .env``` will do for macos users
## Run the app
- run ``` python main.py ```
