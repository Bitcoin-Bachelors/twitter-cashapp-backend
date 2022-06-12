# Pull base image
FROM python:3.7.10-buster

RUN apt-get update && apt-get install build-essential libxmlsec1-dev pkg-config libpq-dev python-dev -yq && rm -rf /var/lib/apt/lists/*


# Install node and npm
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get update && apt-get install -y nodejs
RUN npm install npm@latest -g

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

# Copy project
COPY . .