from toolz.itertoolz import cons

from amino import List

from ribosome import NvimFacade

from $name$.env import Env
from $name$.state import $name_camel$State


class $name_camel$($name_camel$State):

    def __init__(self, vim: NvimFacade, plugins: List[str],) -> None:
        core = '$name$.plugins.core'
        super().__init__(vim, plugins.cons(core))

    def init(self):
        return Env(  # type: ignore
        )

__all__ = ('$name_camel$',)
