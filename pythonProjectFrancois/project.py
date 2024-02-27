import mysql.connector
from mysql.connector import Error

def connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='test',
      )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f'erreur lors de la connexion: {e}')
        return None


def createLanguage (name,creation,level):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO language (name,creation,level) VALUES (%s,%s,%s)"
            cursor.execute(query, (name,creation,level))
            conn.commit()
            print(f"Language '{name}'added")
        except Error as e:
            print(f"Error {e}")
        finally:
            cursor.close()
            conn.close()


def deleteLanguage (user_id):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM language WHERE id = %s"
            cursor.execute(query, (user_id,))
            conn.commit()
            print(f"Language '{user_id}' deleted")
        except Error as e:
            print(f"Error {e}")
        finally:
            cursor.close()
            conn.close()

def updateLanguage (id,name,creation,level):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            if name != None and creation != None and level != None:
                query = "UPDATE language SET name = %s, creation = %s, level =%s WHERE Id = %s"
                cursor.execute(query, (name,creation,level))
                conn.commit()
                print(f"Language '{name}' edited")
            if name == None and creation != None and level == None:
                query = "UPDATE language SET creation = %s WHERE Id = %s"
                cursor.execute(query, (creation))
                conn.commit()
                print(f"Language '{name}' edited")
            if name != None and creation == None and level == None:
                query = "UPDATE language SET name = %s WHERE Id = %s"
                cursor.execute(query, (name))
                conn.commit()
                print(f"Language '{name}' edited")
            if name == None and creation == None and level != None:
                query = "UPDATE language SET creation = %s, level =%s WHERE Id = %s"
                cursor.execute(query, (level))
                conn.commit()
                print(f"Language '{name}' edited")
            if name == None and creation != None and level != None:
                query = "UPDATE language SET creation = %s, level =%s WHERE Id = %s"
                cursor.execute(query, (creation,level))
                conn.commit()
                print(f"Language '{name}' edited")
            if name != None and creation == None and level != None:
                query = "UPDATE language SET name = %s, level =%s WHERE Id = %s"
                cursor.execute(query, (name,level))
                conn.commit()
                print(f"Language '{name}' edited")
            if name != None and creation != None and level == None:
                query = "UPDATE language SET name = %s, creation = %s WHERE Id = %s"
                cursor.execute(query, (name,creation))
                conn.commit()
                print(f"Language '{name}' edited")

        except Error as e:
            print(f"Error {e}")
        finally:
            cursor.close()
            conn.close()

def listLanguage ():
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT name,creation,level FROM language")
            return cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()


def verifyUser(name):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM users WHERE name = %s", (name,))
            user = cursor.fetchone()
            if user:
                return True
            else:
                return False
        except Error as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()


def logging(message):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO logs (message) VALUES (%s)"
            cursor.execute(query, (message,))
            conn.commit()
            print("Log entry added")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()


def option():
    name = input("Enter your username: ")
    if not verifyUser(name):
        print("access denied.")
        return

    while True:
        data = listLanguage()
        if data is not None:
            for (name, creation, level) in data:
                print(f"name: {name}, creation: {creation}, level: {level}")
        else:
            print("no data available")

        choice = input(" |0| quit\n |1| create\n |2| delete \n |3| update\n:")
        choice = int(choice)
        if choice == 0:
            quit()
        elif choice == 1:
            name = input("name: ")
            creation = input("date of creation (YYYY-MM-DD format): ")
            level = input("language level: ")
            createLanguage(name, creation, level)
            logging(f"{verifyUser(name)} Option 1 ")

        elif choice == 2:
            user_id = input("DELETE by ID: ")
            deleteLanguage(user_id)
            logging(f"{verifyUser(name)} Option 2")

        elif choice == 3:
            user_id = input("ENEW ID to update: ")
            name = input("NEW name (press enter to skip): ")
            creation = input("NEW creation (press enter to skip): ")
            level = input("NEW level (press enter to skip): ")
            updateLanguage(user_id, name, creation, level)
            logging(f"{verifyUser(name)} Option 3")
option()




#Ajout de 2 tables en plus: table users(id,user) table logs(id,message(user, action, which table)
