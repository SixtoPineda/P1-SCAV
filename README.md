# ***SCAV: P1-JPEG***

## **EJERCICIOS**

### EJERCICIO-1
#### ***RGB-&-YUV***

<p align="justify">Para realizar este ejercicio me basé en los cálculos propuestos por la diapositiva 40 de la teoria 2 sobre MPEG y MPEG-2.<br>
Únicamente pasamos el valor RGB o YUV a la función, según la conversión que queramos realizar y dentro realizamos los cálculos necesarios para obtener la conversión correctamente. Finalmente las funciones devuelven la array con el resultado correspondiente.</p>

<p align="center">
  <img src="https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-1/rgb_yuv.png" width="600" title="Diapo 40, teoría 2 (MPEG y MPEG-2)">
</p>

```python
import numpy as np

def RGB2YUV(rgb):

    #sacado de la diapositiva 40 de la teoria T2 MPEG y MPEG-2
    Y =  0.257 * rgb[0] + 0.504 * rgb[1] + 0.098 * rgb[2] +  16
    U = -0.148 * rgb[0] - 0.291 * rgb[1] + 0.439 * rgb[2] + 128
    V =  0.439 * rgb[0] - 0.368 * rgb[1] - 0.071 * rgb[2] + 128

    return Y,U,V

def  YUV2RGB(yuv):

    #sacado de la diapositiva 40 de la teoria T2 MPEG y MPEG-2
    r =  1.164 * (yuv[0] - 16) + 2.018 * (yuv[1] - 128)
    g =  1.164 * (yuv[0] - 16) - 0.813 * (yuv[2] - 128) - 0.391 * (yuv[1] - 128)
    b =  1.164 * (yuv[0] - 16) + 1.596 * (yuv[2] - 128)

    return rgb

```
![](https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-1/result.png)
> Resultado.

<p align="justify">Como podemos ver en el resultado, el proceso es correcto, puesto que en pasar de RGB a YUV obtenemos unos valores que en realizar la función inversa obtenemos el valor RGB previamente creado.</p>

### EJERCICIO-2
#### ***Resize Images***

<p align="justify">Dado que había que hacer un <em>resize</em>, con el fin de reducir la calidad, busqué un comando para poder acceder a <em>ffmpeg</em> desde el terminal y poder aplicar una reducción de tamaño de una imagen y así obtener el resultado pedido. Para ello usé el comando encontrado en la página de <em><strong>FFmpeg:</strong></em> <em>https://trac.ffmpeg.org/wiki/Scaling</em> -> "<em>ffmpeg-i original.png -vf scale=100:100 original_100x100.png</em>"</p>
<p align="justify">A continuación muestro los resultados. Yo decidí redimensionar la imagen a un tamaño de 100x100, asegurándome una reducción de calidad.</p>

##### **Comando + Terminal**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-2/comandos_ejercicio_2.png" width="400"/>
</p>

##### **Resultados**

<p align="center">
  <img src="https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-2/original.png" width="500">
  <img src="https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-2/original_100x100.png" width="250">
</p>

<p align="justify">En el resultado claramente se ve como la imagen final (derecha) tiene una peor calidad, hemos bajado su resolución.</p>

### EJERCICIO-3
#### ***Image into b/w***

<p align="justify">De igual modo que en el caso anterior, busqué en internet qué comando nos permitía usar <em>ffmpeg</em> para poder binarizar la imagen con color blanco y negro tal y como se pedía en el enunciado b/w (black/white). Para ello utilizé el comando que hacía referencia a un filtro llamado <em>threshold</em> que permite binarizar la imagen: <em>https://ffmpeg.org/ffmpeg-filters.html#threshold</em> -> "<em>ffmpeg -i 320_240_original.png -f lavfi -i color=gray -f lavfi -i color=black -f lavfi -i color=white -lavfi threshold b_w.png</em>"</p>
<p align="justify">A continuación muestro los resultados: </p>

##### **Comando + Terminal**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-3/ejercicio_3.png" width="400"/>
</p>

##### **Resultados**

<p align="center">
  <img src="https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-3/320_240_original.png" width="350">
  <img src="https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-3/b_w.png" width="350">
