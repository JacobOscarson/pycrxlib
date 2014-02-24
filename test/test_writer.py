import os
import zipfile

from crx.writer import zipdir

here = os.path.abspath(os.path.dirname(__file__))

def test_zipdir():
    data = zipdir(os.path.join(here, 'dirfix'))
    with open('zipout.zip', 'w') as fp:
        fp.write(data)

    zipfile.ZipFile('zipout.zip', 'r') # just don't raise

