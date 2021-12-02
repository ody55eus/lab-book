Usage
=====

To reproduce the results shown in the Lab Book, you need a running Python environment with Ana and spectrumanalyzer installed.


Install dependencies
--------------------

Linux
~~~~~

If you are running Debian or Ubuntu you can easily download and install docker with the following command:

.. code-block:: console

   $ apt install docker.io


Windows / OS X
~~~~~~~~~~~~~~

Users with different operating systmes should download and install docker directly from the docker homepage: <https://docs.docker.com/get-docker/>



Run Docker Image
~~~~~~~~~~~~~~~~

Run the docker container for **Jupyterlab** to start developing:

.. code-block:: console

   $ docker run -d -p 8888:8888 -e "PASSWORD=YourSecurePassword" \
                -e GIT_URL="http://gitlab.com/ody55eus/lab-book.git" \
                --name jupyterlab \
                registry.gitlab.com/ganymede/jupyterlab:latest


If you just want the Python environment to execute the tests, use the `ana` tag:

.. code-block:: console

   $ docker run -d -p 8888:8888 -e "PASSWORD=YourSecurePassword" \
                -e GIT_URL="http://gitlab.com/ody55eus/lab-book.git" \
                --name python \
                registry.gitlab.com/ganymede/jupyterlab:ana

and execute a bash terminal inside the container:

1. JupyterLab: go to http://localhost:8888/ and open a terminal.

2. Python environment: enter the environment in a bash:

.. code-block:: console

   $ docker exec -it jupyterlab bash

Use this bash terminal to install the dependencies for the software packages

.. code-block:: console

   $ cd spectrumanalyzer && python -m pip install -e . && cd ..
   $ cd ana && python -m pip install -e . && cd ..
   $ cd EVE python -m pip install -e . && cd ..
   $ python -m pip install coverage


Local installation
~~~~~~~~~~~~~~~~~~

Clone the repositories (change URLs accordingly) and install spectrumanalyzer and Ana using pip:

.. code-block:: console

   $ python -m pip install -e git+http://gitlab.com/ody55eus/spectrumanalyzer.git
   $ python -m pip install -e git+http://gitlab.com/ody55eus/ana.git
   $ python -m pip install coverage


Install and start a Jupyterlab server:

.. code-block:: console

   $ python -m pip install jupyterlab
   $ jupyterlab
    

Reproduce
---------

To reproduce the plots and run the code either run the JupyterLab server or execute the test files:

.. code-block:: console

    $ git clone ANA_URL
    $ python -m unittest discover -s ana/tests/basic
    $ python -m unittest discover -s ana/tests/ana/prepair
    $ python -m unittest discover -s ana/tests/ana/fit
    $ python -m unittest discover -s ana/tests/ana/visualize


Create the Lab Book
-------------------

To create the Lab Book use the following docker image

.. code-block:: console

   $ docker run -d  -e GIT_URL="http://gitlab.com/ody55eus/lab-book.git" \
                -p 8888:8888 -e "PASSWORD=YourSecurePassword" \
                --name python \
                registry.gitlab.com/ganymede/jupyterlab:ana

Run JupyterLab Server
---------------------

After starting the server you can open the Jupyter notebooks at http://localhost:8888

Run Tests
---------

**optionally run tests** to make sure the code is working:

.. code-block:: console

   $ coverage run -m pytest spectrumanalyzer
   $ coverage run -m unittest discover -s tests/basic

Afterwards **create the Lab Book** by executing

.. code-block:: console

   $ make html

Run Lab Book
------------

To run the Lab Book as static webserver download the `_build` directory and run the following line in the command line:

.. code-block:: console

   $ docker run -d -p 80:80 \
                --name nginx \
                -v /c/_build:/usr/share/nginx/html:ro \
                nginx

This will start a local webserver at http://localhost/ and mount the folder ``/c/_build`` (linux) or ``c:\_build`` (Windows) as root.
