"""
Script to dump SEP publications for Katy's group.
"""
import json

from pubs.model import *
import pubs.lib

# create a placeholder for the JSON data
citations = dict()

# query for all citations
for c in session.query(Citation).all():
    # get the sep dirs from the sep collection names
    sep_entries = [col.collection_name.strip('SEP ')
        for col in c.collections if col.owner == 'sep']

    # build the individual records
    citations[c.citation_id] = { 'sep_dirs' : sep_entries,
        'possible_matches' : [match.citation_id 
            for match in c.possible_matches],
        'data' : c.json,
        'cleaned' : (c.entryTime != c.last_modified)
        }

# simply print to the console to allow flexibility for file piping
print pubs.lib.json(citations)
