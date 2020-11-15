# importing the collections
import collections


def run_length_encoding(string):
    # diccionario con los símbolos de la string
   dicc = collections.OrderedDict.fromkeys(string, 0)

   for char in string:
      # + 1 cada vez que aparece ese carcater en la string
      dicc[char] += 1
   encoded_string = ""
   # recorremos el diccionario según el símbolo (key) y el número de veces que aparece (value)
   for key, value in dicc.items():
       # pasamos el enetero(int) a tipo string(str) para crear el output con la string resultante
      encoded_string += key + str(value) # Ejemplo: dicc = "{'w':4}" output = w4

   return (encoded_string)


# creamos la string a codificar
string = "F.C.BBBBaaaarccceellooonnaa"
# llamamos a la funcion
print("\nString: ", string, "\n\nRun length encoding resutl: ",run_length_encoding(string), "\n")
