# Skaha Usage Examples

## Session API

The bread and butter of Skaha is the Session API. This API allows you to create, destroy, and get information about your sessions on the Skaha platform.

### Creating a Session

```python title="Create a session"
from skaha.session import Session

session = Session()
session_id = session.create(
    name="test",
    image="images.canfar.net/chimefrb/testing:keep",
    cores=2,
    ram=8,
    kind="headless",
    cmd="env",
    env={"TEST": "test"},
    replicas=3,
)
```

This will create three headless containers, each with 2 cores and 8GB of RAM, and run the command `env` in each container. The environment variable `TEST` will be set to `test` in each container.
The response will be a list of session IDs created.

```python
print(session_id)
["mrjdtbn9", "ov6doae7", "ayv4553m"]
```

### Getting Session Information

```python title="Get session information"
session.info(session_id)
```

``` { .python .annotate }
[{'id': 'mrjdtbn9',
  'userid': 'shinybrar',
  'image': 'images.canfar.net/chimefrb/testing:keep',
  'type': 'headless',
  'status': 'Succeeded',
  'name': 'test',
  'startTime': '2022-12-15T18:59:12Z',
  'connectURL': 'not-applicable',
  'requestedRAM': '8G',
  'requestedCPUCores': '2',
  'requestedGPUCores': '<none>',
  'coresInUse': '<none>',
  'ramInUse': '<none>'},
  ...
 {'id': 'ayv4553m',
  'userid': 'shinybrar',
  'image': 'images.canfar.net/chimefrb/testing:keep',
  'type': 'headless',
  'status': 'Succeeded',
  'name': 'test',
  'startTime': '2022-12-15T18:59:13Z',
  'connectURL': 'not-applicable',
  'requestedRAM': '8G',
  'requestedCPUCores': '2',
  'requestedGPUCores': '<none>',
  'coresInUse': '<none>',
  'ramInUse': '<none>'}]
```

### Getting Session Logs

To get the logs of a session, you can use the `logs` method. The response will be a dictionary with the session IDs as keys and the logs as values.
The logs are plain text format and can be printed to the console.

```python title="Get session logs"
session.logs(session_id)
```

### Destroying a Session

When you are done with your session, you can destroy it using the `destroy` method.
The response will be a dictionary with the session IDs as keys and a boolean value indicating whether the session was destroyed or not.

```python title="Destroy a session"
session.destroy(session_id)
```

```python
{"mrjdtbn9": True, "ov6doae7": True, "ayv4553m": True}
```

## Image API

The Image API allows you to get information about the images available on the Skaha platform. Nominally, 

### Getting Image Information

```python title="Get image information"
from skaha.images import Images

images = Images()
images.fetch()
```

But most of the time, you are only interested in images of a particular type. For example, if you want to get all the images that are available for headless sessions, you can do the following:

```python title="Get headless image information"
images.fetch(kind="headless")
```

```python
[
    "images.canfar.net/chimefrb/testing:keep",
    "images.canfar.net/lsst/lsst_v19_0_0:0.1",
    "images.canfar.net/skaha/lensfit:22.11",
    "images.canfar.net/skaha/lensfit:22.10",
    "images.canfar.net/skaha/lensingsim:22.07",
    "images.canfar.net/skaha/phosim:5.6.11",
    "images.canfar.net/skaha/terminal:1.1.2",
    "images.canfar.net/skaha/terminal:1.1.1",
    "images.canfar.net/uvickbos/pycharm:0.1",
    "images.canfar.net/uvickbos/swarp:0.1",
    "images.canfar.net/uvickbos/isis:2.2",
    "images.canfar.net/uvickbos/find_moving:0.1",
]
```

## Context API

Context API allows the user to get information about the resources available on the Skaha platform.

### Getting Reosources Information

```python title="Get context information"
from skaha.context import Context

context = Context()
context.resources()
```

```python
{
    "defaultCores": 2,
    "defaultCoresHeadless": 1,
    "availableCores": [1, 2, 4, 8, 16],
    "defaultRAM": 16,
    "defaultRAMHeadless": 4,
    "availableRAM": [1, 2, 4, 8, 16, 32, 64, 128, 192],
    "availableGPUs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...],
}
```
