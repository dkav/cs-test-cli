#!/usr/bin/python

"""Modified csrun.py for testing."""

import os
import sys


CS_PATH = "..\\cs.py\\circuitscape"
TST_PATH = (os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
sys.path.append(os.path.join(TST_PATH, CS_PATH))

from compute import Compute


def main(argv=None):
    """Run Circuitscape."""
    if argv is None and len(sys.argv) == 2:
        argv = sys.argv[1]

    if argv is None:
        print 'Error: Circuitscape configuration (.ini) file required.',sc,sc
    else:
        configFile = argv
        cs = Compute(configFile, 'Screen')
        cs.compute()


if __name__ == "__main__":
    main()
