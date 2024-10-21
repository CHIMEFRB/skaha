# Get Started

## Installation (Quick Start)

!!! note ""

    Skaha requires Python 3.8+.

!!! code ""

    ```bash
    pip install skaha
    ```

## Before you Begin

Before you can use the Skaha python package, you need a valid CANFAR account and access to the Skaha Science Platform.
To create a new account, you can register [here](https://canfar.net).

### Authentication

Skaha uses a X509 security certificate for interactions with the CANFAR Science Platform.
You need to have a valid certificate in order to authenticate with the platform.

#### Generating a certificate

Installing the skaha package will also install a command line tool called `cadc-get-cert`.
This tool can be used to generate a certificate with the following command:

    ```bash
    cadc-get-cert -u <your-username>
    Password: <your-password>

    DONE. 10 day certificate saved in /home/<your-username>/.ssl/cadcproxy.pem
    ```

This will generate a certificate for you and store it in `~/.ssl/cadcproxy.pem`. 

By default, skaha looks at the location `$HOME/.ssl/cadcproxy.pem` for your certificate. 
Alternatively, you can specify the location of your certificate when creating a new session.

    ```python
    from skaha.session import Session

    session = Session(certificate="/path/to/certificate.pem")
    ```

### Container Registry Access

In order to access private container images from the CANFAR Harbor Registry, you need to provide your harbor `username` and the `CLI Secret` through a `ContainerRegistry` object.

    ```python
    from skaha.models import ContainerRegistry
    from skaha.session import Session

    registry = ContainerRegistry(username="username", password="sUp3rS3cr3t")
    session = Session(registry=registry)
    ```

Passing the `ContainerRegistry` object passes the base64 encoded `username:secret` to the Skaha server for authentication under the `X-Skaha-Registry-Auth` header.