#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:07:54 2021

@author: yannicklehr
"""
from pathlib import Path

from time import sleep
import random

import os
from os import listdir
from os.path import isfile, join

filesForUpload = [f for f in listdir('readyForUpload/') if isfile(join('readyForUpload/', f)) and join('readyForUpload/', f).endswith('.mp4')]