import Pyro5.api

@Pyro5.api.expose
class OlaMundo(object):
    def ola_mundo(self,name):
        return f'Ola Mundo para {name}\n'

daemon = Pyro5.api.Daemon()
ns = Pyro5.api.locate_ns()
uri = daemon.register(OlaMundo)
print("Ready. Object uri =", uri)
ns.register("HelloWorld",uri)
daemon.requestLoop()