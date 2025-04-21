import Pyro5.api

@Pyro5.api.expose
class HelloService:
    def say_hello(self):
        return "Hello from the Python RMI server!"

def main():
    daemon = Pyro5.api.Daemon()
    uri = daemon.register(HelloService)
    print("Ready. Object URI =", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    main()
