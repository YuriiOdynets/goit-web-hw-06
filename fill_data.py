import sqlite3
from faker import Faker
import random
from datetime import datetime

faker = Faker()

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Insert groups
group_names = ['Group A', 'Group B', 'Group C']
for name in group_names:
    cursor.execute('INSERT INTO groups (name) VALUES (?)', (name,))

# Insert teachers
teacher_names = [faker.name() for _ in range(5)]
for name in teacher_names:
    cursor.execute('INSERT INTO teachers (name) VALUES (?)', (name,))

# Insert subjects
subject_names = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Literature', 'Art']
for name in subject_names:
    teacher_id = random.randint(1, 5)
    cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (name, teacher_id))

# Insert students
for _ in range(50):
    name = faker.name()
    group_id = random.randint(1, 3)
    cursor.execute('INSERT INTO students (name, group_id) VALUES (?, ?)', (name, group_id))

# Insert grades
for _ in range(1000):
    student_id = random.randint(1, 50)
    subject_id = random.randint(1, 8)
    grade = random.randint(1, 100)
    date = faker.date_between(start_date='-1y', end_date='today')
    cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)', (student_id, subject_id, grade, date))

conn.commit()
conn.close()