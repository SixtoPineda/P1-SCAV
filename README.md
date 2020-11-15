# ***SCAV: P1-JPEG***

## **EJERCICIOS**

### EJERCICIO-1
#### ***RGB-&-YUV***

Para realizar este ejericio me basé en los cálculos propuestos por la dispositiva 40 de la teoria 2 sobre MPEG y MPEG-2. 
Únicamente pasamos el valor RGB o YUV a la función, según la conversión que queramos realizar y dentro realizamos los cálculos necesarios para obtener la conversión correctamente. Finalmente las funciones devuelven la array con esl resultado correspondiente. 

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


### EJERCICIO-2
#### ***Resize Images***

Dado que habia que hacer un *resize*, con el fin de reducir la calidad, busqué un comando para poder acceder a *ffmpeg* desde el terminal y poder aplicar una reducción de tamaño de una imagen y así obtener el resultado pedido. Para ello usé el comando encontrado en la página de **FFmpeg:** *https://trac.ffmpeg.org/wiki/Scaling* -> "*ffmpeg -i original.png -vf scale=100:100 original_100x100.png*"
<p>A continuación muestro los resultados. Yo decidí redimensionar la imagen a un tamaño de 100x100, asegurándome una reducción de calidad.</p>

##### **Comando + Terminal**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-2/comandos_ejercicio_2.png" width="400"/>
</p>

##### **Resultados**

<p align="center">
  <img src="https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-2/original.png" width="500">
  <img src="https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-2/original_100x100.png" width="250">
</p>



### EJERCICIO-3
#### ***Image into b/w***

De igual modo que en el caso anterior, busqué en internet que comando nos permitía usar *ffmpeg* para poder binarizar la imagen con color blanco y negro tal y como se pedía en el enunciado b/w (black/white). Para ello utilizé el comando que hacía referencia a un filtro llamado *threshold" que permite binarizar la imagen: *https://ffmpeg.org/ffmpeg-filters.html#threshold* -> "*ffmpeg -i 320_240_original.png -f lavfi -i color=gray -f lavfi -i color=black -f lavfi -i color=white -lavfi threshold b_w.png*"
<p>A continuación muestro los resultados: </p>

##### **Comando + Terminal**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-3/ejercicio_3.png" width="400"/>
</p>

##### **Resultados**

<p align="center">
  <img src="https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-3/320_240_original.png" width="350">
  <img src="https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-3/b_w.png" width="350">
</p>

### EJERCICIO-4
#### ***Run-lenght encoding***

<p>La codificación de Run-length consiste en detectar los distintos símbolos que aparecen en una serie de bytes y saber cuantas veces aparece cada uno de ellos.<br>Para a la función le pasamos una string con una série de símbolos. A partir de aquí, mediante <em>ollections.OrderedDict.fromkeys(string, 0)</em> procedemos a crear un diccionario con una lista de todos los símbolos que aparecen en la string. Hecho esto pasamos a ver cuantas veces aparece cada uno de esos símbolos de la lista en la string pasada a la función.<br>Por último procedemos a crear el output donde colocaremos el símbolo junto con un valor que hará referencia al número de veces que aparece en la string pasada a la función.</p> <p>Fuentes:<br>https://www.geeksforgeeks.org/run-length-encoding-python/<br>https://www.tutorialspoint.com/run-length-encoding-in-python</p>

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


### EJERCICIO-5
#### ***DCT***

<p>pssss</p><p>Fuente:<br>https://stackoverflow.com/questions/7110899/how-do-i-apply-a-dct-to-an-image-in-python</p>



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

# plot de la imagen original y la reconstruida
plt.gray()
plt.subplot(121), plt.imshow(im), plt.axis('off'), plt.title('Original image', size=20)
plt.subplot(122), plt.imshow(im_IDCT), plt.axis('off'), plt.title('Reconstructed image (DCT+IDCT)', size=20)
plt.show()
```
![](https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-5/Reconstructed_image(DCT%2BIDCT).png)
> Resultado.
