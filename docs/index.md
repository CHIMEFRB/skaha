# Skaha

!!! note ""

    A lightweight python interface to the CANFAR Science Platform.

??? Tip "Support for Private Container Images on Harbor"

    Starting October 2024, to create a session with a private container image from the [CANFAR Harbor Registry](https://images.canfar.net/), you will need to provide your harbor `username` and the `CLI Secret` through a `ContainerRegistry` object. 

    ```python
    from skaha.models import ContainerRegistry
    from skaha.session import Session

    registry = ContainerRegistry(username="username", password="sUp3rS3cr3t")
    session = Session(registry=registry)
    ```

!!! example "Example"

    ```python
    from skaha.session import Session

    session = Session()
    session_id = session.create(
        name="test",
        image="images.canfar.net/skaha/base-notebook:latest",
        cores=2,
        ram=8,
        gpu=1,
        kind="headless",
        cmd="env",
        env={"KEY": "VALUE"},
        replicas=3,
    )
    ```

[Get Started :material-coffee:](get-started.md){: .md-button .md-button--primary } 
[Go to GitHub :fontawesome-brands-github:](https://github.com/chimefrb/skaha){: .md-button .md-button--primary }
[Changelog :material-vector-polyline-remove:](changelog.md){: .md-button .md-button--primary }