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
- Flask==0.10.1
- Jinja2==2.7.3
- MarkupSafe==0.23
- Werkzeug==0.10.4
- argparse==1.2.2
- gunicorn==19.3.0
- heroku==0.1.4
- itsdangerous==0.24
- pbr==0.10.0
- python-dateutil==1.5
- requests==2.7.0
- stevedore==1.1.0
- virtualenv==1.11.6
- virtualenv-clone==0.2.5
- virtualenvwrapper==4.3.1
- wsgiref==0.1.2
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
