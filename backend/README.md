# random_github backend

## Running the server

> `uvicorn main:app --reload`

## Setting up datastore communication

`$env:GOOGLE_APPLICATION_CREDENTIALS="key.json"`

## Setting up terraform

Make sure you have `key.json` available

Make sure you've enabled all used APIs

Sensitive variables are currently typed in by hand, so you need to know them if you want to deploy anything, will be changed in some point in the future probably.

You can deploy new version of whatever you are deploying simply by running: `terraform apply`
