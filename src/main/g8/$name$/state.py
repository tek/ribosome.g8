from trypnv import Machine, PluginStateMachine, NvimFacade
from trypnv.nvim import HasNvim
from trypnv.machine import ModularMachine, Transitions

from $name$.logging import Logging

from tryp import List


class $name_camel$Component(ModularMachine, HasNvim, Logging):

    def __init__(self, name: str, vim: NvimFacade) -> None:
        Machine.__init__(self, name)
        HasNvim.__init__(self, vim)


class $name_camel$State(PluginStateMachine, HasNvim, Logging):

    def __init__(self, vim: NvimFacade, plugins: List[str]) -> None:
        HasNvim.__init__(self, vim)
        PluginStateMachine.__init__(self, '$name$', plugins)


class $name_camel$Transitions(Transitions, HasNvim):

    def __init__(self, machine, *a, **kw):
        Transitions.__init__(self, machine, *a, **kw)
        HasNvim.__init__(self, machine.vim)

__all__ = ('$name_camel$Component', '$name_camel$State', '$name_camel$Transitions')
