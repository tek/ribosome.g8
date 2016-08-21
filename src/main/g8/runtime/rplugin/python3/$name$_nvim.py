import os

import neovim

from $name$.nvim_plugin import $name_camel$NvimPlugin

import amino
from amino.logging import amino_file_logging, VERBOSE

if '$name;format="upper"$_DEBUG' in os.environ:
    amino.development = True
    amino_file_logging(VERBOSE)


@neovim.plugin
class Plugin($name_camel$NvimPlugin):
    pass
