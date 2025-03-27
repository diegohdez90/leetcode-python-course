import logging
log = logging.getLogger()

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

ch.setFormatter(formatter)

log.addHandler(ch)
log.setLevel(logging.NOTSET)

__all__ = [
    'log'
]