# -*- encoding: utf-8 -*-
"""
Fully Coded App by AppSeed.us
License: MIT
For more apps please access https://appseed.us/
Copyright (c) 2019 - present AppSeed.us
"""

import os
from app import app
from flask_frozen import Freezer

#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
    freezer = Freezer(app)
    freezer.freeze()
