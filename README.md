# Skaha

Python Client for Skaha Container Platform in CANFAR

## Installation

The recommended way to install skaha is via pip:

```bash
pip install skaha
```

## Before you start

Before you can use skaha, you need to have a valid CANFAR account and have access to the Skaha Science Platform.
If you don't have a CANFAR account, you can register for one [here](https://canfar.net).

## Basic Usage

```python
from skaha.session import Session

session = Session()

# Create a session
session_id = session.create(
    name="some-name", image="images.canfar.net/chimefrb/alpine:keep", cmd="ls -l"
)

# Get logs
session.logs(id)

# Destroy session
session.destroy(id)
```
