from setuptools import setup, find_packages

setup(
    name='rrltdb',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'alembic',
        'pymysql']
)
