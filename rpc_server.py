from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    return x + y

server = SimpleXMLRPCServer(("localhost", 8000))
print("RPC Server is running on port 8000...")
server.register_function(add, "add")
server.serve_forever()
