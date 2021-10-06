# -----------------------------------------------------------
# Example of naive Bayes classifier  implementation
# (C) 2021 Paweł Goj, PL
# Released under MIT license
# -----------------------------------------------------------


import json
from scipy.stats import norm
import numpy as np


#Read users from json file
with open('data.json', 'r') as file:
    file = file.read()


#earlier customers list
customers = json.loads(file)


#predicts whether the new_customer owns a car
new_customer = {}
new_customer['age'] = 25
new_customer['salary'] = 3500


def predict_the_customer_owns_a_car(new_customer, customers):

    probabilites_have_car_base_age_and_income = create_probabilities(customers, True)
    probabilites_no_have_car_base_age_and_income = create_probabilities(customers, False)

    product_probabilites_have_car = customer_have_car_probability(customers)
    product_probabilites_no_have_car = 1 - product_probabilites_have_car

    for item in probabilites_have_car_base_age_and_income:
        product_probabilites_have_car *= item

    
    for item in probabilites_no_have_car_base_age_and_income:
        product_probabilites_no_have_car *= item
    
    probability_of_new_customer_have_car = product_probabilites_have_car / (product_probabilites_no_have_car\
        + product_probabilites_have_car)

    return probability_of_new_customer_have_car


def create_probabilities(customer, car: bool):

    salary = [customer['salary'] for customer in customers if customer['car'] == car]
    age = [customer['age'] for customer in customers if customer['car'] == car]

    N = len(salary)

    average_salary = sum(salary) / N

    list = [(X - average_salary) ** 2 for X in salary]
    standard_deviation_of_salary = (sum(list) / N) ** (1/2)

    average_age = sum(age) / N

    list = [(X - average_age)**2 for X in age]
    standard_deviation_of_age = ((sum(list) / N)) ** (1/2)

    #norm distribution 
    probability_based_on_income = norm.pdf(new_customer['salary'], average_salary, standard_deviation_of_salary)

    probability_based_on_age = norm.pdf(new_customer['age'], average_age, standard_deviation_of_age)


    return probability_based_on_income, probability_based_on_age


def customer_have_car_probability(customers):
    quantity = 0 

    for customer in customers: 

        if customer['car'] == True:
            quantity+=1 

    probability = quantity / len(customers)

    return probability


probability = predict_the_customer_owns_a_car(new_customer, customers)


print(probability)