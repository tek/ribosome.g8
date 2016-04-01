import tryp.logging
from trypnv.logging import trypnv_logger

from tryp.lazy import lazy


log = $name$_root_logger = trypnv_logger('$name$')


def $name$_logger(name: str):
    return $name$_root_logger.getChild(name)


class Logging(tryp.logging.Logging):

    @lazy
    def _log(self) -> tryp.logging.Logger:
        return $name$_logger(self.__class__.__name__)

__all__ = ('$name$_logger', 'Logging')
