from setuptools import setup, find_packages

setup(
    name='tokenizer',
    version='0.1.0',
    description='A regex-based tokenizer for general-purpose text processing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Franco Malatacca',
    author_email='franco.malatacca@gmail.com',
    url='https://github.com/francomalatacca/tokenizer',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
