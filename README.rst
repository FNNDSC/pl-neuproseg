################################
pl-neuproseg
################################


Abstract
********

This application applies a trained model to MRI data of prostrates and outputs a segmented volume. Note, this application has already been trained *a priori* and the purpose of this plugin is to deploy this trained model and perform a segmentation on existing *preprocessed* data.

The *preprocessing* of data is **out of scope** of this application, and the assumption is that input data has been properly preprocessed.

The original python code was developed by Anneke Meyer and adapted to a CHRIS plugin during NAMIC project week at MIT, Jan 8-12th, 2018.

Data
====

Input data is required to run this plugin and has been supplied as part of this repository in the ``data`` directory. This directory contains test sets as input to the trained model.


Deploy
******

This repository is associated with ``dockerhub`` and automated builds are enabled. Thus, to ``install`` this container, simply do

.. code-block:: bash

    docker pull fnndsc/pl-neuproseg

Alternatively, you can also build a local version of this container:

.. code-block:: bash

    docker build -t local/pl-neuproseg .

Run
***

Using a container
=================

Assuming you have pulled the ``fnndsc/pl-neuproseg`` container, and assuming the use of the ``data`` directory in this repository, 

.. code-block:: bash

    mkdir output
    chmod 777 output # So that the container can write results here!
    docker run -v ./data/ProstateX-0029:/incoming -v ./output:/outgoing   \
            fnndsc/pl-neuproseg neuproseg.py --multistream           \
            /incoming /outgoing

This will run the containerized segmenter on the passed input directory (on the host), writing output to the passed output directory.

The ``chmod 777 output`` is necessary to allow the container to store data in ``output`` -- in some cases, particularly in NFS mapped spaces (if ``output`` is on an NFS space) and if the NFS space is mounted as ``rootsquash``, then ``root`` on the local machine might not be able to write to a directory, pending its permissions.

Directly *on the metal*
=========================

To run directly, several dependencies have to be satisfied -- thus we recommend using the container. If, however, you wish to run *on the metal*, and assuming these dependencies have been met, do

.. code-block:: bash

    mkdir output
    python3 neuproseg/neuproseg.py --multistream ./data/ProstateX-0029 ./output

See below for the setup of the app *directly*.

Setup a python virtual environment
----------------------------------

To run the app directly, we recommend setting up a python virtual environment. On Ubuntu, you can do

.. code-block:: bash

    sudo apt install virtualenv virtualenvwrapper python3-tk

**NOTE: the ``python3-tk`` is critical and must be installed before creating the virtual environment.**

then, create a directory to contain all your python virual environments, e.g.

.. code-block:: bash

    cd ~
    mkdir python-venv
    cd python-venv
    virtualenv --python=python3.6 --system-site-packages pl_env

finally, run the following to use the virtual environment

.. code-block:: bash

   export WORKON_HOME=~/python-venv
   source /usr/share/virtualenvwrapper/virtualenvwrapper.sh    

we suggest adding the above to a file and then simply sourcing that file. Create the file once

.. code-block:: bash

   export WORKON_HOME=~/python-venv > ~/penv
   source /usr/share/virtualenvwrapper/virtualenvwrapper.sh  >> ~/penv 

and then simply for any subsequent use

.. code-block:: bash

    source ~/penv ; workon pl_env

Install dependencies
--------------------

In this virtual environment, install all the necessary dependencies

.. code-block:: bash

    pip3 install -r requirements.txt



Run in this environment

Using ``docker run``
====================

Assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``

.. code-block:: bash

    docker run -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing   \
            fnndsc/pl-neuproseg neuproseg.py            \
            /incoming /outgoing

This will ...

Make sure that the host ``$(pwd)/out`` directory is world writable!







