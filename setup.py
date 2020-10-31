from setuptools import setup

setup(
    name='cat',
    packages=['cat'],
    include_package_data=True,
    install_requires=[
        'flask',
        'jinja2',
        'pyquery',
        'python',
        'requests', # needed by bin/check_site.py
    ],
    #setup_requires=[
    #    'pytest-runner',
    #],
    tests_require=[
        'pytest',
    ],
)

# vim: expandtab
