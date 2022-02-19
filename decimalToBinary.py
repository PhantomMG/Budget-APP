# Function decToBin takes a decimal number as an input

def decToBin(num):
    digit=num%2
    rest=int(num/2)

    if num>1:
        decToBin(rest)
    print(digit,end="")

while True:
    try:
        decimalNumber=input("Enter a decimal number: ")
        decimalNumber=int(decimalNumber)
        break
    except ValueError:
        print("Please enter a valid decimal number!")
print("Success! Here is your binary number: ", end=" ")
decToBin(decimalNumber)