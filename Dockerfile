# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:alpine

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=flaskexp Version=0.0.1
EXPOSE 55181

WORKDIR /app
ADD . /app

# Using pip:
# RUN pip install -r requirements.txt
# CMD ["python", "index.py"]

# Using pipenv:
# RUN python -m pip install pipenv
# RUN pipenv install --ignore-pipfile
# # CMD ["pipenv", "run", "python3", "-m", "flaskexp"]
# CMD ["python", "index.py"]

# Using miniconda (make sure to replace 'myenv' w/ your environment name):
#RUN conda env create -f environment.yml
#CMD /bin/bash -c "source activate myenv && python3 -m flaskexp"
