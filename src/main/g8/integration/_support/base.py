import os
from pathlib import Path

from fn import _

from amino.test import fixture_path, temp_dir

from amino import List, Map, Just, Maybe, Right
from ribosome import NvimFacade
from ribosome.test import PluginIntegrationSpec

from $name$.logging import Logging
from $name$.test import Spec
from $name$.nvim_plugin import $name_camel$NvimPlugin


class IntegrationCommon(Spec):

    def setup(self):
        self.cwd = Maybe.from_call(Path.cwd, exc=IOError)
        super().setup()

    def _cd_back(self):
        try:
            self.cwd.map(str).foreach(os.chdir)
        except Exception as e:
            self.log.error('error changing back to project root: {}'.format(e))

    def teardown(self):
        super().teardown()
        self._cd_back()


class IntegrationSpec(PluginIntegrationSpec, IntegrationCommon, Logging):

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
        self.vim.set_pvar('plugins', self._plugins)

    @property
    def _plugins(self):
        return List()

__all__ = ('IntegrationSpec', 'VimIntegrationSpec')
