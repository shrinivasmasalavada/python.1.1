# ATM Simulation Program

# Initial setup
balance = 1000  # Starting balance
correct_pin = "1234"  # Hardcoded PIN for simplicity

print("--- Welcome to the ATM Simulation ---")

# Step 1: Login (PIN Verification)
entered_pin = input("Please enter your 4-digit PIN: ")

if entered_pin == correct_pin:
    print("\nLogin Successful!")
    
    # Step 4: Looping Behavior (Repeat until Exit)
    while True:
        # Step 2: Menu Options
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        # Step 3: Core ATM Operations
        if choice == '1':
            print(f"Your current balance is: ${balance}")
            
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"${amount} has been deposited successfully.")
            else:
                print("Invalid amount. Please enter a positive value.")
                
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance! Transaction failed.")
            elif amount <= 0:
                print("Invalid amount. Please enter a positive value.")
            else:
                balance -= amount
                print(f"${amount} has been withdrawn successfully.")
                
        elif choice == '4':
            print("Thank you for using our ATM. Goodbye!")
            break  # Exit the loop
            
        else:
            print("Invalid choice! Please select an option between 1 and 4.")
            
else:
    print("Incorrect PIN! Access Denied.")