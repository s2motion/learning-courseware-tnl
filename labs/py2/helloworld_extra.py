'''Here's a less trivial lab, testing your knowledge of basic Python
object-oriented programming.

(Remember: if a method response has quotes around it, that means the
method returns a string.  If there are no quotes, that means it
printed (i.e., using print()).

>>> fido = Dog("Fido")
>>> fido.description()
'Fido the Dog'
>>> fido.speak()
'Woof!'

>>> fifi = Cat("Fifi")
>>> fifi.description()
'Fifi the Cat'
>>> fifi.speak()
'Meow!'

>>> nemo = Fish("Nemo")
>>> nemo.description()
'Nemo the Fish'
>>> nemo.speak()
''

>>> fifi.emote()
Fifi the Cat says: Meow!
>>> fido.emote()
Fido the Dog says: Woof!
>>> nemo.emote()
Nemo the Fish says: 

'''

# Write your code here:
class Animal(object):
    def __init__(self, word, animal_name, sneak):
        self.word = word
        self.animal_name = animal_name
        self.sneak = sneak
    def description(self):
        print ("'%s the %s'" % (self.word, self.animal_name))
    def speak(self):
        print("'%s'" % self.sneak)
    def emote(self):
        print("%s the %s says: %s" % (self.word, self.animal_name, self.sneak))

class Dog(Animal):
    def __init__(self, word):
        super(Dog, self).__init__(word, 'Dog', 'Woof!')

class Cat(Animal):
    def __init__(self, word):
        super(Cat, self).__init__(word, 'Cat', 'Meow!')

class Fish(Animal):
    def __init__(self, word):
        super(Fish, self).__init__(word, 'Fish', '')


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
