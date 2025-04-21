import Pyro5.api

def main():
    uri = input("Enter the object URI: ")
    hello = Pyro5.api.Proxy(uri)
    print(hello.say_hello())

if __name__ == "__main__":
    main()
    
