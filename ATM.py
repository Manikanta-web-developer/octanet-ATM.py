import time

print("Please insert your CARD")

print("------------------------------------------------")
print("------------------------------------------------")



time.sleep(5)

password = 7310

pin = int(input("Enter your ATM PIN : "))

print("------------------------------------------------")
print("------------------------------------------------")



balance = 1000

if pin==password:
    while True:
        print("""
             1 == balance
             2 == withdraw balance
             3 == deposit balance
             4 == exit
         """)

        print("------------------------------------------------")
        print("------------------------------------------------")

        try:
              
           option = int(input("Please enter your choice : "))

           print("------------------------------------------------")
           print("------------------------------------------------")


        except:
            
           print("Please enter valid option")

           print("------------------------------------------------")
           print("------------------------------------------------")



        if option == 1:
        
            print(f"your current balance is {balance}")

            print("------------------------------------------------")
            print("------------------------------------------------")



    
        if option == 2:
            
        
            withdraw_amount = int(input("Enter your Withdrawal amount : "))

            print("------------------------------------------------")
            print("------------------------------------------------")

            balance = balance-withdraw_amount

            print(f"{withdraw_amount} is debited from your account ")

            print("------------------------------------------------")
            print("------------------------------------------------")

            print(f"Your updated balance is {balance}")

            print("------------------------------------------------")
            print("------------------------------------------------")

        if option == 3:
        
            deposit_amount = int(input("Enter your Deposited amount : "))

            print("------------------------------------------------")
            print("------------------------------------------------")

            balance = balance+deposit_amount

            print(f"{deposit_amount} is credited from your account ")

            print("------------------------------------------------")
            print("------------------------------------------------")

            print(f"Your updated balance is {balance}")

            print("------------------------------------------------")
            print("------------------------------------------------")
            
        if option == 4:
            break
       
else:
    print("Wrong pin please try again !")
