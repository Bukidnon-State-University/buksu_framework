from setuptools import setup, find_packages

setup(
    name='buksu_framework',
    version='0.1.1',
    packages=find_packages(exclude=['tests']),
    package_data={'buksu_framework': ['py.typed']},
    install_requires=[
        'requests>=2.25.1,<3.0.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.2.3,<7.0.0',
            'pytest-mock>=3.5.1,<4.0.0',
        ],
    },
    author='Kid Mediante',
    author_email='kram@buksu.edu.ph',
    description='A framework for BukSU API integration',
    long_description='Provides a comprehensive set of tools and services for interacting with BukSU APIs, including authentication, user management, notifications, and media handling.',
    url='https://github.com/buksu/buksu_framework',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)