import art
import operation

print(art.logo)
proceed = True

first_no = int(input("Enter the first number?: "))
print("+\n-\n*\n/\n")

while proceed:
    symbol = input("Pick an operation: ")
    second_no = int(input("Whats the next number?: "))

    if(symbol == "+"):
        first_no = operation.add(first_no,second_no)
        print (first_no)
    elif(symbol == "-"):
        first_no = operation.sub(first_no,second_no)
        print (first_no)
    elif(symbol == "*"):
        first_no = operation.mul(first_no,second_no)
        print (first_no)
    elif(symbol == "/"):
        first_no = operation.div(first_no,second_no)
        print (first_no)

    ans = input("Type 'y' to continue and 'n' to exit ")   

    if(ans == "n"):
        proceed = False 
