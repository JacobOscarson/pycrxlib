import os
import zipfile

from crx.writer import zipdir, sign

here = os.path.abspath(os.path.dirname(__file__))

def test_zipdir():
    data = zipdir(os.path.join(here, 'dirfix'))
    with open('zipout.zip', 'w') as fp:
        fp.write(data)

    zipfile.ZipFile('zipout.zip', 'r') # just don't raise

# This is a dummy private key. It doesn't go anywhere. (..and, should
# be obvious but, for your own sake DO NOT USE IT FOR ANYTHING!!).
goes_nowhere_pem = open('test/goes_nowhere.pkey').read()

def test_sign():
    sign('some data', goes_nowhere_pem) # also, don't raise
