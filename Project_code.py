def subsumption(main_list):
    length1 = len(main_list)
    z={}
    u = ""
    for i in range(len(main_list)):
        z[i]=[]
     
    for i in range(len(main_list)):
         
         for j in range(len(main_list)):
            
            if len(main_list[i])<=len(main_list[j]):
              k=0   
              while(k+len(main_list[i])<=len(main_list[j])):
                 if main_list[i]==main_list[j][0+k:len(main_list[i])+k] and main_list[i]!=main_list[j]:
                   z[i].append(main_list[j])
                   
                 k+=1  
    # print(z)             
    for i in z.keys():
        if z[i]!=[]:
           for j in z[i] :
            if j in main_list:    
             main_list.remove(j)
    length = len(main_list)
    for i in main_list:
        u += "".join(i) + "+"
    u = u[: -1]
    if(length1 == length):
        return 0,u
    else:
        return 1,u

def canBeReduced(list1, list2):
    count = 0 
    temp_val = ""
    judge_list = []
    for iter1 in list1:  
        sub_list = []
        for iter2 in list2:
            d = dict()
            for iter3 in (iter1 + iter2):  
                if(iter3 not in d.keys()):
                    d[iter3] = 1
                else:
                    d[iter3] += 1
            if(len(d) == 2 and set(d.values()) == set([1, 2])):
                for iter4 in d.keys():
                    if('n' != iter4):
                        judge_list.append(iter4)  
                        count += 1
    judge_list = set(judge_list)
    if(count == 1):
        for iter1 in judge_list: 
            val = ""
            for iter2 in (list1 + list2): 
                if(iter1 not in iter2):
                    val += iter2  
        return 1, val
    return 0, None

index_list = []
def func(ipt):
    global index_list
    unique = []
    d = dict()
    main_list, temp = [], ""
    for iter1 in ipt.split("+"):
        sub_list = []
        flag = 0
        for iter2 in iter1: 
            if(iter2 == 'n'):
                flag = 1
            if(iter2 != 'n'):
                temp = ('n' + iter2) if(flag) else iter2   
                flag = 0
                sub_list.append(temp)
        main_list.append(sub_list)
                
    # print(main_list)
    
    l = len(main_list) 
    iter1 = 0
    while(iter1 <= l-2):  
        iter2 = iter1+1
        while(iter2 <= l-1):
            if([iter1, iter2] not in index_list):
                index_list.append([iter1, iter2])
                val = ""
                res, val = canBeReduced(main_list[iter1], main_list[iter2]) 
                if(res):
                    sub_list, temp = [], ""  
                    flag = 0
                    for iter3 in val:
                        if(iter3 == 'n'):
                            flag = 1
                        if(iter3 != 'n'):
                            temp = ('n' + iter3) if(flag) else iter3
                            flag = 0
                            sub_list.append(temp)
                    count_main = 0
                    for iter3 in main_list:
                        if(set(sub_list) != set(iter3)):
                            count_main += 1
                    if(count_main == l):
                        main_list.append(sub_list)
                        l += 1
                    val3 = ""
                    for iter3 in main_list:
                        val3 += "".join(iter3) + '+'
                    val3 = val3[: -1]
                    temp_var = []
                    for iter3 in val3.split('+'):
                        if(iter3 not in temp_var):
                            temp_var.append(iter3)
                    val3 = "+".join(temp_var)
                    ipt = val3
                    return func(ipt)
                
            iter2 += 1 
        iter1 += 1
    return ipt

def main():
    global index_list
    a = 1
    while(a):
        val = ""
        ipt = input("Enter input = ")
        for iter1 in func(ipt).split('+'):
            temp, flag = "", 0
            d = dict()
            for iter2 in iter1 :
                if(iter2 not in d.keys()):
                    d[iter2] = 1
                else:
                    d[iter2] += 1
            for k, v in d.items():
                if(k != 'n' and v > 1):
                    d[k] = 1
            for iter2 in iter1:
                if(d[iter2]):
                    if(iter2 == 'n'):
                        flag = 1
                    else:
                        temp += ("n" + iter2) if(flag) else iter2
                        flag = 0
                    d[iter2] -= 1
            val += temp + '+'
        val = val[: -1]
        
        main_list, temp = [], ""
        for iter1 in val.split("+"):
            sub_list = []
            flag = 0
            for iter2 in iter1: 
                if(iter2 == 'n'):
                    flag = 1
                if(iter2 != 'n'):
                    temp = ('n' + iter2) if(flag) else iter2  
                    flag = 0
                    sub_list.append(temp)
            main_list.append(sub_list)
        flag, val = subsumption(main_list)
        if(flag):
            print("val =", val)
            a = int(input("Continue 1/0:"))
            if(a):
                index_list = []
            continue
        print("val =", val)
        a = int(input("Continue 1/0:"))
        if(a):
            index_list = []

    
if(__name__ == '__main__'):
    main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	# This is subsumption function where we will check if the resultant output is the subset of the input strings
def subsumption(main_list):
    length1 = len(main_list)
    #declare a z empty dictionary and u empty string
    z={}
    u = ""
    # store individual elements of the strings in the form of the list
    for i in range(len(main_list)):
        z[i]=[]
    # This loop iterates over the individual elements of the list
    for i in range(len(main_list)):
         
         for j in range(len(main_list)):
            # checkthe resultant input size less than individual string size
            if len(main_list[i])<=len(main_list[j]):
              k=0   
              while(k+len(main_list[i])<=len(main_list[j])):
                 # if it is a subset change the main_list and append to z
                 if main_list[i]==main_list[j][0+k:len(main_list[i])+k] and main_list[i]!=main_list[j]:
                   z[i].append(main_list[j])
                   
                 k+=1  
    # print(z)             
    for i in z.keys():
        if z[i]!=[]:
           for j in z[i] :
            if j in main_list:    
             main_list.remove(j)
    # Calculate length of the main_list
    length = len(main_list)
    for i in main_list:
        u += "".join(i) + "+"
    u = u[: -1]
    # If the output string length is equal to the input string return 0,u else return 1,u
    if(length1 == length):
        return 0,u
    else:
        return 1,u

