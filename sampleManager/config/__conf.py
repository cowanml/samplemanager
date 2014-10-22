__author__ = 'arkilic'

import os.path
import ConfigParser
from os import path


config_path = [
            '/etc/sampleManager.conf',
            os.path.expanduser('~/sampleManager.conf'),
            'dataBroker.conf'
            ]


def check_config_file():
    result = False
    for f in config_path:
        if path.isfile(f):
            result = True
    return result


def __loadConfig():
    cf=ConfigParser.SafeConfigParser()
    if check_config_file():
        cf.read(config_path)
    else:
        raise IOError('sampleManager configuration file does not exist')
    return cf


conf_dict = __loadConfig()
