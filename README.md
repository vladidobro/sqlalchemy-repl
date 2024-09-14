sqlalchemy-repl
===============

REPL for SQLAlchemy and Python REPL.

Installation
------------
```
pip install sqlalchemy-repl
```

Basic usage
-----------
```
import sqlalchemy as sa
from sqlrepl import sqlrepl

engine = sa.create_engine('sqlite://')
repl = sqlrepl(engine)
```
