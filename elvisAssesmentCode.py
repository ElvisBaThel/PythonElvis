option = 2
queue = ['A19','B28','C23','D4','E78','F90','G32','H54','I32','J12','J67','L90','M87','N6','O36','P12','Q24']

while option != 3:

    print ("Welcome to WhooziJuicy \n \n")

    age = input ("How old are you? \n")

    if int(age) < 18:
        print ("You are too young to get in \n")
    elif int(age) >= 90:
        print ("You are too old to get in \n")
    else:
        queue.append(str(age))
        print ("You in, enjoy yourself \n")

    option = input ("Press 1 to view the queue \nPress 2 to continue \nPress 3 to see the age of Q24 \n \n")

    if int(option) == 1:
        print (queue)
        option = input ("Press 2 to continue and let someone else in \n")
    elif int(option) == 2:
        print ("\n")
    elif int(option) == 3:
        position = queue.index('Q24')
        position2 = position - 2

        person1 = queue[position]
        age1 = person1[1:]

        person2 = queue[position2]        
        age2 = person2[1:]

        
        print (int(age1) + int(age2))
        
