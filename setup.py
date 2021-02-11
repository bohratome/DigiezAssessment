from setuptools import setup

setup(
    name='MoncifApp',
    version='1.0',
    description='REST API implementation in flask framework',
    author='Moncif EL KASSIMI',
    packages=[
                'myapp',
                'myapp/models',
                'myapp/views',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-WTF',
        'requests',
        'flask-swagger',
    ]
)
