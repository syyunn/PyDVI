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

import pylab as pl

#####################################################################################################

from PyDVI.Font import *
from PyDVI.FontManager import *

#####################################################################################################

font_manager = FontManager(font_map='pdftex')

# Pk Font

cmr10_pk = font_manager._load_font(font_types.Pk, 'cmr10')

cmr10_pk.print_summary()

glyph = cmr10_pk[ord('x')]

glyph.print_summary()
glyph.print_glyph()

glyph_bitmap = glyph.get_glyph_bitmap()

# pl.imshow(glyph_bitmap)
# pl.show()

# Type1 Font

print

#font_manager.set_use_pk(False)
font_manager.use_pk = True

cmr10_type1 = font_manager['cmr10']

cmr10_type1.print_summary()
#cmr10_type1.print_glyph_table()

cmr10_type1.tfm[ord('A')].print_summary()

#####################################################################################################
#
# End
#
#####################################################################################################
