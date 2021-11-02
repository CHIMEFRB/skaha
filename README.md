# skaha
Python Client for Skaha Container Platform in CANFAR

## Installation

```
pip install skaha
```

## Basic Usage

```
from skaha.session import Session

session = Session()
session.create(name="<name>", image="<image>")
```
