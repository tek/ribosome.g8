from ribosome.machine import may_handle

from $name$.state import $name_camel$Component, $name_camel$Transitions
from $name$.plugins.core.message import StageI, Echo


class CoreTransitions($name_camel$Transitions):

    @may_handle(StageI)
    def stage_i(self):
        pass

    @may_handle(Echo)
    def echo(self):
        self.log.info(self.msg.text)


class Plugin($name_camel$Component):

    Transitions = CoreTransitions

__all__ = ('Plugin', 'StageI')
