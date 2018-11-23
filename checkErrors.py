import openRead

if __name__ == '__main__':
    text = openRead.read()
    how_many = openRead.how_many(text)
    list_of_errors = openRead.print_errors(how_many,text,"<Error>","</Error>")
    print(text)
    print(how_many)
    print(list_of_errors)