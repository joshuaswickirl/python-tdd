def calculate(book_name):
    result = book_name[0] + str(len(book_name))
    return result

file = open("books.txt", "r")

lines = file.readlines()
for line in lines:
    book_name = line[0:len(line)-1]
    result = calculate(book_name)
    print(result)

file.close()
