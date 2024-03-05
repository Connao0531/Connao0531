import json

class Pokemon:

    def __init__(self,idx,nombre,nivel,ps,ataque,defensa,ataque_esp,defensa_esp,velocidad):

        self.nombre = nombre
        self.idx = idx
        self.nivel = nivel
        self.ps = ps
        self.ataque = ataque
        self.defensa = defensa
        self.ataque_esp = ataque_esp
        self.defensa_esp = defensa_esp
        self.velocidad = velocidad

       

    def calculadora_daño(self,dano):

        return 10
        

    def movimiento_1(self,nombre,poder,precision,pp,tipo,clase):

        self.movimiento_1_data = {
            
          'nombre' :nombre,
          'precision' : precision,
          'poder' : poder,
          'pp' : pp,
          'tipo' : tipo,
          'clase' : clase,

        }
    def movimiento_2(self,nombre,poder,precision,pp,tipo,clase):

       self.movimiento_2_data = {
            
          'nombre' : nombre,
          'precision' : precision,
          'poder' : poder,
          'pp' : pp,
          'tipo' : tipo,
          'clase' : clase,

        }

    def movimiento_3(self,nombre,poder,precision,pp,tipo,clase):

       self.movimiento_3_data = {
            
          'nombre' : nombre,
          'precision' : precision,
          'poder' : poder,
          'pp' : pp,
          'tipo' : tipo,
          'clase' : clase,

        }

    def movimiento_4(self,nombre,precision,poder,pp,tipo,clase):

      self.movimiento_4_data = {
            
          'nombre' : nombre,
          'precision' : precision,
          'poder' : poder,
          'pp' : pp,
          'tipo' : tipo,
          'clase' : clase,

        }

    def to_dict(self):

        return {

         'identificador': self.idx,
         'nombre': self.nombre,
         'nivel': self.nivel,
         'ps': self.ps,
         'ataque': self.ataque,
         'defensa': self.defensa,
         'ataque_esp': self.ataque_esp,
         'defensa_esp': self.defensa_esp,
         'velocidad': self.velocidad,
         'movimiento_1': self.movimiento_1_data,
         'movimiento_2': self.movimiento_2_data,
         'movimiento_3': self.movimiento_3_data,
         'movimiento_4': self.movimiento_4_data,

         }

    def from_dict(cls,data):
        return cls(**data)
    
