#!/bin/bash
# Generage Python SDK library for interacting with Laserfiche API

# Get the latest URL from: https://api.laserfiche.com/repository/swagger/index.html
SWGSPEC='https://api.laserfiche.com/repository/swagger/v1-alpha/swagger.json'
USRAGT='Chrome/91.0.4472.106'
LFAPI=${PWD}/laserfiche_api
OPWD=${PWD}

if [ -d "$LFAPI" ]; then
    echo "$LFAPI folder exists. Cleaning up before rebuilding..."
    sudo rm -rfv $LFAPI
    sudo rmdir $LFAPI
fi

mkdir ${LFAPI}

# Generate "laserfiche_api" client from Laserfiche swagger spec
# Must use swagger-codegen v3 since JSON is OpenAPI 3.0 spec
docker run -it --rm \
    -v ${PWD}:/local \
    swaggerapi/swagger-codegen-cli-v3 generate \
    -i ${SWGSPEC} \
    --http-user-agent "$USRAGT" \
    -l python \
    -o /local/laserfiche_api \
    -DpackageName=laserfiche_api

# Package for PyPi
# cd ${PWD}/../dist
echo '' > ${PWD}/../dist/laserfiche-api.tar.gz
tar -czvf ${PWD}/../dist/laserfiche-api.tar.gz -C ${PWD} laserfiche_api


# Add package to repo

git add -f ${PWD}/../dist/laserfiche_api.tar.gz

git commit -m "Added/updated laserfiche-api.tar.gz"

git push

#pip install twine
#python setup.py sdist
#twine upload laserfiche-api.tar.gz