import Pyro5.api

#uri = "PYRO:obj_829bcf9ace7547ba9488f76437a72030@localhost:62022"
#o = Pyro5.api.Proxy(uri)
o = Pyro5.api.Proxy("PYRONAME:HelloWorld")
print(o.ola_mundo(f'Fulano'))