# Sending 2 of the individual strings from the input and check whether they are resolvable or not
def canBeReduced(list1, list2):
    count = 0 
    temp_val = ""
    judge_list = []
    # for suppose input to this function is (ipt = nab + ab) then list1 = ['na', 'b'] and list2 = ['a', 'b']
    for iter1 in list1:  
        sub_list = []
        for iter2 in list2:
            d = dict()
            # this for loop is used to get the character count
            for iter3 in (iter1 + iter2):  
                if(iter3 not in d.keys()):
                    d[iter3] = 1
                else:
                    d[iter3] += 1
            # to remove duplicate values we used set over here
            if(len(d) == 2 and set(d.values()) == set([1, 2])):
                for iter4 in d.keys():
                    if('n' != iter4):
                        judge_list.append(iter4)  
                        count += 1
    # judge_list contains the resolvable strings as the list form
    judge_list = set(judge_list)
    if(count == 1):
        for iter1 in judge_list: 
            val = ""
            for iter2 in (list1 + list2): 
                if(iter1 not in iter2):
                    val += iter2  
        return 1, val
    return 0, None

index_list = []

def func(ipt):
    global index_list
    unique = []
    d = dict()
    main_list, temp = [], ""
    for iter1 in ipt.split("+"):
        sub_list = []
        flag = 0
        # For suppose (ipt = anb+bc) iter1 = anb, bc, main_list = [['a', 'nb'], ['b', 'c']]
        #print(iter2) #1st time = a and 2nd time = n and 3rd time  = b
        for iter2 in iter1: 
            if(iter2 == 'n'):
                flag = 1
            if(iter2 != 'n'):
                temp = ('n' + iter2) if(flag) else iter2   
                flag = 0
                sub_list.append(temp)
        main_list.append(sub_list)
                
    # print(main_list)
    
    l = len(main_list) 
    iter1 = 0
    while(iter1 <= l-2):  
        iter2 = iter1+1
        while(iter2 <= l-1):
            if([iter1, iter2] not in index_list):
                index_list.append([iter1, iter2])
                val = ""
                # we need to call canBeReduced function
                res, val = canBeReduced(main_list[iter1], main_list[iter2]) 
                if(res):
                    sub_list, temp = [], ""  
                    flag = 0
                    for iter3 in val:
                        if(iter3 == 'n'):
                            flag = 1
                        if(iter3 != 'n'):
                            temp = ('n' + iter3) if(flag) else iter3
                            flag = 0
                            sub_list.append(temp)
                    count_main = 0
                    for iter3 in main_list:
                        if(set(sub_list) != set(iter3)):
                            count_main += 1
                    if(count_main == l):
                        main_list.append(sub_list)
                        l += 1
                    val3 = ""
                    for iter3 in main_list:
                        val3 += "".join(iter3) + '+'
                    val3 = val3[: -1]
                    temp_var = []
                    for iter3 in val3.split('+'):
                        if(iter3 not in temp_var):
                            temp_var.append(iter3)
                    val3 = "+".join(temp_var)
                    ipt = val3
                    return func(ipt)
                
            iter2 += 1 
        iter1 += 1
    return ipt

def main():
    global index_list
    a = 1
    while(a):
        val = ""
        # Enter the input string for the evaluation
        ipt = input("Enter input = ")
        # Split the given combined string into individual string which are seperated by "+"
        for iter1 in func(ipt).split('+'):
            temp, flag = "", 0
            d = dict()
            # Creating a dictionary and getting the key, value pairs
            for iter2 in iter1 :
                if(iter2 not in d.keys()):
                    d[iter2] = 1
                else:
                    d[iter2] += 1
            for k, v in d.items():
                #After going through the dictionary keys if key vaalue does not contain n aand value is greater than 1 then set d[k] = 1
                if(k != 'n' and v > 1):
                    d[k] = 1
            for iter2 in iter1:
                if(d[iter2]):
                    #set flag = 1 when the iter2 string has n
                    if(iter2 == 'n'):
                        flag = 1
                    else:
                        temp += ("n" + iter2) if(flag) else iter2
                        flag = 0
                    d[iter2] -= 1
            val += temp + '+'
        # Since we are adding + to the temp string we used :-1 to print since we get rid of + in the val string
        val = val[: -1]
        
        main_list, temp = [], ""
        for iter1 in val.split("+"):
            sub_list = []
            flag = 0
            # For suppose we have (ipt = anb+bc) then iter1 = anb, bc  main_list = [['a', 'nb'], ['b', 'c']]
            for iter2 in iter1: 
                if(iter2 == 'n'):
                    flag = 1
                if(iter2 != 'n'):
                    temp = ('n' + iter2) if(flag) else iter2  
                    flag = 0
                    sub_list.append(temp)
            main_list.append(sub_list)
        # subsumption function will return a number and a string which will be assigned to flag aand val
        flag, val = subsumption(main_list)
        if(flag):
            print("val =", val)
            a = int(input("Continue 1/0:"))
            if(a):
                index_list = []
            continue
        # print the final output
        print("val =", val)
        # Give input 1 if we want to enter another input string or give 0 if you want to exit from the program
        a = int(input("Continue 1/0:"))
        if(a):
            index_list = []

    
if(__name__ == '__main__'):
    main()

