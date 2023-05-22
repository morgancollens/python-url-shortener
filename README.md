# Python URL Shortener

A simple project built using Python and Flask as a learning exercise. Designed to allow users to shorten a URL and then access
the original URL through the shortened version.

---

## How to Use

### Prerequisites

#### Setup your Database

First you'll need to create the table in your MySQL database which will be used to persist the original URLs

```mysql
CREATE TABLE tbl_shortened_urls(
    urlID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    hash VARCHAR(500) NOT NULL COMMENT "The hashed key appended to the shortened url",
    originalUrl TEXT NOT NULL COMMENT "The original URL that was shortened. Used for redirection when a user clicks the shortened version of the link",
    INDEX (hash)
);
```
---

### Clone the repository

First, clone the repository to your local machine

```shell
git clone git@github.com:morgancollens/python-url-shortener.git
```

### Setup your virtual environment

Next you will need to set up the virtual environment for the project, to ensure that application specific configurations and packages are separate
from your global python workspace

Create the environment first...

```shell
    pip3 -m venv ENV_DIR python-url-shortener
```

Then change directory to go to the projects root path

```shell
    cd python-url-shortener
```

Then activate the virtual environment...

```shell
    # On Unix
    source bin/activate

    # On Windows
    Scripts/activate
```

### Install dependencies

```shell
    pip3 install -r requirements.txt
```

### Start the application

```shell
    python3 app.py
```

You should now be able to access the application from `http://localhost:5000`.