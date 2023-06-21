__all__ = (
    'log',
    )

import functools
import logging


@functools.lru_cache(maxsize=1)
def log() -> logging.Logger:
    f = logging.BASIC_FORMAT.split(':')
    f.insert(0, '%(asctime)s')
    logging.basicConfig(format=':'.join(f))
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    return log
