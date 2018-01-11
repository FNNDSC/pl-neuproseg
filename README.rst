################################
pl-neuproseg
################################


Abstract
********

This application applies a trained model to MRI data of prostrates and outputs a segmented volume.

The original algorithm was developed by Anneke Meyer and adapted to a CHRIS plugin during NAMIC project week at MIT, Jan 8-12th, 2018.

Run
***

Data
====

Input data is required to run this plugin and has been supplied as part of this repository in the ``data`` directory. This directory contains test sets as input to the trained model.

Directly ``on the metal``
=========================

Setup a python virtual environment
----------------------------------

To run the app directly, we recommend setting up a python virtual environment. On Ubuntu, you can docker

.. code-block:: bash

sudo apt install virtualenv virtualenvwapper
echo "source /usr/share/virtualenvwrapper/virtualenvwrapper.sh" >> ~/.bashrc

then, create a directory to contain all your python virual environments, e.g.

.. code-block:: bash
cd ~
mkdir python-venv
cd python-venv
virtualenv --python=python3.6 --system-site-packages pl_en


Using ``docker run``
====================

Assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``

.. code-block:: bash

    docker run -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing   \
            fnndsc/pl-neuproseg neuproseg.py            \
            /incoming /outgoing

This will ...

Make sure that the host ``$(pwd)/out`` directory is world writable!







