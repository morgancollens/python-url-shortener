# Python URL Shortener

A simple project built using Python and Flask as a learning exercise. Designed to allow users to shorten a URL and then access
the original URL through the shortened version.

---

## How to Use

### Clone the repository

First, clone the repository to your local machine and navigate to the directory.

```shell
    git clone git@github.com:morgancollens/python-url-shortener.git

    cd python-url-shortener
```

### Create your environment variables

Create a `.env` file in your project, using the variables in `.env.example` as a guide.

```text
DB_HOST=
DB_USER=
DB_PASSWORD=
DB_SCHEMA=

# Docker Compose
MYSQL_ROOT_PASSWORD=
```

### Setup your Database

Run the following script to setup a local MySQL database on your machine, using `docker-compose` and the credentials you've created in your `.env` file. **Note**: It's easiest in this case to set up a database
on your local machine, and using the user of `root`, with the same `DB_PASSWORD` and `MYSQL_ROOT_PASSWORD`.

```shell
    docker-compose up
```

The following script can then be run to create the database table used by the application.

```shell
    python3 scripts.py create-db
```

### Setup your virtual environment

Next you will need to set up the virtual environment for the project, to ensure that application specific configurations and packages are separate
from your global python workspace

Create the environment first...

```shell
    pip3 -m venv environment
```

Then activate the virtual environment...

```shell
    # On Unix
    source environment/bin/activate

    # On Windows
    environment/Scripts/activate
```

### Install dependencies

```shell
    pip3 install -r requirements.txt
```

### Start the application

```shell
    python3 scripts.py start
```

You should now be able to access the application from `http://localhost:5000`.