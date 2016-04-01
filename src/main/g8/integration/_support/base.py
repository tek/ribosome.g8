import os
from pathlib import Path

from fn import _

from tryp.test import fixture_path, temp_dir

from tryp import List, Map, Just, Maybe
from trypnv.test import IntegrationSpec as TrypnvIntegrationSpec
from trypnv.test import VimIntegrationSpec as TrypnvVimIntegrationSpec
from trypnv import NvimFacade

from $name$.logging import Logging
from $name$.test import Spec


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


class IntegrationSpec(TrypnvIntegrationSpec, IntegrationCommon):
    pass


class VimIntegrationSpec(TrypnvVimIntegrationSpec, IntegrationCommon, Logging):

    def setup(self):
        super().setup()
        self.vim.cmd_sync('$name_camel$Start')
        self.vim.cmd('$name_camel$PostStartup')
        self._pvar_becomes('started', True)

    def _nvim_facade(self, vim):
        return NvimFacade(vim, '$name$')

    def _pre_start_neovim(self):
        self._setup_plugin()

    def _post_start_neovim(self):
        self._set_vars()

    def _set_vars(self):
        pass

    def _setup_plugin(self):
        self._rplugin_path = fixture_path(
            'nvim_plugin', 'rplugin', 'python3', '$name$_nvim.py')
        self._handlers = [
            {
                'sync': 1,
                'name': '$name_camel$Start',
                'type': 'command',
                'opts': {'nargs': 0}
            },
            {
                'sync': 0,
                'name': '$name_camel$PostStartup',
                'type': 'command',
                'opts': {'nargs': 0}
            },
        ]

    @property
    def _plugins(self):
        return List()

    def _pre_start(self):
        pass

__all__ = ('IntegrationSpec', 'VimIntegrationSpec')
