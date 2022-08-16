## Problem Statement

The goal of Calrifornia House Price prediction project is to predict the efficient house pricing for realestate customers with respect to their budgets and priorities.
It will aslo help us understand the relationship between house features and how these variables are used to predict house price.

## Data Ingestion

1. In this phase we will download the dataset from the URL.
2. The data present in the URL is in zip file we will extract that data and convert the data into train and test split in this phase.

## Data Validation.

1. In This step, we perform different sets of validation on the available data.
2. We validate the number of columns present,the datatype of columns,etc in the data with the help of the schema file
3. We also validate if there is a data drift present in the train and test data.

## Data Transformation

1. In this phase we add some feature which will help us increase the accuracy of the model.Also perform the different EDA techinques such as the scaling,imputing,encoding for the categorical features.
2. And after the transformation of the data this data is stored in transformed train and test directory.

## Model Trainer

1. The data stored in the transformed train and test directories is loaded and with the help of model_config.yaml file the best model is calculated for both train and test dataset and depending on the base accuracy the best model is accepted.
2. In this we have also created a function which will combine the preprocessing model and the best model selected and then this model is stored.

## Model Evaluation.

1. This phase is created to implement the model retraining approach.
2. Here we evaluate our previous model with the new model which we have achieved with the help of the new data.
3. And then the best model among this is saved.

## Model pusher.
1. This phase is used to export and store the best model.


-----------------------------------------------------------

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = anishyadav7045075175@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-regression-app

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```

''''''
python setup.py install
......

Install ipynb kernel
------
pip install ipykernel
