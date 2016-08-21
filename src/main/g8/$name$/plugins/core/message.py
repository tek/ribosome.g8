from ribosome.machine import message

StageI = message('StageI')
Echo = message('Echo', 'text')

__all__ = ('StageI', 'Echo')
