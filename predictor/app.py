from predictor.initializers import db
from predictor.common import entities
from sqlalchemy import select
from sqlalchemy.orm import Session, relationship


def run():
    engine = db.get_db('school')
    db.create_tables(engine)
    db.insert_data(engine)
    
    user_input = input('Enter grades for the lessons:\
            math, physics, biology,\n \
            chemistry, economics, history, english, art')
    grades = list(map(int, user_input.split(',')))


    sps = {}
    with Session(engine) as session, session.begin():
        specialities = session.execute(
            select(entities.Speciality)).scalars().all()
        
        for speciality in specialities: 
            wages = speciality.wages
            sps[speciality.name] = grades[0] * wages.math \
                + grades[1] * wages.physics \
                + grades[2] * wages.biology \
                + grades[3] * wages.chemistry \
                + grades[4] * wages.economics \
                + grades[5] * wages.history \
                + grades[6] * wages.english \
                + grades[7] * wages.art

    for item in sorted(sps.items(), key=lambda item: item[1], reverse=True):
        print(f'{item[0]} -- {item[1]}')
