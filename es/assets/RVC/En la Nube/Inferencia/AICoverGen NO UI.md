``Última actividad: Feb 10, 2024`` 
‎  
***
###### ‎  
:::content-center
## Introducción
:::
- AICoverGen NO UI es un port del [<U>fork</U>](http://localhost:5000/otro/glosario/#fork) AICoverGen para [<U>Google Colab</u>](http://localhost:5000/otro/glosario/#google-colab). Cuaderno base hecho por [<u>Ardha27</u>](https://github.com/ardha27).    

- Esta versión (**Eddy's Version**) es una mejora del espacio de Colab original, que trae con menos bugs, mejoras y nuevas opciones. Créditos a Eddy & Raid.

- Por su **rápida** <u>[inferencia](http://localhost:5000/otro/glosario/#inferencia)</u>, automática extracción vocal, y el poder subir audios mediante links de YouTube, es considerado uno de los mejores Colab para inferencia en RVC.  
‎               
### Pros & Contras :icon-tasklist:
==- ***Abrir***
!!!
***Los pros & contras son subjetivos según tus necesidades.***
!!!
||| **✔️ PROS:**       
-  Extracción vocal automática.           
-  Herramienta de mezcla musical.            
-  Opción para añadir reverb.            
-  Incluye Mangio-Crepe.      
-  Descarga de modelos mediante links.               
-  Subida de audio por links de YouTube. 
-  Separara automáticamente los elementos de la canción, & los puedes obtener.
||| **❌ CONTRAS**      
-  Límite de uso para usuarios gratis.                   
-  Toma de 10 a 15 para cargar.       
-  Interfaz no buena.  
-  No hay control de la extracción vocal. Puede dar problemas.
-  Dicha extracción siempre se ejecuta. Perderás tiempo si insertas vocales limpias. 
-  Poco control de la mezcla & reverb. Conviene usar un <u>[EAD](http://localhost:5000/otro/glosario/#ead)</u>.
|||     
===               
***
###### ‎  
:::content-center
## Cómo Usar
:::
###### ‎  
#### 1. <u>Ingresa al espacio</u>      
a. Primero, inicia sesión en Google [<u>aquí</u>](https://accounts.google.com/).     
b. Luego accede al espacio de Colab [<u>aquí</u>](https://www.google.com/url?q=https://colab.research.google.com/drive/1u1brjK8IZt647UsbZuGYfW29oFM2I4tk?usp%3Dsharing&sa=D&source=editors&ust=1704303145687891&usg=AOvVaw3M9tmokG80RXF-GD1LJqCL).    

    <img src="../aicovergen-img/page.png" alt="image" width="500" height="auto">     

***     
‎       
#### 2. <u>Clona e Instala.</u>     
- Ejecuta la celda ``Clone and Install``.     
Esto preparará RVC.      

    <img src="../aicovergen-img/cloneandinstall.png" alt="image" width="280" height="auto">‎         
‎    
- Tomará al rededor de 15 minutos.       
Terminará cuando veas un tick (✔️) en la esquina.        

    <img src="../aicovergen-img/check.png" alt="image" width="370" height="auto">‎
‎         
>No te preocupes si ves texto en rojo, es normal.          

***
‎       
#### 3. <u>Descarga modelo de voz.</u>    
   <img src="../aicovergen-img/model.png" alt="image" width="550" height="auto">‎       
   ‎ 
   a. Ve a la celda `Model Download Function`.        
Pega el link del modelo en la barra de ``url``.     
       

b. En `dir_name` nombra el modelo. No incluyas espacios/caracteres especiales.        
           
c. Luego ejecuta la celda. 

!!!
Los modelos se guardarán hasta que termine la sesión de Colab.  
!!!
***
###### ‎  
#### 4. <u>Inserta el audio</u>      
Ingresa las vocales/canción en la celda `Generate Cover`.     

Tienes dos maneras de hacerlo: usando un **link de YouTube**, o un **archivo de Google Drive**:     

+++ **Link de YouTube**
###### ‎ 
Copia un link de YouTube, y pégalo en la barra ``SONG_INPUT``.

<img src="../aicovergen-img/generatecoveryt.png" alt="image" width="420" height="auto">‎              

+++ **Archivo de Google Drive**    
###### ‎   
a. Debajo de `Generate Cover`, ejecuta `Mount Drive`.      
‎       
     <img src="../aicovergen-img/mountdrive.png" alt="image" width="210" height="auto">‎           

***    
b. Toca `Conectar con Google Drive` y selecciona tu cuenta de Google.   
‎        
    <img src="../aicovergen-img/connect.png" alt="image" width="280" height="auto">‎           
***
c. A la derecha, toca el símbolo de carpeta ( :icon-file-directory: ) en la derecha.  

    Ve a la carpeta ``drive``, luego ``MyDrive``, & ahí estará tu almacenamiento de Google Drive.        
    Localiza tu audio, hazle click-derecho & toca ``Copiar ruta``.       
    ‎       
    <img src="../aicovergen-img/1.png" alt="image" width="320" height="auto">‎       
***    
d. Pega la ruta en la barra `SONG_INPUT`, en la celda `Generate Cover`.    
‎            
    <img src="../aicovergen-img/inputaudio.png" alt="image" width="420" height="auto">
+++

###### ‎  
#### 5. <u>Selecciona el modelo.</u>        
Debajo de este, en ``RVC_DIRNAME`` inserta el nombre que asignaste al modelo anteriormente.

<img src="../aicovergen-img/2.png" alt="image" width="400" height="auto">    

***     
###### ‎   
#### 6. <u>Modifica opciones.</u> (opcional)        
Debajo de ``RVC_DIRNAME`` hasta ``Audio Mixing Options`` encontrarás las [<u>opciones de inferencia</u>](http://localhost:5000/recursos-de-rvc/opciones-de-inferencia/).     
Modifícalas para mejores resultados si lo deseas.  


 <img src="../aicovergen-img/3.png" alt="image" width="270" height="auto">        

‎       
> • ‎ `REMIX_MIX_RATE` funciona como *Volume Envelope*.        
> • ‎ `FILTER_RADIUS` baja el volumen de los sonidos de respiración. (no suprime) 
***
###### ‎  
#### 7 . <u>Ajusta la mezcla & reverb.</u> (opcional)         

- En ``Audio Mixing Options``, puedes cambiar los valores para determinar el volumen de las vocales principales, coro, e instrumental.      

    <img src="../aicovergen-img/4.png" alt="image" width="240" height="auto">‎                
    ‎     
- En `Reverb Control`, puedes añadirle reverb a las vocales de salida.      
    ‎       
<img src="../aicovergen-img/6.png" alt="image" width="240" height="auto"> ‎  
 ‎      
==- <u>*Configuración de Reverb Control:*</u>     
REVERB_SIZE
:   Lo "amplio" que suena la reverb, como el tamaño de una habitación.        

REVERB_WETNESS
:   Volumen del reverb. en sí.        

REVERB_DRYNESS
:   Volumen de las vocales.       

REVERB_DAMPING
:   Absorción de las altas frecuencias de la reverb:   
‎ ‎ ‎ ‎ ‎ ‎ • ‎ Un mayor valor equivale a una reverb. más cálida & natural.       
‎ ‎ ‎ ‎ ‎ ‎ • ‎ Uno menor equivale una más brillante & presente.   
===

***
###### ‎    
#### 8. <u>Comienza la inferencia.</u>      
Cuando estés listo, ejecuta la celda `Generate Cover` para empezar la conversión.      

Terminará cuando el último mensaje ponga "**Cover generated at**" seguido de la ruta del audio de salida.    

<img src="../aicovergen-img/9.png" alt="image" width="850" height="auto">

***
###### ‎   
#### 9. <u>Descarga el resultado.</u>     
a. Toca el símbolo de carpeta ( :icon-file-directory: ) a la derecha.       
Abre la carpeta `content`, luego `FIX`, `song_output`, y habrá una nueva carpeta con números, conteniendo el resultado & algunos elementos de la canción.     
    
    El audio con las vocales convertidas será nombrado con el **algoritmo** que usaste (Crepe o RMVPE), seguido de "**mixed**" al final.     

b. Hazle click derecho, toca `Descargar` & eso será todo.       

    <img src="../aicovergen-img/10.png" alt="image" width="550" height="auto">‎     

    !!!
    Si quieres el audio sin la influencia de `REMIX_MIX_RATE`, usa el que no contenga "mixed" al final.
    !!!
###### ‎   
- #### Si notas que la voz falla, toca [<u>aquí</u>](http://localhost:5000/recursos-de-rvc/artifacting/).
***
###### ‎   
:::content-center   
``Guía original: Eddy``    
``Rehecho por: Julia`` 
:::     
:::content-center
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Envíanos Ideas"](https://forms.gle/Q1WX8AxWkH2vuMRd9)
:::    
***