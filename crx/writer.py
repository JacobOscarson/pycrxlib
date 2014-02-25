import os
import io
import zipfile

import M2Crypto

def zipdir(path):
    def dozip(path, fp):
        for root, dirs, files in os.walk(path):
            for file in files:
                fp.write(os.path.join(root, file))

    with io.BytesIO() as stream:
        zfp = zipfile.ZipFile(stream, 'w', zipfile.ZIP_DEFLATED)
        dozip(path, zfp)
        zfp.close()
        return stream.getvalue()

def sign(data, pem):
    pkey = M2Crypto.EVP.load_key_string(pem)
    pkey.sign_init()
    pkey.sign_update(data)
    buf = M2Crypto.BIO.MemoryBuffer()
    pkey.save_key_bio(buf, cipher=None)
    return (buf.getvalue(), pkey.sign_final())
