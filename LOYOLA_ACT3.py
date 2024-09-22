while True:
    shapes = input("\nEnter ASCII art shape: ")
    
    if shapes == "draw line":
        no = int(input("Pick 5 or 7: "))
        if no == 5:
            print("*****")
        elif no == 7:
            print("*******")
        else:
            print("Invalid input. Please pick 5 or 7.")   
    elif shapes == "draw striped line":
        no = int(input("Pick 5 or 7: "))
        if no == 5:
            print("*_*_*")
        elif no == 7:
            print("*_*_*_*")
        else:
            print("Invalid input. Please pick between 5 or 7.")  
    elif shapes == "draw parallelogram":
        no = int(input("Pick 5 or 7: "))
        if no == 5:
            print("______*****\n_____*****_\n___*****___\n__*****____\n_*****_____")
        elif no == 7:
            print("______*******\n_____*******_\n___*******___\n__*******____\n_*******_____")
        else:
            print("Invalid input. Please pick between 5 or 7.")       
    elif shapes == "draw triangle":
        no = int(input("Pick 5 or 7: "))
        if no == 5:
            print("*****\n****_\n***__\n**___\n*____")
        elif no == 7:
            print("*******\n******_\n*****__\n****___\n***____\n**_____\n*______")
        else:
            print("Invalid input. Please pick between 5 or 7.")      
    else:
        print("Wrong shape. Please enter draw line, draw striped line, draw parallelogram, or draw triangle.")
