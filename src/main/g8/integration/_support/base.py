import os
from pathlib import Path

from fn import _

from amino.test import fixture_path, temp_dir

from amino import List, Map, Just, Maybe, Right
from ribosome import NvimFacade
from ribosome.test.integration.spec import (PluginIntegrationSpec,
                                            VimIntegrationSureHelpers)

from $name$.logging import Logging
from $name$.nvim_plugin import $name_camel$NvimPlugin


class IntegrationSpec(PluginIntegrationSpec, VimIntegrationSureHelpers):

    def _pre_start(self):
        super()._pre_start()
        self.vim.cmd_sync('$name_camel$Start')
        self.vim.cmd('$name_camel$PostStartup')
        self._pvar_becomes('started', True)

    @property
    def plugin_class(self):
        return Right($name_camel$NvimPlugin)

    @property
    def _prefix(self):
        return '$name$'

    def _post_start_neovim(self):
        super()._post_start_neovim()
        self._set_vars()

    def _set_vars(self):
        self.vim.vars.set_p('plugins', self._plugins)

    @property
    def _plugins(self):
        return List()

__all__ = ('IntegrationSpec', 'VimIntegrationSpec')
