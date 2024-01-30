# Set base image (host OS)
FROM python:3.8-alpine

# By default, listen on port 5000
EXPOSE 5001/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev \
    make automake g++ subversion



# Install any dependencies
RUN pip install -r requirements.txt  


# Copy the content of the local src directory to the working directory
COPY . .



# Specify the command to run on container start
RUN ls
CMD [ "python", "./app.py" ]
