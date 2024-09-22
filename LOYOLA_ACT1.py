month = ["January" , "February" , "March" , "April" , "May" , "June" , "July" ,
          "August" , "September" , "October" , "November" , " December"]

while True:
    input_month = int(input("\nEnter your birth month number: "))

    if 1 <= input_month <= 12 :
        break
    
    else :
        print("Invalid input!")

print(f"\nYour birth month is {month[input_month - 1]}.")
