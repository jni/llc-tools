from setuptools import setup

descr = """LLC tools: prettier LowLevelCallables with SciPy and Numba."""

DISTNAME            = 'llc'
DESCRIPTION         = 'Prettier LowLevelCallables'
LONG_DESCRIPTION    = descr
MAINTAINER          = 'Juan Nunez-Iglesias'
MAINTAINER_EMAIL    = 'juan.n@unimelb.edu.au'
URL                 = 'https://github.com/jni/llc-tools'
LICENSE             = 'BSD 3-clause'
DOWNLOAD_URL        = 'https://github.com/jni/llc-tools'
VERSION             = '0.2.0'
PYTHON_VERSION      = (3, 6)
INST_DEPENDENCIES   = []


if __name__ == '__main__':

    setup(name=DISTNAME,
        version=VERSION,
        url=URL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        license=LICENSE,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Topic :: Scientific/Engineering',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Operating System :: Unix',
            'Operating System :: MacOS',
        ],
        packages=['llc'],
        package_data={},
        install_requires=INST_DEPENDENCIES,
    )

