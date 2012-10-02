"""
Script to dump SEP publications for Katy's group.
"""
import json

from seppubs.model import *
import seppubs.lib

citations = dict()

for c in session.query(Citation).all():
    sep_entries = [col.collection_name.strip('SEP ')
        for col in c.collections if col.owner == 'sep']
    citations[c.citation_id] = { 'sep_entries' : sep_entries,
        'possible_matches' : [match.citation_id 
            for match in c.possible_matches],
        'record' : c.json,
        'cleaned' : (c.entryTime != c.last_modified)
        }

print seppubs.lib.json(citations)
