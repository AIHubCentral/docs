``Última actividad: Feb 10, 2024``

***
###### ‎ 
:::content-center
## Introducción
:::
- Al hacer [<u>inferencia</u>](http://localhost:5000/otro/glosario/#inferencia) en RVC, te toparás con varios ajustes que puedes modificar. Estos influyen la conversión del audio.

- Configurarlos correctamente puede mejorar la calidad del audio de salida significativamente, al igual que reducir artifacting, por lo que recomendamos aprenderlos.  

- Hay algunas opciones que están obsoletas o no son muy importantes. Si una opción no se explica aquí, puedes ignorarla.
***
###### ‎ 
:::content-center
## Explicación
:::
***
:::content-center 
###### ‎ 
### <u>Transpose</u>
<img src="../infsettings-img/1.png" alt="image" width="" height="auto">  ‎ 
:::

###### 
#### :icon-chevron-down: También conocido como <u>Pitch</u>, ajusta el tono de voz:

- Usa un valor negativo para bajarlo. EJ: ``-2``.

- Usa uno positivo para subirlo. EJ: ``5``.

- Puedes usar decimales si es necesario también. EJ: ``-4.3``.               
‎  
>Usualmente tendrás que ajustar esta opción para excelentes resultados. Modifícalo hasta que iguale el tono del modelo.

***
:::content-center 
###### ‎
### <u>Search Feature Ratio</u>
<img src="../infsettings-img/2.png" alt="image" width="" height="auto"> 
:::

‎    
#### :icon-chevron-down: También conocido como <u>Index Rate</u>, define el nivel de influencia del [<u>.INDEX</u>](http://localhost:5000/gu%C3%ADas-populares/modelos-de-voz/#archivos-de-modelos) del modelo.

- Cuanto más lo subas, más se aplicarán las características del .INDEX.

- Bajarlo puede **minimizar [<u>artifacting</u>](http://localhost:5000/recursos-de-rvc/artifacting/)**.      
‎  
>Recuerda, si el <u>[dataset](http://localhost:5000/aislamiento-vocal--datasets/datasets/)</u> tenía otros ruidos como ruido de fondo, también habrá ruido en el .INDEX.

***
:::content-center 
###### ‎
### <u>Pitch Extraction Algorithm</u>

<img src="../infsettings-img/3.png" alt="image" width="440" height="auto"> 
:::
‎ 

#### :icon-chevron-down: También conocido como <u>f0</u>, son los algoritmos para convertir las vocales:

- Cada uno suena & trabaja a su manera, y tiene sus pros & contras.       

- Ya que mayoría están obsoletos, nos centraremos en los 3 mejores: **RMVPE**, **Crepe**, & **Mangio-Crepe**.

    ==- *RMVPE*
    ###### ‎       
    - Rápido        
    - Decente calidad       
    - Puede que suene algo abrasivo       
    - Debido a su conveniencia, usa este **por defecto**    

    *** 
    :::content-center 
    ##### Algunos [<u>forks</u>](http://localhost:5000/otro/glosario/#fork) traen *RMVPE_GPU* & *RMVPE+*. Mismo algoritmo, pero con una modificación:       
    ###### ‎       
    :::
    **RMVPE GPU**
    :   Solo para entrenamiento. Usa más potencia del <u>[GPU](http://localhost:5000/otro/glosario/#gpu)</u>, haciéndote entrenar más rápido.

    **RMVPE+**
    :   Solo para [inferencia](http://localhost:5000/otro/glosario/#inferencia). Puedes indicar la frecuencia mínima/máxima usable, para reducir distorsiones. Ideal para usuarios avanzados. 

    ===

    ==- *Crepe*
    ###### ‎    
    - Más lento
    - Tiene una calidad algo mejor
    - Más propenso al ruido & [<u>artifacting</u>](http://localhost:5000/recursos-de-rvc/artifacting/). Usa RMVPE si no lo puedes solucionar
    - Recomendado para resultados más **profesionales**.
    ===

    ==- *Mangio-Crepe*
    ###### ‎  
    - Es Crepe, pero puedes ajustar su **hop_length**.
    - Este determina el tiempo que le toma a la voz alcanzar una nota
    - Cuanto más lo bajes, más resultados detallados tendrás, pero tomará más en procesar
    - Útil cuando las vocales/modelo hace saltos drásticos de notas
    
    >Bajarlo demasiado puede provocar fallos en la voz.

    ===
>También funcionan igual para entrenar modelos.     

***
###### ‎ 
:::content-center    
### <u> Protect Voiceless Consonants</u>
<img src="../infsettings-img/4.png" alt="image" width="" height="auto"> 
:::
‎ 

#### :icon-chevron-down: También conocido como <u>Protection</u>, suprime sonidos de respiración:

- Disminuye el valor para reducirlos, ya que estos puede que causen algo de artifacting.

- Un valor de ``0.5`` **desactiva** esta opción.     
‎   

>Cuidado, bajarlo mucho hará que la voz suene "inhumana" y suprima parte de las palabras.

***
###### ‎
:::content-center    
### <u>Volume Envelope</u>
<img src="../infsettings-img/5.png" alt="image" width="" height="auto"> 
:::
‎  

#### :icon-chevron-down: Controla el volumen de salida:
- Cuanto más cerca esté a ``0``, el volumen del audio de salida **igualará** el de **entrada**. Ideal para disminuir ruidos indeseados.

- Y cuanto más cerca esté a ``1``, **igualará** el audio del [<u>dataset</u>](http://localhost:5000/aislamiento-vocal--datasets/datasets/) que el **modelo** fue entrenado.

>Básicamente, déjalo en `0` si quieres que el audio intente conservar su volumen original.

***
:::content-right
`Escrito por Julia & Alex`  
:::
‎   
:::content-right
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Envíanos Ideas"](https://forms.gle/Q1WX8AxWkH2vuMRd9)
:::
‎   
‎  
***