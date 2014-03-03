pubsapi
=======

This script parses the iucogs/pubs database to find collections corresponding to
entries in the SEP and then produces a JSON data structure with the following
format:

    { id :                                  # Citation ID
        {
          'sep_dirs' : ['', ... ],          # SEP Dirs for collections
          'possible_matches' : [###, ...],  # Possible duplicates
          'data' : { ... },                 # Citation information
          'checked' : bool                  # Human verified?
        }
      ...
    }

This will then be used by the HTRC-DID team for citation analysis.

Installing the ORM
----------------------

    git clone git@github.com:iucogs/pubsapi.git
    cd pubsapi
    virtualenv pubsenv
    source pubsenv/bin/activate
    python setup.py develop

Configure pubs.ini from pubs.ini.template with the proper username and password.

Using the ORM:

```python
from pubs.model import *

first_collection = session.query(Collection).first()

for citation in first_collection.citations:
    print citation.title

```