</p>

<p align="justify">Si nos fijamos en la imagen de color, podemos ver que aquellas partes que ésta tiene más claras o blancas son las que se traducen en la imagen b/w en blanco (1). En cambio aquellas que tiene un color más apagado u oscuro, pasan a ser negro (0). Esto se debe al threshold, si de la imagen original el valor de ese pixel esta por encima de un cierto límite pasan a ser 0 o 1.</p>

### EJERCICIO-4
#### ***Run-lenght encoding***

<p align="justify">La codificación de Run-length consiste en detectar los distintos símbolos que aparecen en una serie de bytes y saber cuántas veces aparece cada uno de ellos.<br>Al crear la función, le pasaremos una string con una série de símbolos. A partir de aquí, mediante <em>ollections.OrderedDict.fromkeys(string, 0)</em> procedemos a crear un diccionario con una lista de todos los símbolos que aparecen en la string. Hecho esto pasamos a ver cuántas veces aparece cada uno de esos símbolos de la lista en la string pasada a la función.<br>Por último procedemos a crear el output donde colocaremos el símbolo junto con un valor que hará referencia al número de veces que aparece en la string pasada a la función.</p> <p align="justify">Fuentes:<br>https://www.geeksforgeeks.org/run-length-encoding-python/<br>https://www.tutorialspoint.com/run-length-encoding-in-python</p>

```python
import collections

def run_length_encoding(string):
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

```
![](https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-4/result.png)
> Resultado.

<p align="justify">En el resultado podemos ver como cada vez que aparece un símbolo en la string, este se muestra en el resultado final junto con un valor entero, que hace referencia al número de veces que aparece dicho símbolo en la string.</p>

### EJERCICIO-5
#### ***DCT***

<p align="justify">La DCT (<em>Discrete Cosine Transform</em>) se caracteriza por tener una buena capacidad de concentración o compactación de la energía o la información en pocos coeficientes a diferencia de otros métodos como la DFT. Principalmente lo que hace es separar la imagen en partes con distintas frecuencias y procede a realizar la cuantización donde se realiza una compresión y las frecuencias menos relevantes o importantes son descartadas. Cabe destacar que el algoritmo no cambia los datos que recibe a diferencia de otros algoritmos que sí lo hacen.<br> En python esa función ya está implementada mediante el paquete <em>scipy</em>. Por ello al iniciar el script importamos ambas funciones, la DCT y la IDCT, a más de importar funciones como <em>imread</em> para poder leer la imagen a la que aplicar la DCT.<br>Dado que queremos aplicar la DCT a una imagen (2D), nos encontramos en un espacio bidimensional, por lo tanto, al usar las funciones <em>dct2()</em> y <em>idct2()</em> deberemos aplicar la DCT dos veces, para cada una de las dimensiones.<br>Cargaremos la imegen, le aplicaremos la DCT, la IDCT y posteriormente veremos el resultado final. </p><p align="justify">Fuente:<br>https://stackoverflow.com/questions/7110899/how-do-i-apply-a-dct-to-an-image-in-python</p>



```python
from scipy.fftpack import dct, idct

from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pylab as plt

##################### DCT & IDCT (2D)########################
# 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

# 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

#########################################################


# leemos una imagen RGB y la pasamos a grayscale
im = rgb2gray(imread('EJERCICIO-5/original.png'))
#DCT
im_DCT = dct2(im)
#IDCT
im_IDCT = idct2(im_DCT)

#comprobación de que se asemejan ambas imágenes
assert(np.allclose(im, im_IDCT) == True)

# plot de la imagen original y la reconstruida
plt.gray()
plt.subplot(121), plt.imshow(im), plt.axis('off'), plt.title('Original image', size=20)
plt.subplot(122), plt.imshow(im_IDCT), plt.axis('off'), plt.title('Reconstructed image (DCT+IDCT)', size=20)
plt.show()
```
![](https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-5/Reconstructed_image(DCT%2BIDCT).png)
> Resultado.

<p align="justify">A simple vista no podemos ver o apreciar apenas ningún cambio, a más de que en realizar una comparación entre el resultado y la imagen original podemos ver que no estan muy lejos entre ellas. </p>
