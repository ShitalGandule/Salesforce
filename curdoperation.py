import mysql.connector

try:
    # Connect to MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",   # replace with your password
        database="college"          # replace with your database name
    )

    print("✅ Connection Successful!")

    # Create cursor
    mycursor = mydb.cursor()

    # Test query
    mycursor.execute("SHOW TABLES")

    print("Tables in database:")
    for table in mycursor:
        print(table)

except mysql.connector.Error as err:
    print("❌ Error:", err)

finally:
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("Connection Closed.")