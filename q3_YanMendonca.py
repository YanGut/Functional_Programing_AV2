import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
)

myDbCursor = mydb.cursor()

def executeSQLComand(command, cursor):
    cursor.execute (command)
    return cursor.fetchall()

createDatabase = lambda dbName, cursor : executeSQLComand(f"CREATE DATABASE {dbName}", cursor)
useDatabase = lambda dbName, cursor : executeSQLComand(f"USE {dbName}", cursor)
dropDatabase = lambda dbName, cursor : executeSQLComand(f"DROP DATABASE {dbName}", cursor)

createTable = lambda table, atributes, cursor : executeSQLComand(f"CREATE TABLE {table} ({atributes})", cursor)
dropTable = lambda table, cursor : executeSQLComand(f"DROP TABLE {table}", cursor)

selectFromWhere = lambda atributes, table, condition, cursor : executeSQLComand(f"SELECT {atributes} FROM {table} WHERE {condition}", cursor)
insertInto = lambda table, atributes, values, cursor : executeSQLComand(f"INSERT INTO {table} ({atributes}) VALUES ({values})", cursor)
deleteFromWhere = lambda table, condition, cursor : executeSQLComand(f"DELETE FROM {table} WHERE {condition}", cursor)


createDatabase("funcional_db", myDbCursor)
useDatabase("funcional_db", myDbCursor)

createTable("USERS", "id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), country VARCHAR(255), id_console INT", myDbCursor)
createTable("VIDEOGAMES", "id_console INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), id_company INT, release_date DATE", myDbCursor)
createTable("GAMES", "id_game INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), genre VARCHAR(255), release_date DATE, id_console INT", myDbCursor)
createTable("COMPANY", "id_company INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), country VARCHAR(255)", myDbCursor)

insertInto("USERS", "name, country", "'Yan', 'Brazil'", myDbCursor)
insertInto("USERS", "name, country", "'Lucas', 'Brazil'", myDbCursor)
insertInto("VIDEOGAMES", "name, release_date", "'PS4', '2018-04-20'", myDbCursor)
insertInto("VIDEOGAMES", "name, release_date", "'XBOX', '2013-06-14'", myDbCursor)
insertInto("GAMES", "title, genre, release_date", "'God of War', 'Action', '2018-04-20'", myDbCursor)
insertInto("GAMES", "title, genre, release_date", "'Halo', 'Action', '2013-06-14'", myDbCursor)
insertInto("COMPANY", "name, country", "'Sony', 'Japan'", myDbCursor)
insertInto("COMPANY", "name, country", "'Microsoft', 'USA'", myDbCursor)

selectFromWhere("*", "USERS", "name = 'Yan'", myDbCursor)
selectFromWhere("*", "VIDEOGAMES", "true", myDbCursor)
selectFromWhere("*", "GAMES", "true", myDbCursor)
selectFromWhere("*", "COMPANY", "name = 'Sony'", myDbCursor)

deleteFromWhere("USERS", "name = 'Lucas'", myDbCursor)
deleteFromWhere("VIDEOGAMES", "name = 'XBOX'", myDbCursor)
deleteFromWhere("GAMES", "title = 'Halo'", myDbCursor)
deleteFromWhere("COMPANY", "name = 'Microsoft'", myDbCursor)

response = myDbCursor.fetchall()
printResult = lambda res: [print(row) for row in res]

printResult(f"{response}")

dropTable("USERS", myDbCursor)
dropTable("VIDEOGAMES", myDbCursor)
dropTable("GAMES", myDbCursor)
dropTable("COMPANY", myDbCursor)

dropDatabase("funcional_db", myDbCursor)

myDbCursor.close()
mydb.close()
