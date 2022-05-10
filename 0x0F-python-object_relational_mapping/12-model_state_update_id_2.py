#!/usr/bin/python3
"""
12-model_state_update_id_2
changes the name of the State object where id=2 to New Mexico from a database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
    session.close()
