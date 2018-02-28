from setuptools import setup

install_requires=[
    'furl',
    'requests',
    ]

tests_require = [
    'mock',
    'nose',
    'requests-mock',
    ]

setup(
        name = 'maury',
        version = '0.1.0',
        description = 'A experimental client for the Engine Yard API',
        license = 'MIT',
        packages = ['maury'],
        install_requires = install_requires,
        tests_require = tests_require,
        test_suite = "nose.collector",
        zip_safe = False)
