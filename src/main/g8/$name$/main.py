from toolz.itertoolz import cons

from tryp import List

from trypnv import NvimFacade

from $name$.env import Env
from $name$.state import $name_camel$State


class $name_camel$($name_camel$State):

    def __init__(self, vim: NvimFacade, plugins: List[str],) -> None:
        core = '$name$.plugins.core'
        $name_camel$State.__init__(self, vim, plugins.cons(core))

    def init(self):
        return Env(  # type: ignore
        )

__all__ = ('$name_camel$',)
