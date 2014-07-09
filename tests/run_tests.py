#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Hack to allow us to run tests before installing.
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..')))

from unittest import main

from test_core import *
from test_lazy import *


if __name__ == '__main__':
    main()
