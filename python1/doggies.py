#!/usr/local/bin/python3
#
# Dog Lister
# doggies.py
#
# 2015 June 29th
#
""" Keeps a list of name and breed of dogs, represented by class instances. """

class Dog:
    """ Representation of a dog with a name and breed. """
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# List that keeps track of all the doggies        
dogs = []

while True:
    name = input("Name: ").strip()
    if not name: # Exit if no entry name
        break
    breed = input("Breed: ").strip()
    
    doggie = Dog(name, breed)
    dogs.append(doggie)
    
    print("DOGS")
    # Print the content of 'dogs'
    for num, dog in enumerate(dogs):
        print("{0}. {1}:{2}".format(num, dog.name, dog.breed))
    print("*" * 40)