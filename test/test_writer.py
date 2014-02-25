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
goes_nowhere_pem = """
-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQC/ZCStymwSw+HSdW9+PWS2wr4mxeMilelavryc08+tfTAM4ojd
sd9U3fvC/hUXcUjKDdEfIp3mr86nQp7U/2Lrvuenyp97N0LuRDxoYNu5GIF76I7s
vEj1QCsjcl4oqeI3g2nSogOTRK77djY+zoyOyApRXMti2UZwCkaBu7j+OwIDAQAB
AoGAEFGlnvvngyIYmy1QOF9buwmX1Q6Cc2x83TPuOSEGUDCgbDjUmrKT7FSRJusr
OTh7kF7lOdZlyEmtQS25BUhRUsqE1fWtKppVgCrxM2Ag9/Y93o5XWiueJ4ynjbuq
kGq62SoZETzX0P8zZci1smPdf/rm0rN3K2CSXPX3vdhtVgECQQD67vy3BBaLZHpB
C4AmSEHbVg8oCImE0lutsdj1eLBxOWetACMxDuLwEadLsd485Im8Z8iaSH3rXtZs
QaPgHZv7AkEAw0FlgoNf7gR0W9I+eoOzv2BY85BxX8NrcqEhStsFQ7AljhwzehHs
qiyVw7zcAf5WY9U4kyWsUSV34lbJsVBSwQJBAOJzoB5tkwbScz2V6l0h4kTVYjIn
misCR3f1wqyr8NcNDhHiyN9x5rztwYMfDkb3m5EqO6938iLh4DGr/v622dcCQDCt
1jPysvDxVV0rDn6W5TJaP/MBWPKqEtiySU2TSz2z5bkHWOIfI+TNVs1FAYjRsxIS
r5cn9k0IzVm1j3VQdEECQQC93Cfq+sOWRVGHBnB7EvQBro67bcqMEiANGSXzVkdo
XIq5ymkjKLtEtg0QvHYTirYOqcBzSSPexImIMkASuw7l
-----END RSA PRIVATE KEY-----"""

def test_sign():
    sign('some data', goes_nowhere_pem) # also, don't raise
