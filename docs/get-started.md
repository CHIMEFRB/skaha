# Get Started

### Installation (Quick Start)

!!! note ""

    Skaha requires Python 3.7 or higher.

!!! code ""

    ```bash
    pip install skaha
    ```

### Before you start

Before you can use skaha, you need to have a valid CANFAR account and have access to the Skaha Science Platform.
If you don't have a CANFAR account, you can register for one [here](https://canfar.net). Once you have a CANFAR account,
you can request access to the Skaha Science Platform from CANFAR Personel.

### Authentication

Skaha uses a X509 security certificate for interactions with the CANFAR Science Platform. You need to have a valid certificate
in order to use skaha.

#### Generating a certificate

When you install skaha, a command line tool called `cadc-get-cert` is also installed. This tool can be used to generate
a certificate for you. You can run the following command to generate a certificate:

```bash title="Generate a certificate"
cadc-get-cert -u <your-username>
Password: <your-password>

DONE. 10 day certificate saved in /home/<your-username>/.ssl/cadcproxy.pem
```

This will generate a certificate for you and store it in `~/.ssl/cadcproxy.pem`. 

By default, skaha will only look at the `$HOME/.ssl/cadcproxy.pem` location for your certificate. 
If you want to use a different location, you can pass the path to the certificate to any Skaha Object when you create it.

```python title="Using a different certificate location"
from skaha.session import Session

session = Session(certificate="/path/to/certificate.pem")
```

### Contributing

We use [poetry](https://python-poetry.org/) to manage our dependencies. To install poetry, run the following command:

```bash title="Install poetry"
pip install poetry>=1.2.2
```

Now you can get started to contribute to skaha:

```bash title="Clone the repository and run tests"
git clone https://github.com/chimefrb/skaha.git
cd skaha
poetry install
poetry run pytest
```

!!! Note "Note"
    To run tests, you need a valid CANFAR security certificate and access to the Skaha Science Platform.

#### Pre-commit

We have a configuration file for [pre-commit](https://pre-commit.com/) that will run a series of checks on your code before
you commit it. To install pre-commit, run the following command:

```bash title="Install pre-commit"
poetry run pre-commit install
```

### Licensing
This code is licensed under the [MIT License](https://en.wikipedia.org/wiki/MIT_License). See the [LICENSE](https://github.com/CHIMEFRB/skaha/blob/main/LICENSE) file for more information.