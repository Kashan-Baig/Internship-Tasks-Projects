import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aps362005",         
    database="gradebook"      
)

cursor = conn.cursor()
print("✅ Connected successfully!")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    math INT default 0,
    science INT default 0,
    eng INT default 0
)
""")


while True:
    print("Enter your choice: \n1.Add Students\n2.View Students and their grades\n3.Average grades\n4.Students Ranking\n5.Exit")
    choice = int(input())
    if choice ==1:
        name = input("Enter your name: \n")
        age = input("Enter your age: \n")
    
        try:
            math = int(input("Enter your math grade (0–100): \n"))
            science = int(input("Enter your science grade (0–100): \n"))
            eng = int(input("Enter your English grade (0–100): \n"))

            if 0 <= math <= 100 and 0 <= science <= 100 and 0 <= eng <= 100:
                sql = "INSERT INTO students (name, age, math, science, eng) VALUES (%s, %s, %s, %s, %s)"
                values = (name, age, math, science, eng)
                cursor.execute(sql, values)
                conn.commit()
                print("✅ Student added successfully!")
            else:
                print("❌ Error: Grades must be between 0 and 100.")

        except ValueError:
            print("❌ Error: Please enter valid numbers for grades.")
    elif choice ==2:
        cursor.execute("SELECT * FROM students")
        results = cursor.fetchall()
        print("\n📋 Student Records:")
        for row in results:
            id, name, age, math, science, eng, percentage = row 
            print("ID: ", id,"  Name:", name,"  Age:", age)
            print("Math Grade:", math,"  Science Grade:", science,"  English Grade:", eng,"\n")
    elif choice==3:
        cursor.execute("SELECT * FROM students")
        results = cursor.fetchall()
        print("\n📋 Student Grade Averages Per Subject:")
        avgm=0 
        avge=0
        avgs=0
        count=0
        for row in results:
            id, name, age, math, science, eng, percenatge = row  
            avgm +=math 
            avgs +=science
            avge +=eng
            count+=1
        try:
            print("Maths = ",round(avgm/count,2),"\nScience = ",round(avgs/count,2), "\nEnglish = ",round(avge/count,2),"\n")
        except ZeroDivisionError:
            print("❌ Error: Cannot divide by zero.")
    elif choice==4:
        cursor.execute("SELECT * FROM students")
        results = cursor.fetchall()
        for row in results:
            id, name, age, math, science, eng, percentage = row 
            percentage = (math+science+eng)/3
            sql = "UPDATE students SET percentage = %s WHERE id = %s"
            values = (percentage, id)
            cursor.execute(sql, values)
            conn.commit()
        cursor.execute("SELECT * FROM students ORDER BY percentage DESC")
        sorted_results = cursor.fetchall()
        print("\n📊 Students sorted by percentage:\n")
        for row in sorted_results:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Percentage: {round(row[6], 2)}%")
    elif choice ==5:
        print("Thankyou !!!")
        break
    
    else:
        print("Enter you choice agian!!")


cursor.close()
conn.close()
