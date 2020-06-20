#!/bin/bash


### removes any old versions that is not serving traffic
### Ideally used after deploying a newer version


script_dir="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

echo "Listing all available versions..."
gcloud app versions list

echo "Finding old versions that are not serving traffic anymore..."
old_versions=($(gcloud app versions list --format="table[no-heading](version.id)" --filter="TRAFFIC_SPLIT=0.00"))

if [[ ${#old_versions[@]} -ne 0 ]]; then
    echo "Found old versions that can be deleted:"
    for version in "${old_versions[@]}"; do
        echo "${version}"
    done

    echo "gcloud app versions delete ${old_versions[@]}"
    gcloud app versions delete ${old_versions[@]}
else
    echo "Could not find any old versions that can be deleted."
fi

exit 0