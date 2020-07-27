import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="websocketbridge", # Replace with your own username
    version="1.0.0",
    author="Ben Hack",
    author_email="benjamin.hack@balliol.ox.ac.uk",
    description="A package for making a unix socket available on a websocket connection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Chinbob2515/python-socket-websocket-bridge",
    packages=setuptools.find_packages(),
    install_requires=[
        "simple_websocket_server",
        "simpleprotocol"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
