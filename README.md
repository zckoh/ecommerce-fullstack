# Website for T.F. Ng Lun 

Website for physical shop to provide more infomation about the shop's services, location, and available products.

## Technologies used
Python 3.7  
Django 3.0.8  
Google Maps API  
Google App Engine  
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
    ## Go to the folder you where you want to keep the project
    mkdir scratch
    cd scratch

    ## via ssh key
    git clone git@github.com:zckoh/tf-nglun.git

    ## via https request (requires password)
    git clone https://github.com/zckoh/tf-nglun.git
    ```

2) Install Python dependencies:  
    Go to project directory, use `pipenv` to install the required packages:
    ```bash
    cd tf-nglun
    pipenv install django~=3.0.8
    pipenv shell
    
    pip install algoliasearch~=2.3.0 autopep8~=1.5.3 mailjet-rest~=1.3.3
    ```
    This will install the required packages and generate the `Pipfile` and `Pipfile.lock` files in the project directory

    Then run the following command to save the dependencies list to `website/requirements.txt`:
    ```bash
    pipenv run pip freeze > website/requirements.txt
    ```

3) Setup `secrets` file:  
    Use the following commands:  
    ```bash
    # creates a file named "secrets.txt" in the directory "website"
    touch website/secrets.txt

    # creates a file named "secrets.yaml" in the directory "website"
    touch website/secrets.yaml
    ```

    First add the following lines in the two files (we will fill in the values in the next step):
    - `secrets.txt` (Please save the file with LF line sequence) :
        ```bash
        export DJANGO_SECRET=""
        export ALGOLIA_ADMIN_API_KEY=""
        export MJ_APIKEY_PUBLIC=''
        export MJ_APIKEY_PRIVATE=''
        ```
    - `secrets.yaml` (Please save the file with LF line sequence) :
        ```bash
        env_variables:
          DJANGO_SECRET: ''
          MJ_APIKEY_PUBLIC: ''
          MJ_APIKEY_PRIVATE: ''
        ```

    For `DJANGO_SECRET`, run the following command which will generate a string of random characters:
    ```
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```

    Copy the string of random characters generated, and paste the string as the value of `DJANGO_SECRET` .

    For `ALGOLIA_ADMIN_API_KEY`, go to https://www.algolia.com/apps/9SXIDIVU1E/api-keys/all, and copy the Admin API Key and paste the API Key as the value of `ALGOLIA_ADMIN_API_KEY`.

    For `MJ_APIKEY_PUBLIC` and `MJ_APIKEY_PRIVATE`, login to Mailjet account, and head to "Account Settings", then click on "Master API Key & Sub API key management", there you will find the 2 keys. Copy and paste them into the two secrets file accordingly. 

4) Now the following files should look something like this (values below are example values):
   - `website/secrets.txt`: 
        ```bash
        # WARNING: make sure this file is saved as LF file sequence
        export DJANGO_SECRET="1234567890qwertyuiop[]asdfghjklzxcvbnm"
        export ALGOLIA_ADMIN_API_KEY="abcdefghijklmnopqrstuvwxvyz"
        export MJ_APIKEY_PUBLIC='abcdefghijklmnop1234567890'
        export MJ_APIKEY_PRIVATE='abcdefghijklmnop1234567890'
        ```
   - `website/secrets.yaml`:
        ```yaml
        # WARNING: make sure this file is saved as LF file sequence
        env_variables:
          DJANGO_SECRET: '1234567890qwertyuiop[]asdfghjklzxcvbnm'
          MJ_APIKEY_PUBLIC: 'abcdefghijklmnop1234567890'
          MJ_APIKEY_PRIVATE: 'abcdefghijklmnop1234567890'
        ```

### Now you are all set!

Note: do this step first before proceeding with the commands below.  
This activates the python virtualenv setup by pipenv when we did `pipenv install` earlier
```bash
cd tf-nglun
pipenv shell
```

### To run django locally:
```bash
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

