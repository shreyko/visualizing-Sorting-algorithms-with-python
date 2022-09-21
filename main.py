
from matplotlib import pyplot as plt


main_text = '''1. Bubble sort\n
2. Insertion sort\n
3.Quick sort \n'''

# initial fucntions
def input_list(l):
    ##l.append(selection)
    #choice =  input("continue (Y/N) ").lower()
    #if choice == "y":
        #return input_list(l)
    #else:
        #return l
    inpt = eval(input("enter list enclosed in [] brackets and with comma separated values (e.g. [1,2,3]): \n"))
    return inpt
    


def bubble_sort(l1 , l2):
    plt.figure(figsize=(14,4))
    for i in range(len(l1) -1):
        for j in range(len(l1)-i-1):
            colour =[]
            for k in range(len(l1)):
                colour.append("Blue")
            
            colour[j] = "red"
            colour[j+1] = "pink"
            plt.bar(l2 , l1 , color = colour)
            plt.title("RED : The current number; PINK: The number that RED is being compared to ; GREEN : The final sorted position of RED for that iteration. ")
            plt.pause((1/len(l1)) + 0.07)
            plt.clf()
            if l1[j] > l1[j+1]:
                l1[j] , l1[j+1]  = l1[j+1] , l1[j]
                colour[j] = "pink"
                colour[j+1] = "green"
                plt.bar(l2 , l1 , color = colour)
                plt.title("RED : The current number; PINK: The number that RED is being compared to ; GREEN : The final sorted position of RED for that iteration. ")
                plt.pause((1/len(l1)) + 0.07)
                plt.clf()
            else: #think about this
                colour[j] = "green"
                colour[j+1] = "pink"
                plt.bar(l2 , l1 , color = colour)
                plt.title("RED : The current number; PINK: The number that RED is being compared to ; GREEN : The final sorted position of RED for that iteration. ")
                plt.pause((1/len(l1)) + 0.07)
                plt.clf()

    
    plt.close()
    print("soretd list: " , l1)
            

def insertion_sort(l2, l3):
    plt.figure(figsize=(14,4))
    for i in range(1, len(l2)):
        to_sort = l2[i]
        j= i-1
        colour =[]
        for k in range(len(l2)):
                colour.append("Blue")
            
        #colour[j] = "pink"
        colour[i] = "red"
        plt.bar(l3 , l2 , color = colour)
        plt.title("RED : The current number; PINK: The number that RED is being compared to ; GREEN : The final sorted position of RED for that iteration. ")    
        plt.pause((1/len(l2)) + 0.07)
        plt.clf()
        
        while j>=0 and to_sort < l2[j]:
            colour[j] = "pink"
            colour[j+1] = "pink"
            plt.bar(l3 , l2 , color = colour)
            plt.title("RED : The current number; PINK: The number that RED is being compared to ; GREEN : The final sorted position of RED for that iteration. ")
            plt.pause((1/len(l2)) + 0.07)
            plt.clf()
            l2[j+1] = l2[j]
            j-=1
        l2[j+1] = to_sort
        colour[j+1] = "green"
        #colour[i] = "red"
        plt.bar(l3 , l2 , color = colour)
        plt.title("RED : The current number; PINK: The number that RED is being compared to ; GREEN : The final sorted position of RED for that iteration. ")    
        
        plt.pause((1/len(l2)) + 0.07)
        plt.clf()
    
            
    plt.close()
    print("soretd list: " , l2)



def quick_sort(l3,h,l,l4,count):
    
    plt.figure(figsize=(14,4))
    for i in range(1, len(l3)):
        
        colour =[]
        for k in range(len(l3)):
                colour.append("Blue")
    colour[l] = "yellow"
    plt.bar(l3 , l4 , color = colour)
    plt.title("Iteration " + str(count) + "; Yellow: The pivot point ; Orange: all values to the left of than pivot ; pink: all values to the right of than pivot")    
    plt.pause(1/len(l3))
    plt.clf()
    
    pivot = l3[l]
    i = l
    j = h
    while i<j:
        while (l3[i] <= pivot):
            colour[l] = "yellow"
            colour[i] = "orange"
            plt.bar(l3 , l4 , color = colour)
            plt.title("Iteration " + str(count) + "; Yellow: The pivot point ; Orange: all values to the left of than pivot ; pink: all values to the right of than pivot")    
            plt.pause((1/len(l3)) + 0.15)
            plt.clf()
            i+=1
        while (l3[j] > pivot):
            colour[l] = "yellow"
            colour[j] = "pink"
            plt.bar(l3 , l4 , color = colour)
            plt.title("Iteration " + str(count) + "; Yellow: The pivot point ; Orange: all values to the left of than pivot ; pink: all values to the right of than pivot")    
            plt.pause((1/len(l3)) + 0.15)
            plt.clf()
            j-=1
        if (i<j):
            l3[i],l3[j] = l3[j],l3[i]
            colour[i] = "orange"
            colour[j] = "pink"
            plt.bar(l3 , l4 , color = colour)
            plt.title("Iteration " + str(count) + "; Yellow: The pivot point ; Orange: all values to the left of than pivot ; pink: all values to the right of than pivot")    
            plt.pause((1/len(l3)) + 0.15)
            plt.clf()
    l3[l],l3[j] = l3[j],l3[l]
    colour[l] = "yellow"
    colour[j] = "pink"
    plt.bar(l3 , l4 , color = colour)
    plt.title("Iteration " + str(count) + "; Yellow: The pivot point ; Orange: all values to the left of than pivot ; pink: all values to the right of than pivot")    
    plt.pause((1/len(l3)) + 0.3)
    plt.clf()
    plt.close()
    
    return j

def quickort_actual(l3, low, high ,l4 , count = 0):

    count+=1
    if low < high:

        j = quick_sort(l3,high,low,l4,count)
        return (quickort_actual(l3, low , j,l4,count) , quickort_actual(l3, j+1 , high,l4,count) , l3)
    
        
    
      
        
    
        
    


#main-section

run = True
while run:
    lst = input_list([])
    print(lst)
    y_val = [i for i in range(1,len(lst)+1)]
    print(main_text)
    ch = int(input("enter the selection: "))
    if ch == 1:
        bubble_sort(lst , y_val)
    if ch==2:
        insertion_sort(lst ,y_val)
    if ch ==3:
        
        print("Sorted list: ",quickort_actual(lst,0,len(lst)-1,y_val)[-1])
        
    ch_2 = input("Continue? (Y/N) ").lower()
    if ch_2 == "y":
        pass
    else:
        run = False

