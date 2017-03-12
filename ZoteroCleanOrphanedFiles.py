#!/usr/bin/python

import sqlite3
import os

# Update this to match your data directory
zoterostorage = "/home/user/zotero"
zoterostoragefiles = zoterostorage +  "/storage"
dbh = sqlite3.connect(zoterostorage + "/zotero.sqlite")

# Query all attachments
c = dbh.cursor()

c.execute("SELECT key FROM items")

# Fetching all dirs as a set  
files = set(os.listdir(zoterostoragefiles))

for key in c.fetchall():
    if key[0] in files:
        files.remove(key[0])

# Loop over the non-existing files
print("\n".join(files))
