from sqlalchemy import create_engine, MetaData, Table, text
from prettytable import PrettyTable

DATABASE_URL = "postgresql+psycopg2://postgres:1234@localhost/healthreport"

#a connection to the database
engine = create_engine(DATABASE_URL)
metadata = MetaData()
connection = engine.connect()

#to show query results in tables
def print_pretty_table(results, headers):
    table = PrettyTable(headers)
    for row in results:
        table.add_row(row)
    print(table)

print("Basic Retrieval Queries")
query1 = text("""
    SELECT disease_code, description AS "disease"
    FROM Disease
    WHERE pathogen = 'Bacteria' AND disease_code IN (
        SELECT disease_code
        FROM Discover
        WHERE first_enc_date < '2020-01-01'
    )
""")
result1 = connection.execute(query1).fetchall()
print("List all diseases caused by 'bacteria' that were discovered before 2020.")
print_pretty_table(result1, ["Disease Code", "Description"])

query2 = text("""
    SELECT D.name, D.surname, Doc.degree
    FROM Users D
    JOIN Doctor Doc ON D.email = Doc.email
    WHERE D.email NOT IN (
        SELECT email
        FROM Specialize
        WHERE id = (
            SELECT id FROM DiseaseType WHERE description = 'infectious diseases'
        )
    )
""")
result2 = connection.execute(query2).fetchall()
print("Retrieve the names and degrees of doctors who are not specialized in “infectious diseases.")
print_pretty_table(result2, ["Name", "Surname", "Degree"])

query3 = text("""
    SELECT D.name, D.surname, Doc.degree
    FROM Users D
    JOIN Doctor Doc ON D.email = Doc.email
    WHERE D.email IN (
        SELECT email
        FROM Specialize
        GROUP BY email
        HAVING COUNT(id) > 2
    )
""")
result3 = connection.execute(query3).fetchall()
print("List the name, surname and degree of doctors who are specialized in more than 2 disease types.")
print_pretty_table(result3, ["Name", "Surname", "Degree"])


print("Complex Queries with Aggregation")
query4 = text("""
    SELECT U.cname, AVG(U.salary)
    FROM users U
    JOIN Doctor D ON U.email = D.email
    JOIN Specialize S ON D.email = S.email
    JOIN DiseaseType DT ON S.id = DT.id
    WHERE DT.description = 'Virology'
    GROUP BY U.cname;
""")
result4 = connection.execute(query4).fetchall()
print("List countries and the average salary of doctors specialized in 'virology.'")
print_pretty_table(result4, ["Country", "Average Salary"])

query5 = text("""
    SELECT P.department, COUNT(DISTINCT P.email)
    FROM PublicServant P
    JOIN Record R ON P.email = R.email
    JOIN Disease D ON R.disease_code = D.disease_code
    WHERE D.description = 'COVID-19'
    GROUP BY P.department
    HAVING COUNT(DISTINCT R.cname) > 1;
""")
result5 = connection.execute(query5).fetchall()
print("Find departments with public servants reporting 'covid-19' cases across multiple countries, counting such employees per department.")
print_pretty_table(result5, ["Department", "Employee Count"])

print("Update and Maintenance Queries")
query6_before = text("""
    SELECT U.email, U.salary
    FROM Users U
    JOIN PublicServant PS ON U.email = PS.email
    WHERE U.email IN (
        SELECT email
        FROM Record R
        JOIN Disease D ON R.disease_code = D.disease_code
        WHERE D.description = 'COVID-19'
        GROUP BY email
        HAVING SUM(R.total_patients) > 3
    );
""")
result6 = connection.execute(query6_before).fetchall()
print("BEFORE: Public Servant Salaries")
print_pretty_table(result6, ["Email", "Salary"])

query6 = text("""
    UPDATE Users
    SET salary = salary * 2
    WHERE email IN (
        SELECT P.email
        FROM PublicServant P
        JOIN Record R ON P.email = R.email
        JOIN Disease D ON R.disease_code = D.disease_code
        WHERE D.description = 'COVID-19'
        GROUP BY P.email
        HAVING SUM(R.total_patients) > 3
);
""")
result6 = connection.execute(query6)

query6_after = text("""
    SELECT U.email, U.salary
    FROM Users U
    JOIN PublicServant PS ON U.email = PS.email
    WHERE U.email IN (
        SELECT email
        FROM Record R
        JOIN Disease D ON R.disease_code = D.disease_code
        WHERE D.description = 'COVID-19'
        GROUP BY email
        HAVING SUM(R.total_patients) > 3
    );
""")
result6 = connection.execute(query6_after).fetchall()
print("AFTER: Public Servant Salaries")
print_pretty_table(result6, ["Email", "Salary"])


query7_before = text("""
    SELECT name
    FROM Users
""")
result7 = connection.execute(query7_before).fetchall()
print("BEFORE: Users with 'bek' and 'gul'")
print_pretty_table(result7, ["Name"])

query7 = text("""
    DELETE FROM Users
    WHERE name LIKE '%bek%' OR name LIKE '%gul%';
""")
result7 = connection.execute(query7)

query7_after = text("""
    SELECT U.name
    FROM Users U
""")
result7 = connection.execute(query7_after).fetchall()
print("AFTER: Users with 'bek' and 'gul'")
print_pretty_table(result7, ["Name"])

print("Indexing")
"""
ALTER TABLE Users
ADD PRIMARY KEY (email);
"""
query8 = text("""
    CREATE UNIQUE INDEX idx_email 
    ON Users (email);
""")
result8 = connection.execute(query8)

query9 = text("""
    CREATE INDEX idx_disease_code 
    ON Disease (disease_code);
""")
result9 = connection.execute(query9)

query_results = text("""
    SELECT indexname, indexdef
    FROM pg_indexes
    WHERE tablename = 'users' OR tablename = 'disease';
""")
result10 = connection.execute(query_results).fetchall()
print_pretty_table(result10, ["Index Name", "Definition"])

print("Additional Analysis")
query11 = text("""
    SELECT cname, SUM(total_patients) AS total
    FROM Record
    GROUP BY cname
    ORDER BY total DESC
    LIMIT 2;
""")
result11 = connection.execute(query11).fetchall()
print("List the top 2 countries with the highest number of total patients recorded.")
print_pretty_table(result11, ["Country", "Total Patients"])

print("Query with a Derived Attribute")
query12 = text("""
    SELECT SUM(R.total_patients)
    FROM PatientDisease P
    JOIN Record R ON P.disease_code = R.disease_code
    JOIN Disease D ON P.disease_code = D.disease_code
    WHERE D.description = 'COVID-19';
""")
result12 = connection.execute(query12).fetchall()
print("Calculate the total number of patients who have covid-19 disease.")
print_pretty_table(result12, ["Total Patients"])

print("View Operation")
query13 = text("""
    CREATE VIEW PatientView AS
    SELECT U.name, U.surname, D.description
    FROM Users U
    JOIN Patients P ON U.email = P.email
    JOIN PatientDisease PD ON P.email = PD.email
    JOIN Disease D ON PD.disease_code = D.disease_code;
""")
result13 = connection.execute(query13)

print("Querying the View just created")
query14 = text("""
    SELECT *
    FROM PatientView;
""")
result14 = connection.execute(query14).fetchall()
print("Retrieve a list of all patients’ full names along with the diseases they have been diagnosed with.")
print_pretty_table(result14, ["Patient Name", "Patient Surname", "Disease"])