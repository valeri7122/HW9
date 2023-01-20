import connect
from models import Quote
import re


quotes = Quote.objects()

def main():
    while True:
        quote_list = []
        command = input('Enter "command: value" ')
        try:
            command_list = command.split(":")
            tag_list = command_list[1].split(",")

 
            if command_list[0] == "name":
                for q in quotes:
                    if q.author.fullname == command_list[1].strip():
                        quote_list.append(re.sub("[“|”]", "", q.quote))

            if command_list[0] == "tag":
                for q in quotes:
                    if command_list[1].strip() in q.tags:
                        quote_list.append(re.sub("[“|”]", "", q.quote))

            if command_list[0] == "tags":
                for q in quotes:
                    for t in tag_list:
                        if t in q.tags:
                            quote_list.append(re.sub("[“|”]", "", q.quote))
                            break

            if command_list[0] == "exit":
                break

            print(quote_list)

        except:
            print('You entered the wrong command')
            pass


if __name__ == "__main__":
    main()
