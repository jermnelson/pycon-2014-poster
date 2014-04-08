# -------------------------------------------------------------------------------
# Name:        pycon 2014 poster
# Purpose:     Web poster for the pycon 2014 conference in Montreal
#
# Author:      Jeremy Nelson
#
# Created:     2014-04-06
# Copyright:   (c) Jeremy Nelson, Colorado College 2014
# Licence:     GPLv2
#-------------------------------------------------------------------------------
__author__ = "Jeremy Nelson"
__license__ = "GPLv2"

from flask import Flask, render_template

poster = Flask('pycon-2014-poster')

@poster.route('/')
def default():
    return render_template('web.html')

if __name__.startswith('__main__'):
    poster.run(
        host='0.0.0.0',
        port=8005,
        debug=True)



