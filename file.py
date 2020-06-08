import logging
from logging import Logger, Handler, Filter
from logging.config import fileConfig, dictConfig

filename = tempfile.mktemp() # Noncompliant
tmp_file = open(filename, "w+")
