import mysql.connector

class DBTasks:
  def __init__(self):
    self.mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="1977",
      database="taskify"
    )

  def getTasks(self, task_id):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM tasks WHERE task_id = " + str(task_id))
    myresult = mycursor.fetchall()
    return myresult
