
texto = """NumPy is the fundamental package for scientific computing with Python.
Website: https: // www.numpy.org
Documentation: https: // numpy.org/doc
Mailing list: https: // mail.python.org/mailman/listinfo/numpy-discussion
Source code: https: // github.com/numpy/numpy
Contributing: https: // www.numpy.org/devdocs/dev/index.html
Bug reports: https: // github.com/numpy/numpy/issues
Report a security vulnerability: https: // tidelift.com/docs/security
It provides:

a powerful N-dimensional array object
sophisticated(broadcasting) functions
tools for integrating C/C++ and Fortran code
useful linear algebra, Fourier transform, and random number capabilities """.split("\n")

for linea in texto:
    if "https" in linea:
        print(linea)