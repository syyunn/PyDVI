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
# - 10/12/2011 fabrice
#   - singleton ?
#   - font plugin ?
#   - font cache
#
#####################################################################################################

""" This module provides a Font Manager for the DVI Machine.

Each time a font is loaded, the Font Manager attributes to it an incremental identification number
that corresponds to the font index in the DVI Machine.

The different type of fonts (Packed, Type 1, etc.) are handled by a subclass of
:class:`PyDVI.Font.Font` that provide a kind of plugin mechanism.  In order to manage the mapping
between the TeX font name and the Type 1 font name, the Font Manager constructor takes a Font Map
name as parameter.

To create a Font Manager instance using the "pdftex" Font Map do::

  font_manager = FontManager('pdftex')

Then to load for example the font "cmr10" and get the font class instance do::

  font = font_manager["cmr10"]

Latter the same piece of codes could be use to retrieve the font class instance.

To get the number of fonts in the Font Manager use the :func:`len` function::

  len(font_manager)

"""

#####################################################################################################

__all__ = ['FontManager']

#####################################################################################################

import subprocess

#!# import ft2

#####################################################################################################

from PyDVI.FontMap import FontMap
from PyDVI.Kpathsea import kpsewhich
from PyDVI.Tools.FuncTools import get_filename_extension
from PyDVI.Tools.Logging import print_card

from PyDVI.Font import font_types, sort_font_class
from PyDVI.PkFont import PkFont
#!# from PyDVI.Type1Font import Type1Font

#####################################################################################################

class FontManager(object):

    """ This class implements a Font Manager for the DVI Machine.
    """

    font_classes = sort_font_class(PkFont,
                                   # Type1Font,
                                   )

    ###############################################

    def __init__(self, font_map, use_pk=False):

        """ The Font Map name is provided by *font_map*.
        """

        self.use_pk = use_pk

        self.fonts = {}
        self.last_font_id = 0

        self._init_font_map(font_map)

    ###############################################

    def _init_font_map(self, font_map):

        """ Load the font map.
        """

        font_map_file = kpsewhich(font_map, file_format='map')
        if font_map_file is not None:
            self.font_map = FontMap(font_map_file)
        else:
            raise NameError("Font Map %s not found" % (font_map)) 

    ###############################################

    def __contains__(self, font_name):

        """ Return :obj:`True` if the Font Manager holds the font *font_name*. """

        return self.fonts.has_key(font_name)

    ###############################################

    def __getitem__(self, font_name):

        """ Return the font *font_name* instance.  If the font is not in the Font Manager then load
        it.
        """

        if font_name in self:
            font = self.fonts[tex_font_name]
        else:
            if self.use_pk:
                font = self._load_font(font_types.Pk, font_name)
            else:
                font = self.fonts[font_name] = self.load_mapped_font(font_name)

        return font

    ###############################################

    def _get_new_font_id(self):

        """ Return a new font id.
        """

        self.last_font_id += 1

        return self.last_font_id

    ###############################################

    def _load_font(self, font_type, font_name):

        """ Load the font *font_name* with the font type *font_type* plugin.
        """

        font_class = self.font_classes[font_type]
        return font_class(self, self._get_new_font_id(), font_name)

#   ###############################################
#
#   def get_font_class_by_filename(self, filename):
#
#       extension = get_filename_extension(filename)
#       if extension is not None:
#               
#           for font_class in self.font_classes:
#               if font_class.extension == extension:
#                   return font_class
#
#       return None

    ###############################################

#   def load_mapped_font(self, tex_font_name):
#
#       if self.font_map is not None:
#
#           print "Font Manager load mapped font %s" % (tex_font_name)
#
#           font_map_entry = self.font_map[tex_font_name]
#
#           if font_map_entry is not None:
#
#               font_map_entry.print_summary()
#
#               font_class = self.get_font_class_by_filename(font_map_entry.pfb_filename)
#
#               if font_class is not None:
#                   return font_class(self, self.get_new_font_id(), font_map_entry.pfb_filename)
#               else:
#                   raise NameError("Unknown font class for font %s mapped to %s"
#                                   % (tex_font_name,
#                                      font_map_entry.pfb_filename))
#           
#           else:
#               return self.load_font(font_types.Pk, tex_font_name)

#####################################################################################################
#
# End
#
#####################################################################################################
