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
    For Django, it requires a DJANGO_SECRET, which can be generated using the following command:
    ```
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```
    Then we need to create a secret file `website/django_secret.txt` to keep the secret key:
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

### To run django locally:
```bash
cd website
python manage.py runserver
```

### To deploy to Production/GAE (Google App Engine):
```bash
## WARNING: Don't forget to update DEBUG value to False in website/settings.py 
cd website

## Collect all static files to be uploaded to GAE
python manage.py collectstatic

## Deploy to GAE
gcloud app deploy

## Once deployed, browse and check the website
gcloud app browse
```

### To add new products:
#### Adding product to existing product category
1) Prepare the product image (ideally a .jpg file)
2) Add the image to correct directory:  `website/static/catalogue/<product_category>/image.jpg`
3) Add the following product information in `website/catalogue/data/<product_category>/product_list.json`
   Edit the values below to fit your product:
   ```json
    {
        "product_name": "Zebra Mechanical Pencil, Air Fit S, 0.5mm",
        "model_no": "MA19",
        "product_category": "Pens",
        "belong_to": "pens_catalogue",
        "product_details": [
            "Mechanical Pencil, Air fit s",
            "With silicone grip",
            "For 0.5mm lead, assorted colors"
        ],
        "product_image_path": "catalogue/pens/zebra-airfit.jpg",
        "url_name": "zebra_airfit",
        "url_link": "pens/zebra_airfit.html"
    }
   ```
4) Update the index in Algolia
   - Go to the Algolia dashboard for this project - https://www.algolia.com/apps/9SXIDIVU1E/dashboard
   - Select "Add records", then select "Add manually"
   - Copy the JSON data that you provided in step 3 and paste it in.
   - Click "Save"
5) Repeat steps 1-4 if you have more products to add, else proceed to next step
5) Verify changes
   - Run local django server, verify that the new product is added
     ```bash
     python manage.py runserver
     ```
6) Save changes and commit/push to Git
   - Save changes
   - `git add` the new/updated files
   - Make a `git commit`
   - `git push`
7) Deploy to production!


#### Adding product to new product category