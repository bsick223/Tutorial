# sort() method = used with lists only
# sort() function = used with iterables

students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")

# students.sort(reverse=True)
sorted_students = sorted(students, reverse=True)

for i in sorted_students:
    print(i)