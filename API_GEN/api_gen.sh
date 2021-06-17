#!/bin/bash
# Generage Python SDK library for interacting with Laserfiche API

# Get the latest URL from: https://api.laserfiche.com/repository/swagger/index.html
SWGSPEC='https://api.laserfiche.com/repository/swagger/v1-alpha/swagger.json'
USRAGT='Chrome/91.0.4472.106'
LFAPI=${PWD}/laserfiche_api

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
echo '' > ${PWD}/../dist/laserfiche_api.tar.gz
tar -czvf ${PWD}/../dist/laserfiche_api.tar.gz ${PWD}/laserfiche_api

# Commit package to repo

git add ${PWD}/../dist/laserfiche_api.tar.gz

git commit -m "Added/updated laserfiche_api.tar.gz"

#git push
