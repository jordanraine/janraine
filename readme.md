##Team

> A test of the Janrain Social Login.

- __ Tester__: Jordan Hewus

## Table of Contents

1. [Usage](#usage)
1. [Requirements][#requirements]
1. [Development](#development]
    1. [Installing Dependencies](#installing-dependencies)
    1. [Deployment Steps](#deployment-steps)

## Usage
 - Download and unzip the repository
 - Install [dependencies](#installing-dependencies).
 - Set API key in console with:
 -   export JANRAIN_ENGAGE_API_KEY='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
## Requirements
 - Flask 0.10.1
 - Jinja2 2.7.3
 - Heroku 0.1.4
 - Gunicorn 19.3.0
 - Request 2.7.0

## Development

### Installing Depenencies

From within the root directory:

```pip install Flask
pip install jinja2
pip install gunicorn
pip install heroku
pip install request
```

### Deployment Steps
In the command line type:
- heroku login
- "follow steps to login with your heroku account and password."
- git init
- heroku git:remote -a "name of app on heroku dashboard"
- heroku config:set JANRAIN_ENGAGE_API_KEY=$JANRAIN_ENGAGE_API_KEY
- git add .
- git commit -am "This should work"
- git push heroku master
- heroku ps:scale web=1
