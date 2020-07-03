# Website for T.F. Ng Lun 

Website for physical shop to provide more infomation about the shop's services, location, and available products.

## Technologies used
Python 3.7  
Django 3.0.8  
Google Maps API  
Google App Engine  
Algolia - InstantSearch.js  
Bootstrap 4.5


## Usage

### Setup Environment

#### Install Git
**Note: You will need this to clone this repository**
- For Windows Users, download and install from https://gitforwindows.org/
- For linux Users, the distribution should already come installed with git.

#### Install Python (Miniconda/Anaconda)
Go to the following link to install Python in your system:  
1) Download installer:  
    https://docs.conda.io/en/latest/miniconda.html
2) Follow installation instructions:  
    https://conda.io/projects/conda/en/latest/user-guide/install/index.html
3) Once installed, make sure you can use conda/pip in command line:
    ```bash
    # anywhere in command line, to verify installation
    conda --version
    # conda 4.8.3

    pip list
    # Package             Version
    # ------------------- -------------------
    # appdirs             1.4.4
    # asn1crypto          0.24.0
    # ...
    ```
4) Install `pipenv` package:
    ```
    pip install pipenv
    ```

#### Install Google Cloud SDK (required for deploying to GAE)
- Download/Install from https://cloud.google.com/sdk/install  
- Follow this quickstart guide: https://cloud.google.com/sdk/docs/quickstart-windows
  - Create GCP project
  - Create billing account
  - Install the App Engine Extension for Python 3
    ```
    gcloud components install app-engine-python
    ```
  - Run `gcloud init`, then select the correct project

#### Setup working directory
1) Clone/Download repository source code:  
    Once Python is installed/setup, download/clone this repository to get the source code.
    ```bash
    git clone git@github.com:zckoh/tf-nglun.git
    ```

2) Install Python dependencies:  
    Go to project directory, use `pipenv` to install the required packages:
    ```bash
    cd tf-nglun
    pipenv install -r website/requirements.txt
    ```
    This will generate the `Pipfile` and `Pipfile.lock` files in the project directory

3) Setup `secrets` file:  
    For Django, we need to create a secret file `website/django_secret.txt` to keep the secret key:
    ```
    export DJANGO_SECRET="VALUE OF DJANGO_SECRET"
    ```
    For GAE, we also need to create a secret file `website/django_secret.yaml` which will contain the same secret key:
    ```
    env_variables:
      DJANGO_SECRET: 'VALUE OF DJANGO_SECRET'
    ``` 

### Now you are all set!

Note: do this step first before proceeding with the commands below.  
This activates the python virtualenv setup by pipenv when we did `pipenv install` earlier
```bash
cd tf-nglun
pipenv shell
```

### To run django locally
```bash
cd website
python manage.py runserver
```

### To deploy to GAE (Google App Engine):
```bash
cd website

## Collect all static files to be uploaded to GAE
python manage.py collectstatic

## Deploy to GAE
gcloud app deploy

## Once deployed, browse and check the website
gcloud app browse
```