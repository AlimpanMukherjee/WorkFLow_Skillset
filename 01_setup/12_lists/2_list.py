marks=[7,5,6,8,0]

print(marks)
marks.append(34)  #add 34 at the end of the list
print(marks)

marks.pop(2)   #pop element at the given index
print(marks)

marks.insert(1,98)  #insert 98 at the index 1
print(marks)

extra_marks=[9,56,87]
marks.extend(extra_marks)  #will add the list extra_marks with the list marks
print(marks)

marks.sort()  #sort the entire list
print(marks)

extra_marks.reverse()  #reverses the entire list
print(marks)

marks.remove(9)  #removes the element 9
print(marks)