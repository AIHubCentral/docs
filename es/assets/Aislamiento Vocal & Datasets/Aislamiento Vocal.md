``Última actividad: Feb 11, 2024``  

***
###### ‎
:::content-center
## Introducción
:::     
- Un programa de aislamiento de voz es un software diseñado para extraer las vocales de una persona en un archivo de audio, usualmente mediante el uso de modelos de IA.

- Pueden remover sonidos indeseados, como ruido de fondo, reverberación, eco, música, etc.

- El objetivo de tener una muestra de audio con vocales limpias, que es lo que RVC necesita para dar los resultados más precisos.

- Para usuarios de RVC, **las dos mejores aplicaciones son:** 
    {.list-icon}
    - ##### :icon-device-desktop: ‎ [<u>Ultimate Vocal Remover 5</u>](https://aihubdocs.github.io/es/aislamiento-vocal--datasets/aislamiento-vocal/#ultimate-vocal-remover-5)       
    - ##### :icon-cloud: ‎ [<u>MVSEP</u>](https://aihubdocs.github.io/es/aislamiento-vocal--datasets/aislamiento-vocal/#mvsep)
***
<img src="../uvrmvsep-img/a.jpg" alt="image" width="" height="auto">‎       
‎       
:::content-center
## Ultimate Vocal Remover 5
###### ‎  
:::
- UVR es considerado la mejor app de aislamiento vocal gratis. Contiene una interfaz simple & conveniente, y es de código abierto.

- Tiene una gran cantidad de modelos para extraer básicamente casi todo de un audio/canción.         
           
