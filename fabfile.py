"""
Example of a Fabric task that uses pycrxlib.

This is just an example of how to use pycrxlib via Fabric.
"""
import fabric
from fabric.api import *

import crx

@task
def pack():
    "Pack our hypothetical Chrome extension"
    crx.write('my-extension-dir', 'my-extension.crx', pemfile='my-pem-file.pem')
