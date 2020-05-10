__version__ = '0.1.2'


def get_version():
    # Get package version string
    return __version__


def get_version_as_tuple():
    # Get package version as tuple
    return tuple(map(int, __version__.split('.')))