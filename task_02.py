#Задача 2
#https://www.codewars.com/kata/57e92e91b63b6cbac20001e5

def duty_free(price, discount, holiday_cost):
    x=price*discount*0.01
    return int(holiday_cost/x)
