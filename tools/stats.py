#!/usr/bin/env python2
import os, sys, re, datetime, time, argparse, ConfigParser
from collections import Counter

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'externals', 'selfspy')))
from selfspy import models

from Crypto.Cipher import Blowfish
import hashlib
import selfspy.config as cfg

PASSWORD = 'changeme'
DATABASE = os.path.expanduser('~/.selfspy/selfspy.sqlite')

models.ENCRYPTER = Blowfish.new(hashlib.md5(PASSWORD).digest())
session = models.initialize(DATABASE)()

def subseq(xs, l):
    for x in range(len(xs) - l):
        yield xs[x:x+l]

keys = session.query(models.Keys).order_by('created_at')
for key in keys:
        # key.id
        # key.started
        # key.created_at
        # key.started
        # key.process.name
        # key.window.title
        # key.nrkeys
    print(key.decrypt_text().decode('utf8'))