if __name__ == '__main__':
        
        ruta_json = r"batalla3.json"

        with open(ruta_json, 'r') as json_a:
            cargar_datos = json.load(json_a)

        pokemon_1_dict = cargar_datos[0]

        pokemon_2_dict = cargar_datos[1]

        cantidad_dict = 0

        batalla =[pokemon_1_dict, pokemon_2_dict]

        with open(r"batalla3.json", "w") as a:
          json.dump(batalla, a)


        #Cosas varias

        mov_indice = 0
        damage = 0

        

        print("******************************")
        print("* Sistema De Combate Pokémon *")
        print("******************************\n")

        print("*********************")
        print("* Lista De Pokemons *")
        print("*********************\n")

        for indice, pokemon_dict in enumerate(batalla, start=1):
        

            print(f"{indice}. {pokemon_dict['nombre']}")
            

        pokemon_atacante = int(input("\nPor favor, seleccione el numero del pokemon atacante: "))


        for pokemon_dict in batalla:
        
            if pokemon_atacante == pokemon_dict['identificador']:
                               
               print(f"Usted ha elegido a: {pokemon_dict['nombre']} \n")
               resultados = {
                               'pokemon_atacante': pokemon_dict['nombre'],   
                            }

        if pokemon_atacante > indice or pokemon_atacante <= 0:

           print("El pokemon no existe")
           exit()
            

        print("***************")
        print("* Movimientos *")
        print("***************\n")


        
        for pokemon_dict in batalla:
            
            if pokemon_atacante == pokemon_dict['identificador']:
                
                for i in range(1, 5):
                    
                    movimiento_actual = f"movimiento_{i}"
                    
                    if movimiento_actual in pokemon_dict:

                        mov_indice += 1
                        movimiento_name = pokemon_dict[movimiento_actual]['nombre']
                        print(f"{mov_indice}. {movimiento_name}")
                        

        movimiento_seleccionado = int(input("\nPor favor, seleccione el movimiento deseado: "))

        if movimiento_seleccionado > mov_indice or movimiento_seleccionado <= 0:

           print("El movimiento no existe")
           exit()
                    
        movimiento_actual = f"movimiento_{movimiento_seleccionado}"
        
        print(pokemon_dict)

        for pokemon_dict in batalla:
            
            if pokemon_atacante == pokemon_dict['identificador']:
                
                print("Usted ha seleccionado a",pokemon_dict[movimiento_actual]['nombre'])

                resultados['movimiento_seleccionado'] = pokemon_dict[movimiento_actual]['nombre']


        print("\n*********************")
        print("* Lista De Pokemons *")
        print("*********************\n")


        filtro_batalla = filter(lambda pokemon:
            pokemon['identificador'] != pokemon_atacante, batalla)
        
        pokemon_disponible = list(filtro_batalla)

        for indice, pokemon_dict in enumerate(pokemon_disponible, start=1):
            print(f"{indice}. {pokemon_dict['nombre']}")

        pokemon_objetivo = int(input("\nPor favor, selecciona el pokemon objetivo del ataque: "))

        if pokemon_objetivo > indice or pokemon_objetivo <= 0:

           print("El pokemon no existe")
           exit()

        pokemon_dict = pokemon_disponible[pokemon_objetivo - 1]

        print(f"Usted ha elegido a: {pokemon_dict['nombre']}")
        
        resultados['pokemon_objetivo'] = pokemon_dict['nombre']


         

        dado = int(input("\nPor favor, seleccione el resultado de una tirada de un dado de 6 caras: "))

        if dado > 6 or dado <= 0:

           print("\nEl valor del dado tiene que ser entre 1 y 6. No se puede aceptar este valor.")
           exit()
        
        print("\n*********************")
        print("*     Resultados    *")
        print("*********************")

        print("Pokemon atacante:",resultados['pokemon_atacante'])
        print("Movimiento a utilizar:",resultados['movimiento_seleccionado'])
        print("Pokemon objetivo:",resultados['pokemon_objetivo'])
        print("Resultado del dado:",dado)
                
        confirmacion = (input("\nEstas deacuerdo? "))
        confirmacion = confirmacion.lower()

        if confirmacion == "si":

                        print("\n¡Perfecto!\n")

        else:

                        exit()


        for pokemon_dict in batalla:
            
            if pokemon_atacante == pokemon_dict['identificador'] and pokemon_dict[movimiento_actual]['clase'] == 'Fisico':

               damage = pokemon_dict['ataque'] + (pokemon_dict[movimiento_actual]['poder'] // 10) + dado

               print("El daño en bruto es:",damage,"\n")


               filtro_batalla = filter(lambda pokemon:
               pokemon['identificador'] != pokemon_atacante, batalla)
            
               pokemon_disponible = list(filtro_batalla)

               for indice, pokemon_dict in enumerate(pokemon_disponible, start=1):

                   pokemon_dict = pokemon_disponible[pokemon_objetivo - 1]


               true_damage = damage - pokemon_dict['defensa']
 

            elif pokemon_atacante == pokemon_dict['identificador'] and pokemon_dict[movimiento_actual]['clase'] == 'Especial':
    
               damage = pokemon_dict['ataque_esp'] + (pokemon_dict[movimiento_actual]['poder'] // 10) + dado

               print("El daño en bruto es:",damage,"\n")


               filtro_batalla = filter(lambda pokemon:
               pokemon['identificador'] != pokemon_atacante, batalla)
            
               pokemon_disponible = list(filtro_batalla)

               for indice, pokemon_dict in enumerate(pokemon_disponible, start=1):

                   pokemon_dict = pokemon_disponible[pokemon_objetivo - 1]

                   true_damage = damage - pokemon_dict['defensa_esp']


           

 
            #Este 'elif' es para cuando el movimiento seleccionado es de tipo: 'Estado'. Estos son dificiles de tratar,
            #Ya que cada uno es su propio caso de estudio. Esto se podria utilizar para una proxima actualización del programa.
                   
            elif pokemon_atacante == pokemon_dict['identificador'] and pokemon_dict[movimiento_actual]['clase'] == 'Estado':
                
                 exit()



        print(resultados['pokemon_atacante'],"ha atacado a",resultados['pokemon_objetivo'],"con",resultados['movimiento_seleccionado'])
        print("El daño verdadero es:",true_damage)
        
