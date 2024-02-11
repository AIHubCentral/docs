``Última actividad: Feb 10, 2024``   

***
###### ‎   
:::content-center
## Formatos con Pérdida
:::
- Formatos comunes con pérdida de calidad son **MP3**, OGG, OPUS, M4A, entre otros.

- Estos comprimen (pierden) la calidad original. Están hechos para una transmisión rápida & ocupar poco espacio.

- Deshaciéndose de algunos datos (en este caso, calidad), logran tener un menor tamaño de archivo.       

***
###### ‎ 
:::content-center
## Formatos sin Pérdida
#### *``(ideales para RVC)``*  
:::
- Los principales son **WAV** & **FLAC**. Estos no compriman la calidad original.

- **FLAC** usa un algoritmo de compresión que no pierde calidad. Recomendable por encima de WAV, ya que ocupa menos espacio.        
- **WAV** no hace ninguna compresión, es puramente los datos originales. Por ende tiene un tamaño de archivo más grande.

- Se recomiendan para RVC, ya que cuanta más calidad tenga audio, más resultados precisos ofrecerán.


!!! <u>NOTAS:</u>
Ambos formatos dan los mismos resultados & no tienen una diferencia audible.      
Convertir un audio con pérdida a uno sin pérdida no restaurará la calidad perdida.
!!!
***
###### ‎  
:::content-center
## Sample Rate
#### *``(Tasa de Muestreo)``*
:::
- La tasa de muestreo es una unidad que determina la cantidad total de muestras (datos) que pueden caber por segundo. 

- Cuánto más grande sea el sample rate, más información será almacenada, por lo tanto, mayor será la calidad.

- Se miden en Kilohertz.

- Las tasas más comunes son **32, 40, 44.1 & 48**.      
‎ 

###### ‎ 
### Determinar Sample Rate
- Al entrenar en RVC, tendrás que insertar el **target sample rate** correspondiente a la tasa de muestreo de tu <u>[dataset](http://localhost:5000/aislamiento-vocal--datasets/datasets/)</u>.       
- Insertar uno incorrecto afectará la calidad final.      
- Para saber el número, usaremos **Ilaria Audio Analyzer**.        
    ***
    #### <u>Instrucciones:</u>  
    
    - ##### Paso 1:       
        Ingresa al espacio de HF [<u>aquí</u>](https://huggingface.co/spaces/TheStinger/Ilaria_Audio_Analyzer).        
    ***
    - ##### Paso 2:    
        Toca la casilla grande para ingresar tu audio (o simplemente arrástralo hacia este). El audio empezará a cargarse.      
        Luego toca `Create Spectrogram And Get Info` y lo procesará.

        <img src="../audioformats-img/1.png" alt="image" width="500" height="auto">‎   
    ***
    - ##### Paso 3:      
        A la derecha, en ``Samples per second`` verás el tasa de muestreo completo de tu audio.

        <img src="../audioformats-img/2.png" alt="image" width="400" height="auto">   
    ***

    !!!warning <u>IMPORTANTE:</u>     
    Si las frecuencias no llegan a lo alto del espectrograma, mira la tasa a la que alcanza y **multiplica** por <U>**2**</u>.      
    !!!

    ###### ‎
    {.list-icon}
    - #### <u>Ejemplo:</u>
        <img src="../audioformats-img/3.png" alt="image" width="480" height="auto">‎    
    ‎    
    >Aquí alcanzó 20kHz. Duplicarlo nos da 40kHz. Por ende, el *target sample rate* ideal sería `40k`. 

***
###### ‎
:::content-center
## Bitrate & Bit Depth
#### *`Info. extra`*
:::

#### :icon-chevron-down: BITRATE:
- La *tasa de bits* es la cantidad de datos procesados por cierta unidad de tiempo. Normalmente se mide en kilobits por segundo (kbps).
- Una mayor tasa equivale a una calidad mayor.
- Puedes imaginarlo como la resolución de video (240, 480p, 1080p, etc.) 
###### ‎   
#### :icon-chevron-down: BIT DEPTH:
- La *profundidad de bit* define el rango dinámico de cada muestra.
- Esto determina la diferencia entre el sonido más bajo & alto de un audio.        
- Un mayor bit depth representará el volumen de manera más precisa.        

***
:::content-right
`Hecho por Julia & Alex`      
:::
‎  
:::content-right
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Envíanos Ideas"](https://forms.gle/Q1WX8AxWkH2vuMRd9)
::: 
‎  
‎  
***