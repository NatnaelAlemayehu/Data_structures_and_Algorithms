import matplotlib.pyplot as plt
import timeit
import random
import string
import time

time_list1 = []
input_size1 = []


# max value
def measure():    
    for i in range(1, 101, 10):
        start = time.clock()
        random_list = random.sample(range(1, 500), i)       
        maximum_number = max(random_list)
        end = time.clock()           
        execution_time = end - start
        time_list1.append(execution_time)
        input_size1.append(i)

    plt.plot(input_size1, time_list1)
    plt.ylabel('Time used in microsecond')
    plt.title('Max value in list algorithm time')
    plt.show()
    
measure()

#capitalise
time_list2 = []
input_size2 = []
def lower_case():
    start = time.clock()
    Capitalised_Strings = ""
    letters = string.ascii_uppercase
    for a in range(1, 101, 10):
        new_capitalised_string = Capitalised_Strings.join(
            random.choice(letters) for i in range(a))
        lowercased_strings = new_capitalised_string.lower()
        end = time.clock()
        execution_time = end - start
        time_list2.append(execution_time)
        input_size2.append(a)
    
    plt.plot(input_size2, time_list2)
    plt.ylabel('Time used in misecond')
    plt.title('Capital to small letter changing algorthm time')
    plt.show()

lower_case()


#sort
time_list3 = []
input_size3 = []

def sort_function():
    start = time.clock()
    Capitalised_Strings = ""
    letters = string.ascii_uppercase
    for a in range(1, 101, 10):
        Start = 10
        Stop = 1000        
        random_list = random.sample(range(Start, Stop), a)
        random_list.sort()
        end = time.clock()
        execution_time = end - start
        time_list3.append(execution_time)
        input_size3.append(a)
        
    plt.plot(input_size3, time_list3)
    plt.ylabel('Time used in microsecond')
    plt.title('sort function algorithm time')
    plt.show()

sort_function()


time_list3 = []
input_size3 = []


def sort_function():
    start = time.clock()
    Capitalised_Strings = ""
    letters = string.ascii_uppercase
    for a in range(1, 101, 10):
        Start = 10
        Stop = 1000
        random_list = random.sample(range(Start, Stop), a)
        random_list.sort()
        end = time.clock()
        execution_time = end - start
        time_list3.append(execution_time)
        input_size3.append(a)

    plt.plot(input_size3, time_list3)
    plt.ylabel('Time used in microsecond')
    plt.title('sort function algorithm time')
    plt.show()


sort_function()
