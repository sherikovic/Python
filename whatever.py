print("Hello me!")
one = 1
two = 2
hello = "hello"
print(one, two, hello)
print(float(7))

numbers=[]
numbers.append(10)
numbers.append("Eric")

print("This is the list containing numbers %s" % numbers[0])

print("hello " * 5)

print([1, 3, 2] * 5)

x = object()
y = object()
x_list = [x] * 10
y_list = [y] * 5

big_list = x_list + y_list
print(big_list.count(y))

name = "Jessy"
print("Hello," + " " + name + "!")
print("Hello, %s!" % name)

age = 25.2
print("%s is %.1f years old." % (name, age))

data = ("John", "Doe", 53.44)
format_string = "Hello"

print("%s %s %s, your balance is $%.2f!" % (format_string, data[0], data[1], data[2]))
format_string = "Hello %s %s, your current balance is $%s"
print(format_string % data)

mystring = "this is a silly string"
print(mystring[::-1])
print(mystring.upper())
print(mystring.startswith("thiS"))
print(mystring[10:15:2])


numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number is 237:
        break
    elif number % 2 == 0:
        print(number)



class Vehicle_class1:
    def __init__(self):
        self.name = "car"
        self.price = 0
        self.color = "Unknown"
    
    def setName(self, name):
        self.name = name
    
    def setColor(self, color):
        self.color = color
    
    def setPrice(self, price):
        self.price = price
    
    def retDescrption(self):
        carDescription = "The requested car of a name %s has a color of %s and costs $%.2f" % (self.name, self.color, self.price)
        return carDescription
    
car1 = Vehicle_class1()
car2 = Vehicle_class1()
car1.setName("Fer")
car1.setColor("Red")
car1.setPrice(60000.00)
car2.setName("Jump")
car2.setColor("Blue")
car2.setPrice(10000.00)

print(car1.retDescrption())
print(car2.retDescrption())


class Vehicle_class2:
    def __init__(self, name, color, price):
        self.name = name
        self.price = price
        self.color = color
    
    def setName(self, name):
        self.name = name
    
    def setColor(self, color):
        self.color = color
    
    def setPrice(self, price):
        self.price = price
    
    def retDescrption(self):
        carDescription = "The requested car of a name %s has a color of %s and costs $%.2f" % (self.name, self.color, self.price)
        return carDescription

car1 = Vehicle_class2("", "", 0.0)
car2 = Vehicle_class2("", "", 0.0)
car1.setName("Ferari")
car1.setColor("Yellow")
car1.setPrice(70000.00)
car2.setName("Jumper")
car2.setColor("Green")
car2.setPrice(50000.00)

print(car1.retDescrption())
print(car2.retDescrption())

class Vehicle_class3:
    def setName(self, name):
        self.name = name

    def setColor(self, color):
        self.color = color

    def setPrice(self, price):
        self.price = price

    def retDescrption(self):
        carDescription = "The requested car of a name %s has a color of %s and costs $%.2f" % (self.name, self.color, self.price)
        return carDescription

car1 = Vehicle_class3()
car2 = Vehicle_class3()
car1.setName("Ferariiii")
car1.setColor("Yellowwww")
car1.setPrice(900000.45)
car2.setName("Jumperrrr")
car2.setColor("Greennnn")
car2.setPrice(200000.78)

print(car1.retDescrption())
print(car2.retDescrption())


checkForOddNums = lambda x : (x % 2) == 1
l = [2,4,7,3,14,19]
for i in l:
    print(checkForOddNums(i))

def bar(first, second, third, **options):
    for key in options:
        print(key)

bar(1, 2, 3, action = "sum", number = "first")


inv = {"Dirty Sock": 1,
       "Microphone": 4,
       "Hair Pin": 2,
       "Bowlin Ball": 21}

inv1 = dict(sorted(inv.items(), key= lambda item : item[1], reverse=True))
inv2 = sorted(inv)
inv3={k:v for k, v in sorted(inv.items(), key=lambda item:item[0])}
print(inv3)


open_tup = tuple('({[')
close_tup = tuple(')}]')
map = dict(zip(open_tup, close_tup))
print(open_tup)
print(map)

lst = [[1], [2]]
lst.extend([[3]])
print(lst)

s1Count = [1] * 12
print(s1Count)