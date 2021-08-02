import config
import os


class ConfigPathError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"The config path is not correct: {self.msg}"


def find_config(path):
    file = "iunctus.cfg"
    if path is None:
        pass
    elif os.path.isdir(path):
        file = os.path.join(path, file)
    elif os.path.isfile(path):
        file = path
    else:
        raise ConfigPathError(f"path {path} is neither a file nor a directory.")

    try:
        config = configparser.read(file)
    except FileNotFoundException:
        raise ConfigPathError(
            f"file {file} does not exist, did you first create a project?"
        )


class IunctusProject(object):

    DEFAULT_CONFIG = {"PROJECT_FILES": {"..": ".."}}

    def __init__(self, config):
        self.config = config

    def __str__(self):
        return " "

    def clean(self):
        pass
