#!/usr/bin/python3
"""
11. Add a new state
Adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    session.add(State(name='Louisiana'))
    state = session.query(State).filter_by(name='Louisiana').first()
    session.commit()
    print(str(state.id))
    session.close()
