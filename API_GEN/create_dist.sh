#!/bin/bash

BUILDROOT=/tmp/laserfiche-api
HOMEROOT=/home/runner/work/laserfiche-api/laserfiche-api/API_GEN

cp -f $HOMEROOT/setup.py $BUILDROOT/setup.py

cd $BUILDROOT

python3 setup.py sdist
