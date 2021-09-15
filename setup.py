import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()
    
setuptools.setup(
    name = 'preprocessing_hoangct',
    version = '0.0.2',
    author  = 'Cao The Hoang',
    author_email = 'thehoang.cao@gmail.com',
    description = 'This is preprocessing package',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        ],
    python_requires = '>=3.5'
    )