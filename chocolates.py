#Simple FIFO
queue = []

def user_queue_fifo(k: int):
    for i in range(0, k):
        studentName = input("Enter the name of student #"+ str(i+1) +": ")
        queue.append(studentName)
    for i in range(0, k):
        print(str(queue[i]) +" gets chocolate #" +str(i+1) +"")

#Simple LIFO
def user_queue_lifo(k: int):
    for i in range(0, k):
        studentName = input("Enter the name of student #"+ str(i+1) +": ")
        queue.append(studentName)
    NewArray = queue[::-1]
    for i in range(0, 4):
        print(str(NewArray[i]) +" gets chocolate #" +str(i+1) +"") 

user_input = int(input("Select 0 for FIFO mode, select 1 for LIFO mode. "))
user_input2 = int(input("Enter the amount of students. "))
if user_input == 1:
    user_queue_fifo(user_input2)
elif user_input == 0:
    user_queue_lifo(user_input2)
else:
    print("Error: Invalid Response.")