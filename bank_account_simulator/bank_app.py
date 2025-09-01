import mysql.connector

conn= mysql.connector.connect(
    host="localhost",
    username="root",
    password="******",
)

cursor=conn.cursor()

cursor.execute("create database if not exists bank_db")
cursor.execute("use bank_db")

cursor.execute("""
create table if not exists accounts(
    account_id int auto_increment primary key,
    name varchar(20),
    balance decimal(10,2)
)
""")

conn.commit()

class BankAccount:
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def create_account(self):
        cursor.execute("insert into accounts(name,balance) values(%s,%s)",(self.name,self.balance))
        conn.commit()
        account_id=cursor.lastrowid
        print(f"account created ID: {account_id} for {self.name} with balance {self.balance}")

    @staticmethod
    def deposit(account_id,amount):
        cursor.execute("update accounts set balance=balance+%s where account_id=%s",(amount,account_id))
        conn.commit()
        print(f"deposited {amount} into account {account_id}")
    
    @staticmethod
    def withdraw(account_id,amount):
        cursor.execute("select balance from accounts where account_id=%s",(account_id,))
        result=cursor.fetchone()
        if result:
            balance=float(result[0])
            if amount>balance:
                print("insufficient balance")
            else:
                cursor.execute("update accounts set balance=balance-%s where account_id=%s",(amount,account_id))
                conn.commit()
                print(f"withdrew {amount} from account {account_id}")
        else:
            print(f"account {account_id} not found")


    @staticmethod
    def check_balance(account_id):
        cursor.execute("select name,balance from accounts where account_id=%s",(account_id,))
        result=cursor.fetchone()
        if result:
            print(f"account holder: {result[0]} balance:{result[1]}")
        else:
            print(f"account {account_id} not found")

    @staticmethod
    def delete_account(account_id):
        cursor.execute("delete from accounts where account_id=%s",(account_id,))
        conn.commit()
        print(f"account {account_id} deleted successfully")

def menu():
    while True:
        print("\n--- Bank Account Simulator ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Delete Account")
        print("6. Exit")

        choice=input("enter your choice: ")

        if choice=="1":
            name=input("enter account holder name: ")
            balance=float(input("enter initial balance: "))
            acc=BankAccount(name,balance)
            acc.create_account()

        elif choice=="2":
            account_id=int(input("enter your account id: "))
            amount=float(input("enter deposit amount: "))
            BankAccount.deposit(account_id,amount)
        
        elif choice=="3":
            account_id=int(input("enter your account id: "))
            amount=float(input("enter withdrawn money: "))
            BankAccount.withdraw(account_id,amount)

        elif choice=="4":
            account_id=int(input("enter your account id: "))
            BankAccount.check_balance(account_id)

        elif choice=="5":
            account_id=int(input("enter your account id: "))
            BankAccount.delete_account(account_id)

        elif choice=="6":
            print("existing ...")
            break

        else:
            print("Invalid choice! try again")

menu()

cursor.close()
conn.close()


