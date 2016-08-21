from integration._support.base import IntegrationSpec

from amino.test import later


class EchoSpec(IntegrationSpec):

    def echo(self):
        text = 'test successful'
        self.vim.cmd('$name_camel$Echo {}'.format(text))
        later(lambda: self._log_out.contains(text))

__all__ = ('EchoSpec',)
