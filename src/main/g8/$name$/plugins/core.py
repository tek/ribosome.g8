from trypnv.machine import message, may_handle

from $name$.state import $name_camel$Component, $name_camel$Transitions

StageI = message('StageI')


class Plugin($name_camel$Component):

    class Transitions($name_camel$Transitions):

        @may_handle(StageI)
        def stage_i(self):
            pass

__all__ = ('Plugin', 'StageI')
