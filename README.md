# Deploying in Kubernetes

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

## Description
This project has the sole purpose of serving as a template for a kubernetes deployment.
To serve the model I used the pickle stored in the `models` folder in this repo.
The application was deployed to a Container Registry, and the image (as can be seen in `Dockerfile`) was loaded in the kubernetes pods exposing the API (as can be seen in `deploy.py`)

## Project Organization
For the purposes of deploying in Kubernetes the code for this project was not made available in scripts
I used the Dockerfile to deploy the application via the `deploy_code.py` script and ran the `deploy.py` to expose the API in order to serve the model.
This project was tested in an Azure environment and for that, the folder azure-pipelines was used for Continuos Integration and Continuos Deployment
In the kubernetes folder lies all the configuration of the kubernetes cluster used
