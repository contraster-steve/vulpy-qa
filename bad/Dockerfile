FROM python:3.7

# Set the working directory and copy the code over
WORKDIR ./app/vulpy/bad
COPY . .

# Install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt

RUN chmod +x ./startup.sh

# Create the atomizer container
FROM python:3.7

WORKDIR ./app/vulpy/bad
RUN ls -la

# Add port 5002 
EXPOSE 5002

# Run Vulpy
ENTRYPOINT ["/bin/sh", "startup.sh"]
