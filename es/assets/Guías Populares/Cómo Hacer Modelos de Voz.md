# :icon-dependabot: Cómo Hacer Modelos de Voz

``Última actividad: Feb 10, 2024``
***
:::content-center
## Introducción
‎
:   ‎
:::
:::content-center
#### ¿Perdido en cómo hacer un modelo de voz de IA? Aprendamos cómo.     
:::
- Para convertir las vocales en tu persona deseada, usaremos el mejor software para lograr este trabajo, <U>**RVC.**</u>   

- RVC (Retrieval-based Voice Conversion) es un software avanzado de IA de clonación de voz. Es gratis y de código abierto.

- Requiere de **buenas [<u>specs</u>](http://localhost:5000/otro/glosario/#specs) & <u>[GPU](http://localhost:5000/otro/glosario/#gpu)</u>** (específicamente NVIDIA) para entrenar efectivamente, aunque también RVC puede ser ejecutado mediante la <u>[nube](http://localhost:5000/otro/glosario/#uso-en-la-nube)</u>, y ser usado en cualquier dispositivo.    

Ahora, empecemos con los pasos. Ten en cuenta que no será un proceso instantáneo, recuerda tener paciencia.
***
:::content-center
## Pasos
:::
‎
:   ‎

### 1. Obtén dataset
- ***En el contexto de RVC***, el dataset es un archivo de **audio** conteniendo la voz que el modelo replicará. Puede ser ya sea hablando o cantando.

- Tener un dataset **limpio** es crucial para buenos resultados, así que tomate el tiempo de remover los ruidos indeseados.        
       
- #### [<u>Aprende más aquí</u>](http://localhost:5000/aislamiento-vocal--datasets/datasets/).
***
###### ‎ 
### 2. Prepara RVC
- Con tu dataset listo, es hora de preparar RVC para entrenar el modelo.

- Existen bastantes versiones de RVC, pero elegimos las más aptas para principiantes.
Escoge según tus necesidades:    

    #### :icon-device-desktop: ‎ <u>[Localmente](http://localhost:5000/rvc/local/mainline/)</u> 

    #### :icon-cloud: ‎ <u>[Por la Nube](http://localhost:5000/rvc/por-la-nube/entrenar/rvc-disconnected/)</u>

***
###### ‎ 
### 3. Entrena el modelo
- Antes de que empieces, te avisamos que las guías de entrenamiento están orientadas al uso  de <u>[TensorBoard](http://localhost:5000/recursos-de-rvc/epochs-sobreentrenar--tensorboard/)</u>. Dale una leída rápida antes de comenzar el entrenamiento.     

- Ahora ve & comienza a entrenar tu modelo. ¡Suerte & recuerda ser paciente!
***
:::content-right
`Hecho por Julia`      
:::
‎  
:::content-right
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Envíanos Ideas"](https://forms.gle/Q1WX8AxWkH2vuMRd9)
::: 
‎  
‎  
***