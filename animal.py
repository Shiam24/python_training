class Animal:
    def speak(self):
        print("Animal speaks")
        

class Dog(Animal):
    def speak(self):
        super().speak()
        print("...but also barks!")

    def bark(self):
        print("woof!")



if __name__ == "__main__":
    a = Animal()
    a.speak()
    print()

    d = Dog()
    d.speak()
    d.bark()
