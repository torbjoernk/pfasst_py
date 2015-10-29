# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""
import logging
import logging.config

DEFAULT_LOG_CONFIG = {
    'version': 1,
    'formatters': {
        'verbose': {
            'style': '{',
            'format': '{asctime:s} [{levelname:<8s}] {name:<25s} - {message:s}',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'style': '{',
            'format': '{asctime:s} [{levelname:<.1s}] {message:s}',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'simple',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'level': 'DEBUG',
            'formatter': 'verbose',
            'class': 'logging.FileHandler',
            'filename': 'pfasst_py.log'
        }
    },
    'loggers': {
        'pfasst_py': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False,
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    }
}

logging.config.dictConfig(DEFAULT_LOG_CONFIG)
