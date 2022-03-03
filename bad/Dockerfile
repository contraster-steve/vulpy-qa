FROM python:3.7-alpine

# Set the working directory and copy the code over
WORKDIR ./app/vulpy/bad
RUN apt --update add bash nano g++ gcc make autoconf automake alpine-sdk linux-headers flask
COPY . .

# Install dependencies
RUN pip3 install -r ./requirements.txt

# Set environment variables
RUN export FLASK_APP=vulpy
RUN export FLASK_ENV=development

# Create the atomizer container
FROM alpine:latest

WORKDIR /

# Add port 5002 
EXPOSE 5002

# Run Vulpy
ENTRYPOINT flask run --host=0.0.0.0
