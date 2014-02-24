import os
import io
import zipfile

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

