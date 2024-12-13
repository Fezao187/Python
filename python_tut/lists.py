##Lists
names = ['Kristine', 'Katlego', 'andNem']
print(names)
print(names[0])
print(names[-1]) # Last element in list
names[2]="Wildheart"
print(names)
print(names[0:2])

### List methods
numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.append(6)
print(numbers)
numbers.insert(0, 0)
print(numbers)
numbers.remove(3)
print(numbers)
print(1 in numbers)
print(len(numbers))
numbers.clear()
print(numbers)