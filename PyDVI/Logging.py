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

__all__= ['print_card']

#####################################################################################################

def print_card(message, width = 80):

    line = '='*width

    print
    print line
    print message
    print line
    # print

#####################################################################################################
#
# End
#
#####################################################################################################
