#!/bin/bash

# script to automate local deploy/testing process

django_root="$( cd "$(dirname "$0")/.." >/dev/null 2>&1 ; pwd -P )"

cd ${django_root}

# Source the secrets file
echo "Loading the secrets as environment variables ..."
source ${django_root}/secrets.txt
if [[ $? -ne 0 ]]; then
    echo "ERROR: Failed to source the secrets file, aborted local_deploy script."
    exit 1
fi

# Updates the product list
pipenv run python scripts/update_product_list.py
if [[ $? -ne 0 ]]; then
    echo "ERROR: Failed to update product list, aborted local_deploy script."
    exit 1
fi

${django_root}/scripts/toggle_debug_flag.sh

pipenv run python manage.py runserver

${django_root}/scripts/toggle_debug_flag.sh

exit 0
