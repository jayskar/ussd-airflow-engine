from setuptools import setup, find_packages
from ussd import VERSION


setup(
    name='ussd_airflow',
    version=VERSION,
    packages=find_packages(exclude=('ussd_airflow',)),
    url='https://github.com/mwaaas/ussd_airflow',
    install_requires=[
        'Django>=2.2,<5.0.11',
        'djangorestframework>=3.10,<4.0',
        'structlog<21.2.0',
        'jinja2<2.12',
        'PyYAML>=5.1,<6.0.2',
        'PyStaticConfiguration==0.10.5',
        'requests<2.32.3',
        'PyConfigure==0.5.9',
    ],
    extras_require={
        'test': [
            'pytest-django>=3.5,<4.3',
            'freezegun',
            'psycopg2-binary',
            'pytest-cov>=2.7,<2.12',
        ],
        'docs': [
            'sphinx>=2.2,<3.6',
            'sphinx-autobuild>=0.7,<2020.10',
            'sphinx_rtd_theme>=0.4,<0.6',
        ]
    },
    include_package_data=True,
    license='MIT',
    author='Mwas',
    author_email='mwasgize@gmail.com',
    description='Ussd Airflow Library'
)
