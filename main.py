import mysql.connector

conn = mysql.connector.connect(
	host="localhost",
	user="root",
	password="mysql"
)

cursor = conn.cursor()

try:
	cursor.execute("CREATE DATABASE password_manager")
	cursor.execute("USE password_manager")
	cursor.execute("CREATE TABLE manager (platform VARCHAR(255), password VARCHAR(255))")
	print("Manager created, you're good to go")
except:
	print("Welcome back!")

conn.close()

def add_platform(platform, password):
	conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="password_manager"
    )

	cursor = conn.cursor()
	command = 'INSERT INTO manager (platform, password) VALUES (%s, %s);'
	val = (platform, password)
	cursor.execute(command, val)
	conn.commit()
	conn.close()
	print("\n\n"*20)


def get_password(platform):
	conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="password_manager"
    )
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM manager WHERE platform='"+platform+"'")
	result = cursor.fetchall()
	print("\n\n"+ str(result) +"\n\n")
	conn.close()


def main():
	while True:
		print("*"*30)
		print("\tCommands")
		print("q = Exit")
		print("get <platform> (Ex.: get youtube) = Get password from x platform")
		print("add <platform> <password> (Ex.: add youtube 123456) [DO NOT USE SPACES ON PLATFORM NAME] = Add new password to manager")
		print("*"*30)

		op = input("\n\n->")

		x = op.split()

		if(x[0] == "q"):
			exit()
		elif(x[0] == "get"):
			get_password(x[1])
		elif(x[0] == "add"):
			add_platform(x[1], x[2])


if __name__ == '__main__':
	main()
