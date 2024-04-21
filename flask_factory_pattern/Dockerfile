# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /flask_factory_pattern

# Set the working directory to /flask_factory_pattern
WORKDIR /flask_factory_pattern

# Copy the current directory contents into the container at /flask_factory_pattern
ADD . /flask_factory_pattern

# Install any needed packages specified in requirements.txt
RUN apt-get update
RUN pip install -r requirements.txt


# port where the Flask app runs  
EXPOSE 8025 

# start server  
CMD uwsgi --ini app.ini