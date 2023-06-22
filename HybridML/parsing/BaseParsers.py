# DeprecationWarning: 
# Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3
# and in 3.10 it will stop working
import sys

if sys.version_info[1] < 3:
    from collections import Sequence
else:
    from collections.abc import Sequence

import numpy as np


class Parser:
    """Base implementation of a parser.
    Parsers get a model-json file and create an abstract representation that can be put into a builder to actually."""

    def parse(self, data):
        raise Exception("Not Implemented")


class NodeParser(Parser):
    """Base implementation of a node parser.
    Saves, which types of nodes it is able to parse."""

    def __init__(self, parses_types):
        super().__init__()
        self.net = None
        if isinstance(parses_types, (Sequence, np.ndarray)) and not isinstance(parses_types, str):
            self.parses_types = parses_types
        else:
            self.parses_types = [parses_types]

    def parse(self, data):
        raise NotImplementedError()
