from sqlalchemy import orm
from flask.ext.sqlalchemy import SQLAlchemy, _SignallingSession

# This allows the use of new versioned session things from SQLAlchemy's
# history_meta example
def create_scoped_session(self, options=None):
    """Helper factory method that creates a scoped session."""
    if options is None:
        options = {}
    scopefunc = options.pop('scopefunc', None)
    db = self

    class SessionClass(_SignallingSession):

        def __init__(self, autocommit=False, autoflush=False):
            super(SessionClass, self).__init__(db, autocommit, autoflush,
                    **options)

    return orm.scoped_session(
        SessionClass, scopefunc=scopefunc
    )

SQLAlchemy.create_scoped_session = create_scoped_session