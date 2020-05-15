import pokebase as pb

for i in range(1, 50):
    pokemon = pb.pokemon(i)
    print(str(pokemon) + ' is ' + str(pokemon.height) + ' feet tall and ' + str(pokemon.weight) + ' kg')