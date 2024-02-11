::: 
``Última actividad: Feb 10, 2024``   
***
###### ‎
:::content-center
## Epochs
:::     
- "Epoch" es una unidad de medida de los ciclos entrenamiento de un modelo de IA.   

- En otras palabras, la cantidad de veces que el modelo recorrió el <u>[dataset](http://localhost:5000/aislamiento-vocal--datasets/datasets/)</u> y aprendió de este.         
###### ‎ 
#### *:icon-chevron-right: " ¿Cuántos epochs debería usar para mi dataset? "*
- No hay manera de saber la cantidad correcta previo al entrenamiento. Depende del tamaño, longitud & calidad del dataset.    

- Si vas por un modelo de calidad, no es conveniente insertar una cantidad de epochs semi-arbitraria, ya que lo hace propenso al underfitting/sobreentrenamiento. (explicado luego)

- Por lo que te conviene usar **<u>TensorBoard</u>**. Con este determinarás **exactamente** por cuánto tiempo tendrás que entrenar. (explicado luego)  
###### ‎   
#### *:icon-chevron-right: " ¿Más epochs equivale a un mejor modelo? "*
- No, ya que una cantidad desproporcionada sobreentrenará el modelo, lo que afectará la calidad de este.             
***
###### ‎ 
:::content-center
## Sobreentrenar
:::
###### ‎       
- En el campo de la IA, es cuando un modelo de IA aprende demasiado bien su <u>[dataset](http://localhost:5000/aislamiento-vocal--datasets/datasets/)</u>, hasta que se centra mucho en el &  comienza a replicar datos indeseados.

- El modelo desempeña muy bien cuando le das información que contenía el dataset, pero mal con datos nuevos, porque perdió su capacidad de replicar cualquier cosa que se desvíe del dataset.

- Sucede cuando el modelo se entrena por **mucho tiempo**/es demasiado complejo. Pero para evitar esto, los usuarios de RVC usan la herramienta ***TensorBoard***.
***   
:::content-center
<img src="../tensorboard-img/1.png" alt="image" width="350" height="auto"> 

###### ‎
## TensorBoard
:::   
###### ‎
- TensorBoard es una herramienta que para visualizar & medir el entrenamiento de un modelo de IA, mediante gráficos y métricas.

- Es especialmente útil para determinar cuándo dejar de entrenar un modelo de voz, ya que puedes detectar cuando el punto de [<u>sobreentrenamiento</u>](http://localhost:5000/recursos-de-rvc/epochs-sobreentrenar--tensorboard/#what-is-overtraining) empieza.    

- Y por esto, TB es la herramienta más conveniente de usuarios de RVC para perfeccionar un modelo de voz.     
***
###### ‎
### :icon-chevron-down: Instalar & Abrir
!!!success
Si usas [<u>RVC Disconnected</u>](http://localhost:5000/rvc/en-la-nube/entrenar/rvc-disconnected/), ignora esto, ya que se abre por si solo.
!!!
###### ‎       
1. Descarga este archivo & muévelo dentro de la carpeta de RVC. Asegúrate que la ruta de la carpeta no contenga espacios/caracteres especiales.   
  
    [!file](./tensorboardfiles/TensorVENV.bat)    
###### ‎
2. Luego ejecútalo. Se abrirá una consola y creará unas carpetas dentro de RVC.    
    - Si te aparece el aviso "Windows protegió su PC", toca <u>**Más información**</u> & **Ejecutar de todas formas**.       
‎   
3. Cuando termine de descargarse, debería de abrirse tu navegador predeterminado con la app de TensorBoard.     
‎              
    - Si no lo hace, copia el enlace de la consola en la parte inferior, y pégala en tu navegador.       
    Dicha dirección dirá "**https://localhost**" seguido de unos números.       
    ‎   
    <img src="../tensorboard-img/11.png" alt="image" width="500" height="auto">

***
###### ‎ 
### :icon-chevron-down: Cómo Usar TensorBoard

+++ Guía Simple      
###### ‎  
#### :icon-chevron-down: <u>PREPARACIÓN</u>
***
- Abre TB & empieza a entrenar tu modelo.     

    - Si solo aparece ``No dashboards are active``, despliega la barra superior derecha, y selecciona `SCALARS`.    
‎   
    <img src="../tensorboard-img/17.png" alt="image" width="230" height="auto">‎    
‎       
‎   
- Primero asegúrate de que **auto-refresh** esté activado, para que los gráficos se actualicen constantemente.    
‎   
    Toca el engranaje ( :icon-gear: ) arriba a la derecha, & activa **``Reload data``**.      
    Para actualizarlos manualmente, toca el símbolo de recarga ( 🔄 ) arriba a la derecha.  
            
    <img src="../tensorboard-img/2.png" alt="image" width="290" height="auto">‎ 
‎       
‎   
- Ve a la pestaña `SCALARS`.      
        ‎       
        <img src="../tensorboard-img/12.png" alt="image" width="280" height="auto">         
        ‎       

***
#### :icon-chevron-down: <u>GRÁFICO</u>
***
- #### En el panel izquierdo:
    1. Activa `Ignore outliers in chart scaling`.
    
    2. Deja <u>**Smoothing**</u> en ``0.987``.

    3. Selecciona tu modelo en la sección `Runs`. Los modelos que actives se mostrarán en los gráficos. (desactiva `/eval` si quieres)        
        ‎       
        <img src="../tensorboard-img/18.png" alt="image" width="240" height="auto">‎       
‎       
- En la barra de búsqueda, escribe "**g/total**". Este será el gráfico que monitorearás.        
‎   
    <img src="../tensorboard-img/19.png" alt="image" width="390" height="auto">‎        
‎       
‎         
- Los gráficos tienen tres botones en la esquina:       
    - El izquierdo <u>maximiza</u> el tamaño del gráfico.       
    - El del medio <u>desactiva</u> el eje **Y**, para una mejor vista.       
    - El derecho <u>centra</u> la vista.      
        ‎      
        <img src="../tensorboard-img/15.png" alt="image" width="300" height="auto">‎    
‎       
‎       
- Para hacer **zoom**, toca la tecla Alt + rueda del mouse (scroll).
Recuerda centrar la vista tras moverla.     
‎      
*** 
#### :icon-chevron-down: <u>MONITOREO</u>
***

- Ahora deja que entrene por un buen tiempo.        

- Detectarás **SE** (sobreentrenamiento) cuando el gráfico alcance el **punto más bajo**, & luego permanece **plano**/**subiendo** indefinidamente.
     
    ##### EJEMPLO: 
    <img src="../tensorboard-img/10.png" alt="image" width="370" height="auto">‎     
    ‎    
- Habrán varios puntos bajos a medida que progrese, uno más bajo que el otro. Por lo que no te pongas ansioso si está SE o no. Siempre puedes usar un punto de guardado anterior.      

- Si alcanza un punto bajo, déjalo andar por **más tiempo** hasta que sea **muy evidente** que lo es.

- Cuando detectes SE, hazle zoom al **punto más bajo** y pasa el cursor sobre este. Observa el número ``Step``.

    <img src="../tensorboard-img/8.png" alt="image" width="400" height="auto">‎    
‎    
- Usa el modelo más **cercano** a ***antes*** del punto de SE.   
    Para más información, consulte la guía de tu RVC en este sitio.

+++ Guía Avanzada
:::content-center
‎   
:icon-alert: ~ ***En construcción.*** ~ :icon-alert:
:::
+++

###### ‎    
:::content-center
`Escrito por Julia, SimplCup, Litsa & Poopmaster`       
:::
:::content-center
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Envíanos Ideas"](https://forms.gle/Q1WX8AxWkH2vuMRd9)
:::
***