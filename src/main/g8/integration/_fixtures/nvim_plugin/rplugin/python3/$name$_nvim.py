import neovim
import os
import logging
from pathlib import Path

from $name$.nvim_plugin import $name_camel$NvimPlugin

import tryp

tryp.development = True

import tryp.logging

logfile = Path(os.environ['TRYPNV_LOG_FILE'])
tryp.logging.tryp_file_logging(level=logging.DEBUG,
                               handler_level=logging.DEBUG,
                               logfile=logfile)


@neovim.plugin
class Plugin($name_camel$NvimPlugin):
    pass
