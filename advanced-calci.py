HISTORY_FILE =  "history.txt"

def show_history():
    file =open(HISTORY_FILE,'r') #read file usong read mode
    lines = file.readlines()
    if len(lines) == 0:# if no data in txt then return message 
        print("No History found")
    else:
        for line in reversed(lines):
            print(lines.strip())
    file.close()

def clear_history():#function to clear the exixting data in txt file 
    file = open(HISTORY_FILE, 'w') #in erite mode the previous data gets clears and file beacomes empty 
    file.close()
    print("History Cleared")

def save_to_history(equation, result):#write the result in txt file 
    file = open(HISTORY_FILE, 'a')
    file.write(equation + "=" + str(result) + "\n") #using concatenation to show result as eqaution of maths 
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input: num operator num ( eg: 8+9)")
        return
    
    num1 =float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2 
    elif op == "/":
        if num2 == 0:
            print("Divison by zero")
            return
        result  = num1 / num2   

    else:
        print('Invalid oprator : use only "+, -, *, /')
        return
    if int(result) ==  result:# convert float result into int
        result = int(result)
    print("Result:", result) #print the final result 
    save_to_history(user_input, result)   #save the result in the txt file       

def main():
    print('---SIMPLE CALCULATOR(type history, clear or exit)')
    while True:
        user_input= input("Enter Calculation (=-*/) or command (history, clear, exit))")
        if user_input == 'exit':
            print("Goodbye")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input) 

main()
