from Sistema_Combate import Pokemon
import json

pokemon_1 = Pokemon(1,'Pikachu',15,20,2,3,2,1,5)
pokemon_1.movimiento_1('Impactrueno',40,100,48,'Electrico','Especial')
pokemon_1.movimiento_2('Cola Férrea',100,75,24,'Acero','Fisico')
pokemon_1.movimiento_3('Encanto',0,100,32,'Hada','Estado')
pokemon_1.movimiento_4('Ataque Rapido',40,100,48,'Normal','Fisico')

pokemon_2 = Pokemon(2,'Kirlia',15,35,1,2,4,3,3)
pokemon_2.movimiento_1('Brillo Mágico',80,100,10,'Hada','Especial')
pokemon_2.movimiento_2('Paz Mental',0,0,20,'Psiquico','Estado')
pokemon_2.movimiento_3('Bola Sombra',80,100,15,'Fantasma','Especial')
pokemon_2.movimiento_4('Divide Dolor',0,0,20,'Normal','Estado')



pokemon_1_dict = pokemon_1.to_dict()

pokemon_2_dict = pokemon_2.to_dict()


batalla =  [pokemon_1_dict, pokemon_2_dict]

ruta_json = r"batalla3.json"

with open(r"batalla3.json", "w") as a:
      json.dump(batalla, a)


with open(ruta_json, 'r') as json_a:
    cargar_datos = json.load(json_a)

    print(cargar_datos)
