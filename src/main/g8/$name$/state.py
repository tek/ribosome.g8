from ribosome import Machine, RootMachine, NvimFacade
from ribosome.machine import ModularMachine, Transitions
from ribosome.nvim import HasNvim

from $name$.logging import Logging

from amino import List


class $name_camel$Component(ModularMachine, HasNvim, Logging):

    def __init__(self, vim: NvimFacade, parent=None) -> None:
        ModularMachine.__init__(self, parent=parent)
        HasNvim.__init__(self, vim)


class $name_camel$State(RootMachine):

    def __init__(self, vim: NvimFacade, plugins: List[str]) -> None:
        super().__init__(vim, plugins, title='$name$')


class $name_camel$Transitions(Transitions, HasNvim):

    def __init__(self, machine, *a, **kw):
        Transitions.__init__(self, machine, *a, **kw)
        HasNvim.__init__(self, machine.vim)

__all__ = ('$name_camel$Component', '$name_camel$State', '$name_camel$Transitions')
