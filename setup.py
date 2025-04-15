from setuptools import setup, find_packages

setup(
    name='telescope',
    version='0.1.0',
    description='A unified interface for Language Model Clients',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Digital Galaxy',
    author_email='Vitalii.Kostenko@digitalgalaxy.com',
    url='https://github.com/digitalgalaxy/telescope',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'typing_extensions==4.12.2',
        'anthropic==0.49.0',
        'google-genai==1.9.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',
    keywords='llm ai language-models anthropic google',
)
