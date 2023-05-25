import pandas as pd
import numpy as np

#The first param is your name and the second param is a int that if it is 1 it 
#counts for the first half of the week and if its 2 the second half
def YourRooms(name):
    sheet_id = ''
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
   # df = pd.read_csv('Daily Checks - 4_3-4_7.csv', header = 1)
    arr = df.to_numpy()

    print(name,'Rooms to Check')
    NumOfRooms = 0;
    return_value = ''

    
    # loop through the rows of the array
    for i in range(arr.shape[0]):
            # loop through the columns of the array
        for j in range(12):
               if(name == arr[i][j]):
                    # print the current cell value
                    print(arr[i][j-1])
                    NumOfRooms = NumOfRooms+1
                    return_value += arr[i][j-1] + " | "

    
    # loop through the rows of the array
    for i in range(arr.shape[0]):
        # loop through the columns of the array
        for j in range(13,21):
                if(name == arr[i][j]):
                    # print the current cell value
                    print(arr[i][j-1])
                    NumOfRooms = NumOfRooms + 1
                    return_value += arr[i][j-1] + " |  "

    return return_value


def RoomsLeft(name):
    sheet_id = '1Tqvx93IeyNNW_jgs4O6YxkSVYAb-eyfF-6OHnSciIRU'
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    # df = pd.read_csv('Daily Checks - 4_3-4_7.csv', header = 1)
    arr = df.to_numpy()

    print(name,'Rooms you have left')
    return_value = '';

    # loop through the rows of the array
    for i in range(arr.shape[0]):
            # loop through the columns of the array
        for j in range(arr.shape[1]):
               if(name == arr[i][j]):
                    # print the current cell value
                    print(arr[i][j-1])
                    return_value += arr[i][j-1] + " | "

