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

# creamos los tres valores RGB para pasar a YUV
rgb = np.array([255, 255, 255])
y, u, v = RGB2YUV(rgb)
print("\nRGB(255,255,255), en YUV: Y = ", "{:.1f}".format(y), "U = ","{:.1f}".format(u),"V = ", "{:.1f}".format(v) )

# a modo de comprobación pasamos el output YUV de los valores RGB creados a la función que convierte el YUV en RGB
yuv = np.array([y, u, v])
r, g, b= YUV2RGB(yuv)
print("\nYUB(","{:.1f}".format(y),",",u,",",v,"), en RGB: R = ", "{:.1f}".format(r), "  G = ","{:.1f}".format(g),"  B = ", "{:.1f}".format(b),"\n" )

```
![](https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-1/result.png)
> Resultado.


### EJERCICIO-2
#### ***Resize Images***

Dado que habia que hacer un *resize*, con el fin de reducir la calidad, busqué un comando para poder acceder a *ffmpeg* desde el terminal y poder aplicar una reducción de tamaño de una imagen y así obtener el resultado pedido. Para ello usé el comando encontrado en la página de **FFmpeg:** *https://trac.ffmpeg.org/wiki/Scaling*.
A continuación muestro los resultados. Yo decidí redimensionar la imagen a un tamaño de 100x100, asegurándome una reducción de calidad.
##### **Comando + Terminal**
<p align="center">
  <img align="center" src="https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-2/comandos_ejercicio_2.png" width="400"/>
</p>

##### **Resultados**

<p align="center">
  <img src="https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-2/original.png" width="900">
  <img src="https://github.com/SixtoPineda/P1-SCAV/blob/main/EJERCICIO-2/original_100x100.png" width="400">
</p>



### EJERCICIO-3
### EJERCICIO-4
### EJERCICIO-5
