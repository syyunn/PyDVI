#####################################################################################################
#
# PyDVI - Python Library to Process DVI Stream
# Copyright (C) 2009 Salvaire Fabrice
#
#####################################################################################################

#####################################################################################################
#
# Audit
#
#
#####################################################################################################

#####################################################################################################

#####################################################################################################

from Font import Font
from VfFontParser import VfFontParser

#####################################################################################################

vf_font_parser = VfFontParser()

#####################################################################################################

class VfFont(Font):

    ###############################################

    def __init__(self, name):

        super(VfFont, self).__init__('vf', name)

#####################################################################################################
#
# End
#
#####################################################################################################