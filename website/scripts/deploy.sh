#!/bin/bash

# Updates the product list
# collect static files
# deploy to GAE

django_root="$( cd "$(dirname "$0")/.." >/dev/null 2>&1 ; pwd -P )"

cd ${django_root}

# Source the secrets file
echo "Loading the secrets as environment variables ..."
source ${django_root}/secrets.txt
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

${django_root}/scripts/remove_old_versions.sh


exit 0
