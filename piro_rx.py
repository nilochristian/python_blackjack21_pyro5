import Pyro5.api

@Pyro5.api.expose
class OlaMundo(object):
    def ola_mundo(self,name):
        return f'Ola Mundo para {name}\n'


Pyro5.api.Daemon.serveSimple({
    OlaMundo: 'HelloWord',
}, host="localhost", port=1234, ns=False)

#*
#daemon = Pyro5.server.Daemon()
#ns = Pyro5.api.locate_ns()
#uri = daemon.register(OlaMundo)
#print("Ready. Object uri =", uri)
#name_server = "HelloWorld"
#ns.register(name_server,uri,True)
#daemon.requestLoop()