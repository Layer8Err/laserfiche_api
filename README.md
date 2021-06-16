# laserfiche_api
Swagger-Codegen auto-generated Laserfiche Cloud API SDK created from swagger.json

# Documentation

* [Laserfiche API](https://api.laserfiche.com/repository/swagger/index.html)
* [Swagger Codegen](https://swagger.io/tools/swagger-codegen/)

# Build info

The Laserfiche API has been built to work with OpenAPI 3.0.0. Because of this, swagger-codegen v3 must be used.

The `api_gen.sh` script under the `API_GEN` folder will spin up a Docker container running `swagger-codegen-cli-v3` and export the `laserfiche_api` SDK to a folder with the same name.

If the resulting SDK files are pushed to their own repo, they can be installed with:

```bash
pip install git+https://github.com/layer8err/laserfiche_api/API_GEN/laserfiche_api
```

You can also manually install via setuptools:

```bash
python setup.py install --user
```