# run the script
./scripts/deploy.sh
# Then follow the prompts accordingly
```

### To add new products:
#### Adding product(s) to existing product category
1) First in the project directory,  do a `git pull` to get any new changes:
   ```bash
   cd tf-nglun
   git pull
   ```
2) Prepare the product image(s) (ideally a .jpg file)
3) Add the image(s) to correct directory:  `tf-nglun/website/static/products/<product_category>/image.jpg`
4) Go to Algolia products_index indices for this project - https://www.algolia.com/apps/9SXIDIVU1E/explorer/browse/products_index
5) Select "Add records", then select "Add manually"
6) Copy the JSON example below and replace the field values according to the product details:  
   JSON example
   ```json
    }
        "product_name": "Cahier 17x22 Travaux Pratiques 64pg Polypro",
        "model_no": "n/a",
        "product_category": "Cahiers",
        "product_details": [
            "Format 17x22",
            "64 pages",
            "Travaux Pratiques",
            "Couverture Polypro",
            "Marque Calligraphe",
            "Disponible uniquement en incolore"
        ],
        "main_product_image": "products/copybooks/cahier_tp_64p_calligraphe_pp.jpg",
        "additional_images": [],
        "url_name": "17x22_tp_64pg_seyes_calligraphe",
        "url_link": "cahiers/17x22_tp_64pg_calligraphe.html",
        "objectID": "5650201"
    },
   ```
7) Click "Save"
8) Repeat steps 2-7 if you have more products to add, else proceed to next step
9)  Verify changes
   - Run local django server, verify that the new product is added
     ```bash
     ./website/scripts/local_deploy.sh
     ## after testing, quit the server with CONTROL+C
     ```
10) Save changes and commit/push to Git
    - Save changes
    - `git add` the new/updated files:
        ```bash
        git add products/data/product_list.json
        git add static/products/<product_category>/<your_new_image>.jpg
        ```
    - Make a `git commit`
    - `git push`
11) Deploy to production!


#### Adding product(s) of a new product category
1) First in the project directory,  do a `git pull` to get any new changes:
   ```bash
   cd tf-nglun
   git pull
   ```
2) Prepare the product image(s) (ideally a .jpg file)
3) Create a new folder for the new product category: `tf-nglun/website/static/products/<NEW_product_category>/`
4) Add the image(s) to correct directory:  `tf-nglun/website/static/products/<NEW_product_category>/image.jpg`
5) Go to Algolia products_index indices for this project - https://www.algolia.com/apps/9SXIDIVU1E/explorer/browse/products_index
6) Select "Add records", then select "Add manually"
7) Copy the JSON example below and replace the field values according to the product details:  
   JSON example
   ```json
    }
        "product_name": "Cahier 17x22 Travaux Pratiques 64pg Polypro",
        "model_no": "n/a",
        "product_category": "Cahiers",
        "product_details": [
            "Format 17x22",
            "64 pages",
            "Travaux Pratiques",
            "Couverture Polypro",
            "Marque Calligraphe",
            "Disponible uniquement en incolore"
        ],
        "main_product_image": "products/copybooks/cahier_tp_64p_calligraphe_pp.jpg",
        "additional_images": [],
        "url_name": "17x22_tp_64pg_seyes_calligraphe",
        "url_link": "cahiers/17x22_tp_64pg_calligraphe.html",
        "objectID": "5650201"
    },
   ```
8) Click "Save"
9) Repeat steps 2-7 if you have more products to add, else proceed to next step
10)  Verify changes
   - Run local django server, verify that the new product is added
     ```bash
     ./website/scripts/local_deploy.sh
     ## after testing, quit the server with CONTROL+C
     ```
11) Save changes and commit/push to Git
    - Save changes
    - `git add` the new/updated files:
        ```bash
        git add products/data/product_list.json
        git add static/products/<NEW_product_category>/<your_new_image>.jpg
        ```
    - Make a `git commit`
    - `git push`
12) Deploy to production!