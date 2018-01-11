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

To run the app directly, we recommend setting up a python virtual environment. On Ubuntu, you can do

.. code-block:: bash

    sudo apt install virtualenv virtualenvwrapper

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







