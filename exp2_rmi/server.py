import Pyro4
@Pyro4.expose
class Calculator:
 def add(self, a, b):
    return a + b
 def multiply(self, a, b):
    return a * b
daemon = Pyro4.Daemon()
uri = daemon.register(Calculator)
print("Server is running...")
print("URI:", uri)
daemon.requestLoop()