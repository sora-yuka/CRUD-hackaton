from views import *
from time import sleep

def main():
    while True:
        print("Function:\n"
              "1 - get all products,\n"
              "2 - get one product,\n"
              "3 - create product,\n"
              "4 - update product,\n"
              "5 - delete product,\n"
              "0 - exit")
        method = input("\nenter the number: ")
        if method == "1":
            print(product_listing(),"\n")
            sleep(2)
        elif method == "2":
            id = int(input("enter the id: "))
            print(product_retrieve_listing(id),"\n")
            sleep(2)
        elif method == "3":
            print(product_creating(),"\n")
            sleep(2)
        elif method == "4":
            id = int(input("enter the id: "))
            print(product_updateting(id),"\n")
            sleep(2)
        elif method == "5":
            id = int(input("enter the id: "))
            print(product_destroying(id),"\n")
            sleep(2)
        elif method == "0":
            print("Good bye my friend.")
            break
        else:
            print("No such method","\n")

if __name__ == "__main__":
    print("Hello, welcome to my CRUD, below are the available method...", "\n")
    main()