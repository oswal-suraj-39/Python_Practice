# Write a program to implement the concept of queue using list.

queue = []
c = 0

while c != 4:
    print("\n1. add a element")
    print("\n2. remove a element")
    print("\n3. display a element")
    print("\n4. exit")
    
    c = int(input("your choice: "))

    if c == 1:
        n = int(input("how many element you want to enter in a queue?\n"))

        for i in range(n):
            element = input("enter element: ")
            queue.append(element)
                         
    elif c == 2: 
        if len(queue) > 0:
            queue.pop(0)
        else:
            print("queue is empty")
    
    elif c == 3:
        print(queue)
    
    elif c == 4:
        break