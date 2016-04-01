from $name$.logging import Logging
from trypnv.data import Data
from trypnv.record import dfield


class Env(Data, Logging):
    initialized = dfield(False)
