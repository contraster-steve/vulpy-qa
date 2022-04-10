FROM python:3.7

# Set the working directory and copy the code over
WORKDIR /app/vulpy/bad
COPY . .

# Install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt

ENV FLASK_APP=vulpy
ENV FLASK_ENV=development

RUN chmod +x ./startup.sh

# Add port 5000
EXPOSE 5000

# Run Vulpy
ENTRYPOINT ["/bin/sh", "startup.sh"]
