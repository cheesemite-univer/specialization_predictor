from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine, select
from sqlalchemy.orm import registry, Session, relationship
from predictor.common import entities

def get_db(path):
    engine = create_engine(f'sqlite:///{path}.db', echo=False)

    return engine


def create_tables(db):
    mapper_registry = registry()

    metadata = MetaData()

    pupils_table = Table('pupil', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('fullname', String)
    )
    grades_table = Table('grades', metadata,
        Column('id', Integer, primary_key=True),
        Column('student_id', Integer, ForeignKey("pupil.id")),
        # subjects
        Column('math', Integer),
        Column('physics', Integer),
        Column('biology', Integer),
        Column('chemistry', Integer),
        Column('economics', Integer),
        Column('history', Integer),
        Column('english', Integer),
        Column('art', Integer)
    )
    mapper_registry.map_imperatively(entities.Pupil, pupils_table,  properties={
        'grades' : relationship(entities.Grades, backref='pupil', order_by=grades_table.c.id)
    })
    mapper_registry.map_imperatively(entities.Grades, grades_table)


    specialities_table = Table('speciality', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', Integer)
    )
    wages_table = Table('wages', metadata,
        Column('id', Integer, primary_key=True),
        Column('speciality_id', Integer, ForeignKey("speciality.id")),
        # subjects
        Column('math', Integer),
        Column('physics', Integer),
        Column('biology', Integer),
        Column('chemistry', Integer),
        Column('economics', Integer),
        Column('history', Integer),
        Column('english', Integer),
        Column('art', Integer)
    )
    mapper_registry.map_imperatively(entities.Speciality, specialities_table, properties={
        'wages' : relationship(entities.Wages, backref="speciality", uselist=False)
    })
    mapper_registry.map_imperatively(entities.Wages, wages_table)
    

    metadata.create_all(db)



def insert_data(engine):
    with Session(engine) as session, session.begin():
        session.add_all([
            entities.Speciality('Translator', wages=entities.Wages(
                math=0,
                physics=0,
                biology=0,
                chemistry=0,
                economics=0,
                history=15,
                english=20,
                art=15
            )),
            entities.Speciality('Architect', wages=entities.Wages(
                math=13,
                physics=15,
                biology=8,
                chemistry=4,
                economics=4,
                history=13,
                english=6,
                art=16
            )),
            entities.Speciality('Engineer', wages=entities.Wages(
                math=20,
                physics=20,
                biology=5,
                chemistry=10,
                economics=5,
                history=5,
                english=5,
                art=16
            )),
            entities.Speciality('Medic', wages=entities.Wages(
                math=10,
                physics=10,
                biology=10,
                chemistry=12,
                economics=13,
                history=14,
                english=15,
                art=16
            )),
            entities.Speciality('Economist', wages=entities.Wages(
                math=10,
                physics=10,
                biology=10,
                chemistry=12,
                economics=13,
                history=14,
                english=15,
                art=16
            )),
            entities.Speciality('Lawyer', wages=entities.Wages(
                math=0,
                physics=0,
                biology=0,
                chemistry=0,
                economics=10,
                history=15,
                english=15,
                art=10
            )),
            entities.Speciality('Politics', wages=entities.Wages(
                math=0,
                physics=0,
                biology=0,
                chemistry=0,
                economics=15,
                history=20,
                english=15,
                art=10
            )),
            entities.Speciality('Actor', wages=entities.Wages(
                math=0,
                physics=0,
                biology=0,
                chemistry=0,
                economics=0,
                history=15,
                english=15,
                art=20
            )),
        ])
        
        session.commit()

    