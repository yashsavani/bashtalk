from setuptools import setup, find_packages

setup(
    name='bashtalk',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'llm'
    ],
    entry_points={
        'console_scripts': [
            'bashtalk=bashtalk:main',
        ],
    },
)
