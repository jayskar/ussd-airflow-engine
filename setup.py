from setuptools import setup, find_packages
from ussd import VERSION


setup(
    name='ussd_airflow',
    version=VERSION,
    packages=find_packages(exclude=('ussd_airflow',)),
    url='https://github.com/mwaaas/ussd_airflow',
    install_requires=[
        'Django>=2.2,<4.2',
        'djangorestframework>=3.10,<4.0',
        'structlog<22.3.0',
        'jinja2<3.1.2',
        'PyYAML>=5.1,<6.0',
        'PyStaticConfiguration==0.11.1',
        'requests<2.28.2',
        'PyConfigure==0.5.9',
        
    ],
    extras_require={
        'test': [
            'pytest-django>=3.5,<4.5.2',
            'freezegun',
            'psycopg2-binary',
            'pytest-cov>=2.7,<4.0.0',
        ],
        'docs': [
            'sphinx>=2.2,<6.1.3',
            'sphinx-autobuild>=0.7,<2021.3.14',
            'sphinx_rtd_theme>=0.4,<1.2.0',
        ]
    },
    include_package_data=True,
    license='MIT',
    author='Mwas',
    author_email='mwasgize@gmail.com',
    description='Ussd Airflow Library'
)
