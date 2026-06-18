# TODO: This is ugly as hell. There should be some way to do this without
#       getting in some nasty dependency loop.
from .iom16 import IOM16
from .iom168 import IOM168
from .iom328 import IOM328
from .iotn48 import IOTn48
from .iotn88 import IOTn88
from .iox128a4u import IOX128A4U
from .iocan64 import IOCAN64
ALL_CHIPS = [
    IOM16,
    IOM168,
    IOM328,
    IOTn48,
    IOTn88,
    IOX128A4U,
    IOCAN64
]


