# -*- coding: UTF-8 -*-
"""
    4nd1Scrapers Module

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Addon Name: 4nd1Scrapers Module
# Addon id: script.module.4nd1scrapers


import os
import sys
import urllib
import urlparse

integer = 1000

# Modified `sleep` command that honors a user exit request
def sleep (time):
    while time > 0 and not xbmc.abortRequested:
        xbmc.sleep(min(100, time))
        time = time - 100



