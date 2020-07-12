#!/bin/bash

django_root="$( cd "$(dirname "$0")/.." >/dev/null 2>&1 ; pwd -P )"

if grep -q "DEBUG = False" "${django_root}/website/settings.py"
then
    # code if found
    echo "DEBUG is currently set to False"
    echo "Setting DEBUG = True in settings.py ..."

    debug_line_number=`grep -n "DEBUG" ${django_root}/website/settings.py | cut -d : -f 1`
    sed -i "${debug_line_number}s/.*/DEBUG = True/" ${django_root}/website/settings.py
    if [[ $? -ne 0 ]]; then
        echo "ERROR: Failed to update DEBUG flag in settings.py"
        exit 1
    fi
    
    echo "Successfully updated settings.py"
else
    # code if not found
    echo "DEBUG is currently set to True"
    echo "Setting DEBUG = False in settings.py ..."

    debug_line_number=`grep -n "DEBUG" ${django_root}/website/settings.py | cut -d : -f 1`
    sed -i "${debug_line_number}s/.*/DEBUG = False/" ${django_root}/website/settings.py
    if [[ $? -ne 0 ]]; then
        echo "ERROR: Failed to update DEBUG flag in settings.py"
        exit 1
    fi
    
    echo "Successfully updated settings.py"
fi