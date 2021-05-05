import Pyro5.api

address = ("localhost",1234)
destiny = f'PYRO:black_jack21@{address[0]}:{address[1]}'

player_name = input("Nome do Jogador: ")
rival_name = input("Nome do Rival: ")

o = Pyro5.api.Proxy(destiny)

print(o.the_game(player_name,rival_name))

