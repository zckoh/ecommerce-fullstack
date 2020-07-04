#!/bin/bash

# Updates the product list
# collect static files
# deploy to GAE

django_root="$( cd "$(dirname "$0")/.." >/dev/null 2>&1 ; pwd -P )"

cd ${django_root}

# Source the secrets file
echo "Loading the secrets as environment variables ..."
source ${django_root}/django_secret.txt
if [[ $? -ne 0 ]]; then
    echo "ERROR: Failed to source the secrets file, aborted deployment."
    exit 1
fi

# Updates the product list
pipenv run python scripts/update_product_list.py
if [[ $? -ne 0 ]]; then
    echo "ERROR: Failed to update product list, aborted deployment."
    exit 1
fi

# Set DEBUG=False in settings.py
echo "Setting DEBUG = False in settings.py ..."
debug_line_number=`grep -n "DEBUG" ${django_root}/website/settings.py | cut -d : -f 1`
sed -i "${debug_line_number}s/.*/DEBUG = False/" ${django_root}/website/settings.py
if [[ $? -ne 0 ]]; then
    echo "ERROR: Failed to set DEBUG = False in settings.py, aborted deployment."
    exit 1
fi

# Collects the static file
pipenv run python manage.py collectstatic
if [[ $? -ne 0 ]]; then
    echo "ERROR: Failed to collect static files, aborted deployment."
    exit 1
fi

# Proceed to deploy to GAE
gcloud app deploy
if [[ $? -ne 0 ]]; then
    echo "ERROR: Failed to deploy to GAE, aborted deployment."
    exit 1
fi

# Set DEBUG=True in settings.py once finished deploying
echo "Setting back DEBUG = True in settings.py ..."
debug_line_number=`grep -n "DEBUG" ${django_root}/website/settings.py | cut -d : -f 1`
sed -i "${debug_line_number}s/.*/DEBUG = True/" ${django_root}/website/settings.py
if [[ $? -ne 0 ]]; then
    echo "WARNING: Failed to set DEBUG = True in settings.py"
    exit 1
fi

exit 0
