import amino.logging
from ribosome.logging import ribosome_logger

from amino.lazy import lazy


log = $name$_root_logger = ribosome_logger('$name$')


def $name$_logger(name: str):
    return $name$_root_logger.getChild(name)


class Logging(amino.logging.Logging):

    @lazy
    def _log(self) -> amino.logging.Logger:
        return $name$_logger(self.__class__.__name__)

__all__ = ('$name$_logger', 'Logging')
