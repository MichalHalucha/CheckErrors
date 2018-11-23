import re
def read():
    f = open("log.txt", "r")
    read = f.read()
    f.close()
    return read


def how_many(text):
    return text.count("<Error>")


def print_errors(how_many,text,start_string,end_string):
    error_list = []
    list = [m.start() for m in re.finditer(start_string, text)]
    for i in range(how_many):
        try:
            result = text[list[i]+len(start_string):list[i+1]-len(end_string)]
            error_list.append(result)
        except:
            result = text[list[i]+len(start_string):len(text)-len(end_string)]
            error_list.append(result)
    return error_list