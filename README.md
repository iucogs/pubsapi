seppubs
=======

This script parses the iucogs/pubs database to find collections corresponding to
entries in the SEP and then produces a JSON data structure with the following
format:

    { 'id' : ###,                       # Citation ID
      'sep_dirs' : ['', ... ],          # SEP Dirs for collections
      'possible_matches' : [###, ...],  # Possible duplicates
      'data' : { ... },                 # Citation information
      'checked' : bool                  # Human verified?
    }

This will then be used by the HTRC-DID team for citation analysis.
