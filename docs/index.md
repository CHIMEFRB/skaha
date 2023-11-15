# Skaha

!!! note ""
    A lightweight pythonic interface to the CANFAR Science Platform.

!!! example "Example"

    ```python
    from skaha.session import Session

    session = Session()
    session_id = session.create(
        name="test",
        image="images.canfar.net/chimefrb/alpine:keep",
        cores=2,
        ram=8,
        gpu=1,
        kind="headless",
        cmd="env",
        env={"TEST": "test"},
        replicas=3,
    )
    ```

[Get Started :material-coffee:](get-started.md){: .md-button .md-button--primary } 
[Go to GitHub :fontawesome-brands-github:](https://github.com/chimefrb/skaha){: .md-button .md-button--primary }
[Changelog :material-vector-polyline-remove:](changelog.md){: .md-button .md-button--primary }