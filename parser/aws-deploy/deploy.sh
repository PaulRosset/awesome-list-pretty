#!/bin/bash

rm -rf algolia-deploy.zip
pip install algoliasearch -t ./
zip -r algolia-deploy.zip *
rm -rf */
