import sqlalchemy as sa

def run_sqlite_memory():
    from sqlrepl import sqlrepl
    engine = sa.create_engine('sqlite://')
    sqlrepl(engine)

if __name__ == '__main__':
    run_sqlite_memory()
