import sqlite3

def execute_query(query):
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Query 1: Find the top 5 students with the highest average grade across all subjects
query_1 = '''
    SELECT students.name, AVG(grades.grade) as avg_grade
    FROM grades
    JOIN students ON grades.student_id = students.id
    GROUP BY students.id
    ORDER BY avg_grade DESC
    LIMIT 5
'''

# Query 2: Find the student with the highest average grade in a specific subject
subject_id = 1  # Example subject_id for the query
query_2 = f'''
    SELECT students.name, AVG(grades.grade) as avg_grade
    FROM grades
    JOIN students ON grades.student_id = students.id
    WHERE grades.subject_id = {subject_id}
    GROUP BY students.id
    ORDER BY avg_grade DESC
    LIMIT 1
'''

# Query 3: Find the average grade in groups for a specific subject
query_3 = f'''
    SELECT groups.name, AVG(grades.grade) as avg_grade
    FROM grades
    JOIN students ON grades.student_id = students.id
    JOIN groups ON students.group_id = groups.id
    WHERE grades.subject_id = {subject_id}
    GROUP BY groups.id
'''

# Query 4: Find the average grade across the entire grade table
query_4 = '''
    SELECT AVG(grades.grade) as avg_grade
    FROM grades
'''

# Query 5: Find which courses are taught by a specific teacher
teacher_id = 1  # Example teacher_id for the query
query_5 = f'''
    SELECT subjects.name
    FROM subjects
    WHERE subjects.teacher_id = {teacher_id}
'''

# Query 6: Find the list of students in a specific group
group_id = 1  # Example group_id for the query
query_6 = f'''
    SELECT students.name
    FROM students
    WHERE students.group_id = {group_id}
'''

# Query 7: Find the grades of students in a specific group for a specific subject
query_7 = f'''
    SELECT students.name, grades.grade
    FROM grades
    JOIN students ON grades.student_id = students.id
    WHERE students.group_id = {group_id} AND grades.subject_id = {subject_id}
'''

# Query 8: Find the average grade given by a specific teacher across their subjects
query_8 = f'''
    SELECT AVG(grades.grade) as avg_grade
    FROM grades
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE subjects.teacher_id = {teacher_id}
'''

# Query 9: Find the list of courses a specific student attends
student_id = 1  # Example student_id for the query
query_9 = f'''
    SELECT subjects.name
    FROM grades
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE grades.student_id = {student_id}
    GROUP BY subjects.id
'''

# Query 10: Find the list of courses taught by a specific teacher to a specific student
query_10 = f'''
    SELECT subjects.name
    FROM grades
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE grades.student_id = {student_id} AND subjects.teacher_id = {teacher_id}
    GROUP BY subjects.id
'''

# Execute and print results for each query
queries = [query_1, query_2, query_3, query_4, query_5, query_6, query_7, query_8, query_9, query_10]

for i, query in enumerate(queries, 1):
    print(f"Query {i} Results:")
    results = execute_query(query)
    for row in results:
        print(row)
    print("\n")


    queries = {
    1: query_1,
    2: query_2,
    3: query_3,
    4: query_4,
    5: query_5,
    6: query_6,
    7: query_7,
    8: query_8,
    9: query_9,
    10: query_10
}

for number, query in queries.items():
    with open(f'query_{number}.sql', 'w') as file:
        file.write(query)