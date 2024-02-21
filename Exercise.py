#Problem-1
def sum_of_digits():
    a = int(input())
    sumofdigits = 0
    while(a>0):
        num = int(a%10)
        sumofdigits+=num
        a = a/10
    return sumofdigits



#Problem-2
def find_armstrong_number():
    number = int(input())
    original_number_to_check = number
    original_number = number
    power_counter = 0
    while (number>0):
        power_counter+=1
        number = int(number/10)
    check_armstrong_number = 0
    while(original_number_to_check>0):
        rem_armstrong = int(original_number_to_check%10)
        check_armstrong_number = check_armstrong_number+(rem_armstrong**power_counter)
        original_number_to_check = original_number_to_check/10
    print("Value:",check_armstrong_number)
    if check_armstrong_number == original_number:
        print("It is an armstrong number")
    else:
        print("It is not an armstrong number")



#Problem-3
def reverse_string():
    input_string = input()
    txt = input_string[::-1]
    if txt == input_string:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")



#Problem -4
def frequency_calculation(*array):
    my_dict={}
    for i in array:
        if i in my_dict:
            my_dict[i] +=1
        else:
            my_dict[i] =1

    for key,value in my_dict.items():
        print(key,value)


#problem-5
def primeFactors(num):
    c = 2
    while(num > 1):
        if(num % c == 0):
            print(c, end=" ")
            num = num / c
        else:
            c += 1

    
#problem-6
def factorial(num):
    factorial = 1
    for i in range (1,num+1):
        factorial *= i
    return factorial
def binomial_coefficient(n,r):
    factorial_of_n = factorial(n)
    factorial_of_r = factorial(r)
    nr = n -r
    factorial_of_nr = factorial(nr)
    binomial_coefficient_calculation = (factorial_of_n/(factorial_of_r*factorial_of_nr))
    return binomial_coefficient_calculation

# problem-7
'''Linear Search'''
def linearSearch(*args,element_to_search):
    arr = list(args)
    arr.sort()
    for i in arr:
        if element_to_search == i:
            print("the value is found")
            break
  
#linearSearch(1,2,3,4,5,6,123,14,element_to_search=123)
'''Binary Search'''
def BinarySearch(*args,element_to_search):
    arr = list(args)
    arr.sort()
    length_of_element = len(arr)
    print(length_of_element)
    middle_element_index = int((len(arr)/2))
    print("the mid element is: ",arr[middle_element_index])
    if (arr[middle_element_index]) > element_to_search:
        for i in range (0,middle_element_index+1):
            if (element_to_search == arr[i]):
                print("The value is sorted from 1st half")
                break
    else:
        for i in range (middle_element_index,(length_of_element)):
            if (element_to_search == arr[i]):
                print("The value is sorted from 2nd half")
                break


# BinarySearch(12,3,4,56,67,7,123,4,5,element_to_search=123)

#problem -8
def frequency_words(file):
    words =[]
    with open (file,"r") as f:
        for  line in f:
            words.extend(line.split())
    from collections import Counter
    counts = Counter(words)
    print("Words count:",counts)
    words_with_3 = counts.most_common(3)
    print("Words that occur 3 most frequent times: ",words_with_3)
   