- Este es el programa que usuarios de RVC locales usan por defecto, para ya sea limpiar muestras o <u>[datasets](https://aihubdocs.github.io/es/aislamiento-vocal--datasets/datasets/)</u>.

!!!warning
*Requerirás buenas <u>[specs](https://aihubdocs.github.io/es/otro/glosario/#specs)</u> & <u>[GPU](https://aihubdocs.github.io/es/otro/glosario/#gpu)</u> para correrlo efectivamente. Sino, usa **<u>[MVSEP](https://aihubdocs.github.io/es/aislamiento-vocal--datasets/aislamiento-vocal/#mvsep)**</u>.*
!!!
***
:::content-center
###### ‎  
### <u> Instalación</u> ‎ :icon-download:    
:::
###### ‎    
1. Ve a su [<u>página oficial</u>](https://ultimatevocalremover.com/) y presiona `Download UVR`.  

    <img src="../uvrmvsep-img/b.jpg" alt="image" width="" height="auto">   
***
2. Te redirigirá a su página de GitHub. Toca el link de descarga correspondiente para tu **sistema operativo**.     
UVR está disponible en Windows & Mac.
***
3. Cuando el instalador termine de descargarse, ejecútalo.      
Asegúrate de marcar `🗹 Create a desktop shortcut` para crear un acceso directo.

    <img src="../uvrmvsep-img/c
    .jpg" alt="image" width="500" height="auto"> 
***
:::content-center
###### ‎       
### <u> Cómo Usar</u> ‎ :icon-checklist:
###### ‎       
!!!success <u>NOTAS:</u>
Toca [<u>aquí</u>](https://www.reddit.com/media?url=https%3A%2F%2Fpreview.redd.it%2Fpmi3ialjjca91.png%3Fwidth%3D1016%26format%3Dpng%26auto%3Dwebp%26s%3D0e75311422270753ebca68fe00eaf9ce6a81218b) para una explicación gráfica en inglés de los botones. Aviso: el post está desactualizado.      

Si te topas con un problema, lee el capítulo <u>[Solución de Problemas](https://aihubdocs.github.io/es/aislamiento-vocal--datasets/aislamiento-vocal/#soluci%C3%B3n-de-problemas--)</u>.
!!!
:::

###### ‎         
- ##### Para extraer & limpiar vocales de una <u>canción</u>, lee la guía `Extracción & Limpieza`.

- ##### Para solamente limpiar vocales, lee `Solo Limpieza`. 

+++ Extracción & Limpieza 🎶  
###### ‎     
#### 1. Selecciona el audio.  
- Toca `Select input` y seleccionar tu audio/s.     
O simplemente arrástralos hacia la casilla.  

- En `Select output` selecciona en qué carpeta saldrán los resultados.    

    <img src="../uvrmvsep-img/d
.jpg" alt="image" width="300" height="auto">         ‎    

!!!success 
Para mejores resultados, usa un audio en un [<u>formato sin pérdida</u>](https://aihubdocs.github.io/es/recursos-de-rvc/formato-de-audio--sample-rate//) (**WAV** o **FLAC**), no MP3.
!!!
***
###### ‎ 
#### 2. Selecciona FLAC & GPU Conversion. 
a. A la derecha podrás seleccionar el formato de salida del audio.       
Recomendamos `FLAC` siempre. Aprende más [<u>aquí</u>](https://aihubdocs.github.io/es/recursos-de-rvc/formato-de-audio--sample-rate//).    

b. Si tu <u>[GPU](https://aihubdocs.github.io/es/otro/glosario/#gpu)</u> es **compatible con [<u>CUDA</u>](https://aihubdocs.github.io/es/otro/glosario/#cuda)**, activa `GPU Conversion` para un proceso más rápido.    

    <img src="../uvrmvsep-img/e.png" alt="image" width="350" height="auto">‎      
‎       
>Este paso no es obligatorio, pero recomendado para mejores resultados.
***
###### ‎   
#### 3. Extrae vocales. 
a. A la izquierda, en `Process Method` selecciona `MDX-Net`.        

b. En `Select MDX-Net Model`, selecciona el modelo `MDX23C`.   

    <img src="../uvrmvsep-img/f.jpg" alt="image" width="250" height="auto">‎      
###### ‎   
b. Ahora toca `Start Processing` para que empiece a procesar.        
‎     
!!!success <u>TIP:</u> 
Para testear modelos/opciones, recomiendo activar `Sample Mode`.       
Esto procesará solo `30` segundos de tu audio, y podrás testear más eficientemente.
!!!     
***
###### ‎
#### 4. Remueve reverberación.    
Normalmente las canciones incluyen reverb. en las vocales. Estas afectan **negativamente** los resultados en RVC, así que conviene removerlas. 
 
a. En UVR, selecciona el audio de las vocales.      
   
b. En `Process Method`, selecciona `VR Architecture`, & elige el modelo `DeEcho-DeReverb`.      
  
c. Activa `No Reverb Only` & pon `Window Size` en `320`. (Opcional)     
    Un menor Window Size brindará resultados de mayor **calidad**, pero **tardará** más en procesar.  
    
d. Empieza a procesar.

    <img src="../uvrmvsep-img/g.png" alt="image" width="380" height="auto">‎  

   
***
###### ‎
#### 5. Extrae vocales principales. 
Al igual que con la reverb., las vocales suelen incluir <u>[coros](https://aihubdocs.github.io/es/otro/glosario/#coro)</u> también.

a. Selecciona las vocales sin reverb.   

b. Elige el modelo `UVR-BVE`.         
   
c. Si quieres un audio aparte de solo el coro, asegúrate que `Vocals Only` esté desactivado.

d. Empieza a procesar. Y eso será todo.     
Si luego notas ruido de fondo, pasa el audio por modelo ``UVR-DeNoise``.

    <img src="../uvrmvsep-img/h.png" alt="image" width="230" height="auto">

!!!warning Para los mejores resultados, sigue el orden con el que explicó:       
Extrae vocales -> Quita reverb -> Extrae vocales principales -> Quita ruido
!!!  
***
:::content-center
[!button variant="danger" corners="pill" icon="heart-fill" iconAlign="right" text="Apoyar UVR"](https://www.buymeacoffee.com/uvr5)
:::     

+++ Solo Limpieza 🗣️   

###### ‎     
#### 1. Selecciona el audio.  
- Toca `Select input` y seleccionar tu audio/s.     
O simplemente arrástralos hacia la casilla.  

- En `Select output` selecciona en qué carpeta saldrán los resultados.    

    <img src="../uvrmvsep-img/d
.jpg" alt="image" width="300" height="auto">         ‎    

!!!success 
Para mejores resultados, usa un audio en un [<u>formato sin pérdida</u>](https://aihubdocs.github.io/es/recursos-de-rvc/formato-de-audio--sample-rate/) (**WAV** o **FLAC**), no MP3.
!!!
***
###### ‎ 
#### 2. Selecciona FLAC & GPU Conversion. 
a. A la derecha podrás seleccionar el formato de salida del audio.       
Recomendamos `FLAC` siempre. Aprende más [<u>aquí</u>](https://aihubdocs.github.io/es/recursos-de-rvc/formato-de-audio--sample-rate/).    

b. Si tu <u>[GPU](https://aihubdocs.github.io/es/otro/glosario/#gpu)</u> es **compatible con [<u>CUDA</u>](https://aihubdocs.github.io/es/otro/glosario/#cuda)**, activa `GPU Conversion` para un proceso más rápido.    

    <img src="../uvrmvsep-img/e.png" alt="image" width="350" height="auto">‎      
‎       
>Este paso no es obligatorio, pero recomendado para mejores resultados.
***
###### ‎  
#### 3. Selecciona modelo.   
a. En `Process Method` selecciona `VR`.  

b. Pon `Window Size` en `320`. (Opcional)     
    Un menor Window Size brindará resultados de mayor **calidad**, pero **tardará** más en procesar.  

b. Ve la <u>[lista de modelos](https://aihubdocs.github.io/es/aislamiento-vocal--datasets/aislamiento-vocal/#mejores-modelos-de-uvr--)</u> & en `Select VR Model` selecciona el modelo según lo que necesites quitar/extraer.        
‎       
Si tienes que quitar más de una cosa, sigue este orden:       
``Quita reverb -> Extrae vocales principales -> Quita ruido``      
‎       
!!!success <u>TIP:</u>
Para testear modelos/opciones, recomiendo activar `Sample Mode`.       
Esto procesará solo `30` segundos de tu audio, y podrás testear más eficientemente.
!!! 

***
###### ‎  
#### 4. Procesa.
Toca `Start processing` abajo. Y eso será todo.

     
***
:::content-center
[!button variant="danger" corners="pill" icon="heart-fill" iconAlign="right" text="Apoyar UVR"](https://www.buymeacoffee.com/uvr5)
:::     
+++
‎      
:::content-center
### <u>Mejores Modelos de UVR</u> ‎ :icon-star-fill:
#### ``Sus modelos más convenientes, orientados a RVC.``
:::
###### ‎

Extracción | Process Method | Modelo
:---: | :---: | :---:
Vocales/Instrumental | MDX-Net | MDX23C
Reverberación | VR | DeEcho-DeReverb
Vocales Principales | VR | UVR-BVE
Ruido | VR | UVR-DeNoise 
***
:::content-center
‎  
### <u>Solución de Problemas</u> ‎ :icon-tools:
:::
###### ‎ 
==- *No me aparece el modelo.*
###### ‎   
- Toca la llave inglesa (🔧) a la izquierda, y ve a `Download Center`
- Selecciona la categoría del modelo (MDX-NET o VR)
- Despliega la barra, selecciona el modelo que necesites, & dale al botón de descarga (📥)
- El modelo se descargará, lo que tomará unos minutos
===

==- *UVR extrajo poco/no lo suficiente.*
###### ‎  
- Modifica el valor de `Aggression Setting` a la derecha. Este determina la profundidad de la extracción.
- Un valor mayor la profundizará, y uno menor la suavizará.
===
###### ‎
***     
:::content-center 
#### ‎
<img src="../uvrmvsep-img/i.png" alt="image" width="400" height="auto">

###### ‎       
## MVSEP
###### ‎     
:::
- MVSEP es un sitio web para aislamiento vocal que funciona como UVR, usando modelos de IA.

- No tiene todos los modelos & opciones que UVR tiene, pero si las suficientes herramientas para vocales decentes para RVC.

- Es una de las mejores alternativas en la nube para UVR.
***
:::content-center
‎  
### <u>Cómo Usar</u> ‎ :icon-checklist:
:::
###### ‎ 
!!! <u>AVISO:</u>
***Para usuarios gratis***, solo puedes convertir 1 audio a la vez, y no puedes usar audios de más de 10 minutos. Recórtalo en varios audios si ese es tu caso.

***Si te topas con un problema***, lee el capítulo de <u>[Solución de Problemas](https://aihubdocs.github.io/es/aislamiento-vocal--datasets/aislamiento-vocal/#soluci%C3%B3n-de-problemas---1)</u>.
!!!
###### ‎         
- ##### Para extraer & limpiar vocales de una <u>canción</u>, lee la guía `Extracción & Limpieza`.

- ##### Para solamente limpiar vocales, lee `Solo Limpieza`. 

+++ Extracción & Limpieza 🎶
###### ‎     
#### 1. Inicia sesión.    
a. Primero, crea una cuenta [<u>aquí</u>](https://mvsep.com/register).      

b. Una vez que inicies sesión, ve a la [<u>página de inicio</u>](https://mvsep.com).

!!!
Iniciar sesión no es obligatorio, pero recomendado para un menor tiempo de espera.
!!!
***
###### ‎
#### 2. Selecciona audio. 
En la casilla del medio, toca `Examinar archivo` & selecciona tu audio. Luego empezará a cargarse.     
(o simplemente arrastra el archivo hacia la casilla)    

<img src="../uvrmvsep-img/j.png" alt="image" width="330" height="auto">‎    
    
***
###### ‎
#### 3. Extrae vocales.
a. En `Tipo de separación`, selecciona `MDX23C`.      

b. En `Codificación de salida` selecciona `FLAC`.      
Siempre recomendamos usar FLAC. Aprende más [<u>aquí</u>](https://aihubdocs.github.io/es/recursos-de-rvc/formato-de-audio--sample-rate/).

c. Cuando el audio termine de cargarse, toca `Separar`

    <img src="../uvrmvsep-img/k.png" alt="image" width="400" height="auto">‎   

!!! No cambies "Model type".
!!!
***
###### ‎
#### 4. Descarga el audio.       
Cuando termine la conversión, te redirigirá a una página en la que puedes escuchar los resultados.   
a. Toca los tres botones del audio de **Vocals** y luego `Descargar`.    

b. Haz lo mismo con el audio de `Instrumental` si lo deseas conservar.

    <img src="../uvrmvsep-img/l.png" alt="image" width="400" height="auto">‎   
***
###### ‎
#### 5. Remueve reverb.        
Normalmente las canciones incluyen reverb en las vocales. Estas afectan **negativamente** los resultados en RVC, así que conviene removerlas. 

a. Ve a la página principal y sube las vocales.

b. En `Tipo de separación` selecciona `Ultimate Vocal Remover HQ`.

c. En `Model Type` selecciona el modelo `UVR-DeEcho-DeReverb`.
d. Toca `Separar` & luego descarga las vocales sin reverb.

    <img src="../uvrmvsep-img/m.png" alt="image" width="420" height="auto">‎   

***
###### ‎
#### 6. Extrae vocales principales.  
Al igual que con el reverb., las canciones suelen incluir <u>[coros](https://aihubdocs.github.io/es/otro/glosario/#coro)</u>, que afectan los resultados en RVC.

a. Ve a la página principal & sube el audio sin reverb.

b. En `Tipo de separación` selecciona `Ultimate Vocal Remover HQ`.      

c. Selecciona el modelo `UVR-BVE-4B_SN-44100-1`.

c. Y finalmente toca `Separar` & descarga las vocales principales. También el coro si lo deseas conservar.   

    <img src="../uvrmvsep-img/n.png" alt="image" width="420" height="auto">‎   
    ‎     

e. Si luego notas que tiene ruido, usa el modelo ``UVR-DeNoise``

!!!warning Para los mejores resultados, sigue el orden con el que explicó:       
Extrae vocales -> Quita reverb -> Extrae vocales principales -> Quita ruido
!!! 
***
:::content-center
[!button variant="danger" corners="pill" icon="heart-fill" iconAlign="right" text="Apoyar MVSEP"](https://mvsep.com/billing)
:::

+++ Solo Limpieza 🗣️   
###### ‎     
#### 1. Inicia sesión.    
a. Primero, crea una cuenta [<u>aquí</u>](https://mvsep.com/register).      

b. Una vez que inicies sesión, ve a la [<u>página de inicio</u>](https://mvsep.com).

!!!
Iniciar sesión no es obligatorio, pero recomendado para un menor tiempo de espera.
!!!
***
###### ‎
#### 2. Selecciona audio & formato de salida. 
a. En la casilla del medio, toca `Examinar archivo` & selecciona tu audio. Luego empezará a cargarse.     
(o simplemente arrastra el archivo hacia la casilla)    

    <img src="../uvrmvsep-img/j.png" alt="image" width="330" height="auto">‎    
‎   
b. En `Codificación de salida` selecciona `FLAC`.      
Siempre recomendamos usar FLAC. Aprende más <u>[aquí](https://aihubdocs.github.io/es/recursos-de-rvc/formato-de-audio--sample-rate/)</u>.
***
###### ‎
#### 3. Selecciona modelo.  
a. En `Tipo de separación`, selecciona `Ultimate Vocal Remover 5 HQ`.

b. Ve la <u>[lista de modelos](https://aihubdocs.github.io/es/aislamiento-vocal--datasets/aislamiento-vocal/#mejores-modelos-de-mvsep--)</u> & en `Model Type` selecciona el modelo según lo que necesites quitar/extraer.       
‎       
    Si tienes que quitar más de una cosa, sigue este orden:       
``Quita reverb -> Extrae vocales principales -> Quita ruido``     
*** 
###### ‎
#### 4. Descarga el audio.    
a. Cuando el audio termine de cargarse, toca `Separar`. Tras un rato te redirigirá a la página donde puedes escuchar los resultados.

b. Toca los 3 puntos del audio que necesites y luego `Descargar`. Y eso será todo. 

    <img src="../uvrmvsep-img/l.png" alt="image" width="400" height="auto">‎   
***
:::content-center
[!button variant="danger" corners="pill" icon="heart-fill" iconAlign="right" text="Apoyar MVSEP"](https://mvsep.com/billing)
:::

+++
‎   
‎       
:::content-center
### <u>Mejores Modelos de MVSEP</u> ‎ :icon-star-fill: 
#### ``Sus modelos más convenientes, orientados a RVC.``
:::
###### ‎       

Extracción | Tipo de separación | Modelo
:---: | :---: | :---:
Vocales/Instrumental | MDX23C | - 
Reverberación | Ultimate Vocal Remover 5 HQ | UVR-DeEcho-DeReverb
Vocales Principales | Ultimate Vocal Remover 5 HQ | UVR-BVE-4B_SN-44100-1
Ruido | Ultimate Vocal Remover 5 HQ | UVR-DeNoise

***
:::content-center
‎  
### <u>Solución de Problemas</u> ‎ :icon-tools:
:::
###### ‎ 

==- *MVSEP extrajo poco/no lo suficiente.*
###### ‎ 
- Seleccionando el ***Tipo de separación*** `Ultimate Vocal Remover HQ`, modifica el valor de `Aggressiveness`. Este determina la profundidad de la extracción.
- Un valor mayor la profundizará, y uno menor la suavizará.
===
###### ‎ 
***
:::content-right
`Escrito por Julia`
:::
‎     
:::content-right
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Envíanos Ideas"](https://forms.gle/Q1WX8AxWkH2vuMRd9)
:::
‎     
‎     
***
