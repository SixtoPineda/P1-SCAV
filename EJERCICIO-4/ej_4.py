# importing the collections
import collections


def run_length_encoding(string):
   # Generamos el diccionario con los símbolos que aparecen el la string
   # Ejemplo: string = 'wwwwaaadexxxxxx' entonces dicc = "{'w':0, 'a':0, 'd':0, 'e':0, 'x':0}"
   dicc = collections.OrderedDict.fromkeys(string, 0)
   # Ahora iteramos a través del input, la string
   # y miramos con que frecuencia aparece cada símbolo
   # Ejemplo: string = 'wwwwaaadexxxxxx' entonces dicc = "{'w':4,'a':3,'d':1,'e':1,'x':6}"
   for char in string:
      # + 1 cada vez que aparece ese carcater en la string
      dicc[char] += 1
   # creamos el output
   encoded_string = ""
   # recorremos el diccionario según el símbolo (key)
   # y el número de veces que aparece (value)
   for key, value in dicc.items():
       # pasamos el enetero(int) a tipo string(str) para crear el output
       # con la string resultante
      encoded_string += key + str(value) # Ejemplo: dicc = "{'w':4}" output = w4

   return (encoded_string)


# creamos la string a codificar
string = "wwwwaaadexxxxxx"
# llamamos a la funcion
print("\nString: ", string, "\n\nRun length encoding resutl: ",run_length_encoding(string), "\n")
