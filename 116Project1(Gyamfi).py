







"""Author: Henry Gyamfi

  Date-Written: 2/3/2021

  Date-Modified: 2/9/2021

  Description: In this project, I created a program that shows a command line argument when run. The command line argument shows a
  pop-up box and picks two integers and randomize the list of integers. After entering the 2 numbers, the program will sort the randomized data
  and arrange them in order. It will give an account of the time taken to arrange the data list in order.
  

  Variables Used:

     sorted - Used to tell if the data has been arranged or not

     maxInList - gives a total amount of data in the list

     setOfDataA - randomizes all data found within the range of the first number entered in the pop up box

     setOfDataB - randomizes all data found within the range of the second number entered in the pop up box

     sortedSetA - bubble sorts data A, which is the first number entered

     sortedSetB - bubble sorts data B, which is the second number entered"""













import sys

import time

import random

def bubbleSort(setOfData):
    sorted = False

    maxInList = len(setOfData)     ### This gives an idea about the total number of data in the list
    
    

    while not sorted:
        
        sorted = True
        
        for i in range(maxInList-1):             ### Gives an idea about the number of data in the list that will be arranged
            
            if setOfData[i] > setOfData[i+1]:
                
                setOfData[i], setOfData[i+1] = setOfData[i+1], setOfData[i]    ###swaps the data as the sorting goes on in the list
                
                sorted = False

        maxInList -= 1         ###the list decreases as the arrangement goes on in the range

    return setOfData
    

def main():
     

    setOfDataSizeA = int(sys.argv[1])      ###data A is passed as 1st Argument
        
    
    setOfDataSizeB = int(sys.argv[2])      ###data B is passed as 2nd argument
    

    setOfDataA = random.sample(range(setOfDataSizeA), setOfDataSizeA)      ### randomizes all data found within the range of data A 
    

    setOfDataB = random.sample(range(setOfDataSizeB), setOfDataSizeB)        ###randomizes all sample found within the range of data B
    

    print("Starting first sort, sort size is: " + str(len(setOfDataA)))
    

    start = time.time()                         ### Time when sorting of data A begins
    

    sortedSetA = bubbleSort(setOfDataA)
    

    elapsedTime = time.time() - start             ###Provides time taken to sort all of data A

    print("\nFirst Sort done\n\nElapsed Time: " + str(elapsedTime) + " seconds")        ###Provides result for sorting data A

    print("\n...")

    print("\nStarting Second sort, sort size is: " + str(len(setOfDataB)))

    start = time.time()                     ###Starts time for sorting data B

    sortedSetB = bubbleSort(setOfDataB)

    elapsedTime = time.time() - start         ### Records time for data B to be sorted 

    print("\nSecond Sort done\n\nElapsed Time: " + str(elapsedTime) + " seconds")          ###Provide results for the second sort


if len(sys.argv) ==3:
    try:

        main()

    except:

        print(Error)
        
        

else:
    print("Error: Please Enter two set of values!")    ###Tells the User to enter two sets of integers
     
    


    
    
