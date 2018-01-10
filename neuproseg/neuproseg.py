#                                                            _
# neuproseg ds app
#
# (c) 2016 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import os

# import the Chris app superclass
from chrisapp.base import ChrisApp



class Neuproseg(ChrisApp):
    """
    This application applies a trained model to MRI data of prostrates and outputs a segmented volume..
    """
    AUTHORS         = 'FNNDSC (dev@babyMRI.org)'
    SELFPATH        = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC        = os.path.basename(__file__)
    EXECSHELL       = 'python3'
    TITLE           = 'Neural Network Prostrate Segmenter'
    CATEGORY        = 'NN'
    TYPE            = 'ds'
    DESCRIPTION     = 'This application applies a trained model to MRI data of prostrates and outputs a segmented volume.'
    DOCUMENTATION   = 'http://github.com/FNNDSC/pl-neuproseg/wiki'
    VERSION         = '0.1'
    LICENSE         = 'Opensource (MIT)'

    # Fill out this with key-value output descriptive info (such as an output file path
    # relative to the output dir) that you want to save to the output meta file when
    # called with the --saveoutputmeta flag
    OUTPUT_META_DICT = {}
 
    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        """

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """


# ENTRYPOINT
if __name__ == "__main__":
    app = Neuproseg()
    app.launch()
