# Vulpy with Contrast
Vulpy is a web application developed in Python / Flask / SQLite that has two faces.

**BAD** (instrumented with Contrast): Purposefully vulnerable application code. 

**GOOD** (not instrumented with Contrast): Tries to code with secure development best practices in mind.

Features
--------

- Login/Logout
- Read posts from other users
- Publish posts
- Multi-Factor Authentication (MFA)
- API for read and write posts
- Content Security Policy
- SSL/TLS Server


Vulnerabilities
---------------

Some of the vulnerabilities present on the "BAD" version:

- Cross-Site Scripting (XSS)
- SQL Injection
- Cross Site Request Forgery (CSRF)
- Session Impersonation
- Insecure Deserialization
- Authentication Bruteforce
- Authentication Bypass

**Note:** The "GOOD" version (not finished yet) is supposed to don't have vulnerabilities, but I'm a human being, so...

## WARNING!
THIS WEB APPLICATION CONTAINS NUMEROUS SECURITY VULNERABILITIES WHICH WILL RENDER YOUR COMPUTER VERY INSECURE WHILE RUNNING! IT IS HIGHLY RECOMMENDED TO COMPLETELY DISCONNECT YOUR COMPUTER FROM ALL NETWORKS WHILE RUNNING!

## Google Chrome Note
Google Chrome performs filtering for reflected XSS attacks. These attacks will not work unless chrome is run with the argument `--disable-xss-auditor`.

### Contrast Instrumentation 
This repo includes the components necessary to instrument contrast Assess/Protect with this Python application except for the contrast_security.yaml file containing the connection strings.

Specifically modified:

1. This app uses a wrapper.py script to call vuply.py. Vulpy.py (the main part of this app) hasn't been modified to include Contrast. The wrapper includes the Contrast Middleware component "from contrast.flask import ContrastMiddleware" and uses a function to call the main application.
2. Updated requirements.txt to inlcude contrast-agent and an update to the library "setuptools" to make it not vulnerable.
3. The inclusion of a new file, "startup.sh" which is used to export the Flask environment variables and run the application on 0.0.0.0 (making it accessible via the Internet instead of localhost).
4. The Dockerfile upgrades the version of pip, installs the requirements, updates the database with seed data, and runs the startup.sh script.
5. The docker-compose.yml sets a few other specific environment variables. Unlike other application languages, I'm letting the agent pick the contrast_security.yaml file up from the root of the application which is the /bad/ directory.
6. Three other docker-compose YAMLs depending on what "environment" you're wanting to run: Development, QA, or Production.

contrast_security.yaml example:

api:<br>
&nbsp;&nbsp;url: https://apptwo.contrastsecurity.com/Contrast<br>
&nbsp;&nbsp;api_key: [REDACTED<br>
&nbsp;&nbsp;service_key: [REDACTED]<br>
&nbsp;&nbsp;user_name: [REDACTED]<br>
application:<br>
&nbsp;&nbsp;session_metadata: buildNumber=${BUILD_NUMBER}, committer=Steve Smith #buildNumber is inserted via Jenkins Pipeline<br>

Your contrast_security.yaml file needs to be in the root of the web application directory. It then gets copied into the Docker Container.

# Requirements

1. Docker Community Edition
2. docker-compose

When built, the Dockerfile pulls all of the code into the Docker Container. 

## How to build and run

### 1. Running in a Docker Container

The provided Dockerfile is compatible with both Linux and Windows containers (note from Steve: I've only run it on Linux).

To build a Docker image, execute the following command: docker-compose build

### Linux Containers

To run the `vulpy` Container image, execute one of the following commands:

1. Development: docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d

2. QA: docker-compose -f docker-compose.yml -f docker-compose.qa.yml up -d

3. Production (this disables Assess and enables Protect): docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

Vulpy should be accessible at http://ip_address:5000.


### Stopping the Docker container

To stop the `vulpy` container, execute the following command in the same directory as your docker-compose files: docker-compose stop 

### 2. Building with Jenkins
Included is a sample Jenkinsfile that can be used as a Jenkins Pipeline to build and run the application. The Jenkins Pipeline passes buildNumber as a parameter to the YAML. 

#### Default user accounts
The database comes pre-populated with these user accounts created as part of the seed data -
* Admin Account - u:admin p:SuperSecret 
* User Accounts - u:elliot p:123123123, u:tim p:12345678
* New users can also be added using the sign-up page.
