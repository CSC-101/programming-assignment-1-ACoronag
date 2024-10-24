import data
from data import Rectangle


# Write your functions for each part in the space below.

# Part 1
#The function inserts a word and checks each individual value in the word if it's a value through a loop and returns the number of values (int).
def vowel_count(word: str)->int:
    word = word.lower()
    num = 0
    for i in word:
        if i in "aeiou":
            num += 1
    return num


# Part 2
#The function gets inputed a list and if the length is equal to 2, then it'll append it to the new list.
#The function returns a list full of nested lists with a length of 2
def short_lists(lists: list)->list:
    lista =[]
    for i in range(len(lists)):
        if len(lists[i]) == 2:
            lista.append(lists[i])
    return lista


# Part 3
#The function is inputed a list full of nested lists. If a list has a length of 2, it will swap the indexes if the
#first index is greater than the second. If the index is not equal to 2, the list will stay the same. Then the new
#list with nested lists is returned.
def ascending_pairs(lists: list)->list:
    lista = []
    for i in range(len(lists)):
        if len(lists[i]) == 2:
            if lists[i][0] > lists[i][1]:
                lista.append([lists[i][1],lists[i][0]])
            else:
                lista.append(lists[i])
        else:
            lista.append(lists[i])
    return lista


# Part 4
#Input is 2 prices. The function adds the dollars and the cents. if the cents is greater than 100, it will subtract
#100 from cents and add 1 to dollars. Then it returns a new object in the price class with the sum.
def add_prices(price1, price2):
    dollars = price1.dollars + price2.dollars
    cents = price1.cents + price2.cents
    while cents > 100:
        cents -= 100
        dollars += 1
    return data.Price(dollars,cents)

# Part 5
#Input is a rectangle from the Rectangle class. It returns the distance from the two points by using the equation
#to find the distance
def rectangle_area(rectangle1):
    return (rectangle1.top_left.y - rectangle1.bottom_right.y) * (rectangle1.bottom_right.x - rectangle1.top_left.x)


# Part 6
#The function inputs a name and the list of all books. A loop goes through every index in the list full of
# Book class objects and checks if one of the authors name matches an author. If it does, it appends the title
#of the book to the new list and returns that list
def books_by_author(name:str,books: list):
    lista = []
    for i in books:
        for a in range(len(i.authors)):
            if name in i.authors[a]:
                lista.append(i.title)
    return lista


# Part 7
#it inputs an object from the rectangle class and it uses the top left and the bottom right points to calculate
#both the distance between the points /2 (aka the radius) and the ceter point. It then returns a Circle class
#object that includes a Point class point (the center) and the radius.
def circle_bound(rectangle):
    diameter = ((rectangle.top_left.y - rectangle.bottom_right.y)**2 + (rectangle.bottom_right.x - rectangle.top_left.x)**2)**0.5
    radius = diameter/2
    center_y = rectangle.top_left.y - (rectangle.top_left.y - rectangle.bottom_right.y)/2
    center_x = rectangle.bottom_right.x - (rectangle.bottom_right.x - rectangle.top_left.x)/2
    return data.Circle(data.Point(center_x,center_y), radius)


main()

# Part 8
#The function input is a list of employees, which is an employee class object. The function calculates the average
#pay and who has a wage under the average. They are inputted into a new list and they are returned as a list of
#names.
def below_pay_average(employees:list)->list:
    lista = []
    sum = 0
    for i in range(len(employees)):
        sum += employees[i].pay_rate
    average = sum / len(employees)
    for i in range(len(employees)):
        if employees[i].pay_rate < average:
            lista.append(employees[i].name)
    print("Average:",average)
    return lista



