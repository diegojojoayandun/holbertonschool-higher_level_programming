#!/usr/bin/python3
"""
14. Cities in state
prints all City objects
from the database hbtn_0e_14_usa
"""

if __name__ == "__main__":

    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    _query = session.query(State, City).filter(City.state_id == State.id)\
                                       .order_by(City.id).all()

    for state, city in _query:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
