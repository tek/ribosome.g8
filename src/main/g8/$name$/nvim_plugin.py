from pathlib import Path

import neovim

from amino import List

from ribosome import command, NvimStatePlugin, msg_command, json_msg_command

from $name$.plugins.core.message import StageI, Echo
from $name$.main import $name_camel$
from $name$.logging import Logging


class $name_camel$NvimPlugin(NvimStatePlugin, Logging):

    def __init__(self, vim: neovim.Nvim) -> None:
        super().__init__(vim)
        self.$name$ = None  # type: $name_camel$
        self._post_initialized = False

    @property
    def name(self):
        return '$name$'

    def state(self):
        return self.$name$

    @command()
    def $name$_reload(self):
        self.$name$_quit()
        self.$name$_start()
        self._post_startup()

    @command()
    def $name$_quit(self):
        if self.$name$ is not None:
            self.vim.clean()
            self.$name$.stop()
            self.$name$ = None

    @command(sync=True)
    def $name$_start(self):
        plugins = self.vim.pl('plugins') | List()
        self.$name$ = $name_camel$(self.vim.proxy, plugins)
        self.$name$.start()
        self.$name$.wait_for_running()
        self.$name$.send(StageI())

    @command()
    def $name$_post_startup(self):
        self._post_initialized = True
        if self.$name$ is not None:
            self.vim.set_pvar('started', True)
        else:
            self.log.error('$name$ startup failed')

    @msg_command(Echo)
    def $name$_echo(self):
        pass

__all__ = ('$name_camel$NvimPlugin',)
