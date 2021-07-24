def calculate(book_name):
    result = book_name[0] + str(len(book_name))
    return result

def parseFile(file):
    return file.read().splitlines()

file = open("books.txt", "r")
books_list = parseFile(file)
for book_name in books_list:
    result = calculate(book_name)
    print(result)

file.close()
