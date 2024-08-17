from database import (
    migrate,
    Config,
    Student,
    Group,
    Human,
    Course,
)
from sqlalchemy import select

migrate()


def init_data():
    iryna, leonid = (
        Human(
            name="Iryna",
            age=17,
        ),
        Human(
            name="Leonid",
            age=15,
        ),
    )

    people = [
        iryna,
        leonid,
    ]
    py_1y_27, py_1y_23_03 = (
        Group(name="1y_27", subject=""),
        Group(name="1y_23_03", subject=""),
    )
    groups = [
        py_1y_27,
        py_1y_23_03,
    ]
    python, frontend, minecraft = (
        Course(name="Python"),
        Course(name="Frontend"),
        Course(name="Minecraft"),
    )
    courses = [
        python,
        frontend,
        minecraft,
    ]

    students = [
        Student(
            course=python,
            human=iryna,
            group=py_1y_27,
        ),
        Student(
            course=python,
            human=leonid,
            group=py_1y_23_03,
        ),
    ]
    with Config.SESSION.begin() as session:
        session.add_all(students)

    with Config.SESSION.begin() as session:
        # query = select(Course.name, Group.name, Human.name).where(Human.age > 15)
        query = (
            select(
                Course,
            )
            .join(Student)
            .join(Human)
            .where(Human.age > 16)
        )
        print(
            [
                [student.human.name for student in course.students]
                for course in session.scalars(query).all()
            ]
        )
        # print(
        #     [
        #         f"{student.course.name}_{student.group.name} ==> {student.human.name}"
        #         for student in session.scalars(query).all()
        #     ]
        # )


init_data()
