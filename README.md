# E-commerce website side project

**See it live in production:** https://www.tfnglun.com

Website for physical shop to provide more infomation about the shop's services, location, and available products.  

- **Home page** - provides a basic landing page and a notice section to show users any new update/notice.

- **Products page** - contains list of all the products, provides a fast search bar that allows users to easily search for products. 
  - Uses **Algolia search** to index all the products.
  - Uses **Algolia InstantSearch.js** for the front-end widgets in products page.
  - Uses **Google Cloud Storage** buckets to store the uploaded images.
  - Uses **mongoDB-Atlas** to store product information.

- **Admin page** - allows shop owner to easily perform **CRUD** operations on products / notices, without having to deal with any source code.

- **Contacts page** - shows the shop information, contact details and provides a contact form to allow users to send any enquiries.
  - A map showing the shop's location using **Google Maps Javascript API** 
  - A simple **google recaptcha** widget is used to prevent any potential spamming of the contact form. 
  - Once contact form is filled and submitted, the django backend uses **Mailjet REST API** to send the contact form via email to the shop's email address.

- **SEO** 
  - Added meta tags in all pages (viewport, robots, HandheldFriendly, MobileOptimized, og:* tags)
  - Added favicons links/tags
  - Added canonical tags on all pages
  - Added robots.txt
  - Added sitemap.xml generated via django-sitemaps

## Future Improvements
- Implement online payment solution using services like Stripe / Shopify.
- Migrate to AWS.

## Technologies used
Python 3.7  
Django 3.0.8  
Google Maps API  
Google App Engine  
MongoDB Atlas  
Google Cloud Storage  
Algoliasearch  
Algolia - InstantSearch.js  
Mailjet Rest API  
Bootstrap 4.5


## Usage

### Setup Environment

#### Install Git
**Note: You will need this to clone this repository**
- For Windows users, download and install from https://gitforwindows.org/
- For linux users, the distribution should already come installed with git.

#### Install Python (Miniconda/Anaconda)
Go to the following link to install Python in your system:  
1) Download installer (Miniconda only):  
    https://docs.conda.io/en/latest/miniconda.html
2) Follow installation instructions:  
    https://conda.io/projects/conda/en/latest/user-guide/install/index.html
3) Once installed, run commands `conda --version` followed by `pip list` to verify installation. You should see something similar to the outputs below:
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

  Summary of quickstart guide:  
  - Create GCP project (skip if already done)
  - Create billing account (skip if already done)
  - Install the App Engine Extension for Python 3
    ```
    gcloud components install app-engine-python
    ```
  - Run `gcloud init`, then you will be prompted to login to your google cloud account. Click "allow" to login.
  - Then you will prompted to select your cloud project on the command line.

#### Setup working directory
1) Clone/Download repository source code:  
    Once Python is installed/setup, download/clone this repository to get the source code.
    ```bash
    git clone git@github.com:zckoh/ecommerce-fullstack.git
    ```

2) Install Python dependencies:  
    Go to project directory, use `pipenv` to install the required packages:
    ```bash
    cd ecommerce-fullstack
    pipenv install django algoliasearch-django mailjet-rest djongo django-storages[google] django-cleanup Pillow dnspython
    ```
    This will install the required packages and generate the `Pipfile` and `Pipfile.lock` files in the project directory

    Then run the following command to save the dependencies list to `website/requirements.txt`:
    ```bash
    pipenv run pip freeze > website/requirements.txt
    ```

3) Setup `secrets` file:  
    Use the following commands to create the 2 `secrets` files:  
    ```bash
    touch website/secrets.txt
    touch website/secrets.yaml
    ```

    First add the following lines in the two files (we will fill in the values in the next step):
    - `secrets.txt` (Please save the file with LF line sequence) :
        ```bash
        export DJANGO_SECRET=""
        export ALGOLIA_ADMIN_API_KEY=""
        export MJ_APIKEY_PUBLIC=''
        export MJ_APIKEY_PRIVATE=''
        export MONGO_DB_USERNAME=''
        export MONGO_DB_PASSWORD=''
        export GS_CLOUD_KEY_FILENAME='path_to.json'
        ```
    - `secrets.yaml` (Please save the file with LF line sequence) :
        ```bash
        env_variables:
            DJANGO_SECRET: ''
            MJ_APIKEY_PUBLIC: ''
            MJ_APIKEY_PRIVATE: ''
            ALGOLIA_API_KEY: ''
            MONGO_DB_USERNAME: ''
            MONGO_DB_PASSWORD: ''
            GS_CLOUD_KEY_FILENAME: 'path_to.json'
        ```

    For `DJANGO_SECRET`, run the following command which will generate a string of random characters:
    ```
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```

    Copy the string of random characters generated, and paste the string as the value of `DJANGO_SECRET` .

    For `ALGOLIA_API_KEY`, go to https://www.algolia.com/apps/PROJECTID/api-keys/all, and copy the Admin API Key and paste the API Key as the value of `ALGOLIA_API_KEY`.

    For `MJ_APIKEY_PUBLIC` and `MJ_APIKEY_PRIVATE`, login to Mailjet account, and head to "Account Settings", then click on "Master API Key & Sub API key management", there you will find the 2 keys. Copy and paste them into the two secrets file accordingly. 

### Now you are all set!

### To run django locally:
```bash
cd ecommerce-fullstack
pipenv shell

### Use local_deploy script
./website/scripts/local_deploy.sh

### OR do it manually 

cd website
source secrets.txt

## NOTE: DON'T FORGET TO SET DEBUG = True in website/settings.py first when testing locally
python manage.py runserver
```

### To deploy to Production/GAE (Google App Engine):
Use `deploy.sh` script:
```bash
cd website
./scripts/deploy.sh
```
