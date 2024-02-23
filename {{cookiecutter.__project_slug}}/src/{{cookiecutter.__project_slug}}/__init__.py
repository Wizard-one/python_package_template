""" 
{{cookiecutter.description}}
"""
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("{{cookiecutter.__project_slug}}")
except PackageNotFoundError:
    # package is not installed
    pass