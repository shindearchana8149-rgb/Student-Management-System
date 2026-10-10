import sqlite3

db = sqlite3.connect("students.db")
db.execute("""CREATE TABLE IF NOT EXISTS students(
 id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
 age INTEGER, course TEXT, marks REAL)""")

def add():
    db.execute("INSERT INTO students(name,age,course,marks) VALUES(?,?,?,?)",
               (input("Name: "), int(input("Age: ")), input("Course: "), float(input("Marks: "))))
    db.commit()

def list_students():
    for s in db.execute("SELECT * FROM students"):
        print(s)

def main():
    while True:
        print("\n1 Add  2 List  3 Delete  4 Exit")
        c=input("> ")
        if c=="1": add()
        elif c=="2": list_students()
        elif c=="3":
            db.execute("DELETE FROM students WHERE id=?", (int(input("ID: ")),)); db.commit()
        elif c=="4": break

if __name__=="__main__": main()
