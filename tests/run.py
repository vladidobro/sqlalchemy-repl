import sqlalchemy as sa
from sqlrepl import sqlrepl

def run_sqlite_memory():
    engine = sa.create_engine('sqlite://')
    sqlrepl(engine)

if __name__ == '__main__':
    run_sqlite_memory()
