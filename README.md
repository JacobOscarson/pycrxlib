# Pythonic .crx file generation

`pycrxlib` generates the `.crx` archives used to distribute extensions
to Google's webbrowser Chrome (see e.g. [here][crx]). It's a
programmatic API, i.e. it's intended to be used from Python based
build tools, e.g. [Fabric][fabric], [Ansible][ansible], [Paver][paver]
or possibly others.

[crx]: http://developer.chrome.com/extensions/crx
[fabric]: http://fabfile.org
[ansible]: http://ansible.com
[paver]: http://paver.github.io/paver/

This script is heavily based on
[crxmake-python](https://github.com/bellbind/crxmake-python) by
[@bellbind](https://github.com/bellbind), but intended to be
integrated in a Python toolchain in a bit more conventional way,
e.g. installable via PyPI and easier to integrate (there's also a
slightly different method of getting M2Crypto to generate a DER public
key).

`pycrxlib` needs [M2Crypto][m2] to run (which in it's turn must have
[Swig][swig] installed on the target system).

[m2]: https://github.com/martinpaljak/M2Crypto
[swig]: http://www.swig.org/

### Usage

If you never have packed your extension before, the easiest way is to
pack manually one time to get your private key (described
[here](http://developer.chrome.com/extensions/packaging)). After that
you have a private key (`xxx.pem` file).

You use `pycrxlib` by calling a simple entry point, `crx.write`. It
takes 3 parameters, the path to the extension you want to pack, the
desired archive name and your extensions private key.

An example of a simple hypothetical Fabric file can be seen
[here](fabfile.py), but the gist of it is that you simply import the
library:

    >>> import crx

and then call the function with your parameters:

    >>> crx.write('my-extension-dir', 'my-extension.crx', pemfile='my-pem-file.pem')

you can use the named parameter `pem` to pass in the private key as a
string instead of a path name (but remember to think about where you
put that private key, m'kay?).
