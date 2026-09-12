main
is_open=True
tekets=5
while tekets>0 and is_open :
    if tekets==0:
        print("the tekets is empity")
    
    name=input("enter your name: ")
    teket_num=int(input("enter how much tekets you want to purch= "))
    
    if teket_num<=0:
        print("error: cant git thats number of tekets")
    elif teket_num>tekets:
        print("thats no {teket_num} is aveylable")
    elif teket_num>0 and teket_num<=tekets:
        print(f"the seller name is {name} and they selled {teket_num} of tekets ")
        tekets-=teket_num
# 2. Variables & Data Types
# tickets_available = 5
is_open = True
movies = 6 
movies_name = ["spider_man", "batman", "superman"]

rooms = 3
rooms_capcity = [20, 30, 60]

branches = 4


# 6. Iteration (while loop)
while is_open:
    print(f"\n--- Tickets Available: {tickets_available} ---")
    
    # 4. Input/Output
    customer_name = input("Enter your name: ")
    requested_tickets = int(input("How many tickets would you like? "))
    
    # 5. Control Flow & 3. Operators
    if 0 < requested_tickets <= tickets_available: # requested_tickets <= tickets_available and requested_tickets > = 0
        tickets_available -= requested_tickets # tickets_available = tickets_available - requested_tickets
        print(f"Success! {customer_name} bought {requested_tickets} ticket(s).")
    
    elif requested_tickets > tickets_available:
        print(f"Sorry {customer_name}, we only have {tickets_available} ticket(s) left.")
        
    else:
        print("Invalid request. You must buy at least 1 ticket.")
        
    # 6. Iteration (Loop control)
    if tickets_available == 0:
        print("Sold out! Closing the ticketing system.")
        is_open = False
        break
main
