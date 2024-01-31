:::
*`Written by Julia`*        
*`A thanks to SimplCup & Poopmaster for helping`*     
``Last update: Jan 27, 2024``   
***
###### ‎
:::content-center
## What are Epochs?
:::     
###### ‎  
- "Epoch" is a unit of measuring the training cycles an AI model has gone through.      
- In other words, the amount of times the model went over its dataset and learned from it.         
‎ 
#### *:icon-chevron-down: How many epochs should I use for my model?*
- There isn't a way to know the right amount, as it depends on the length, quality & size of the dataset.       
Instead, use **<u>TensorBoard</u>**. This tool helps you determine **exactly** for how long you should train. (explained later)  

- A common **mistake** RVC users make is insert a specific epochs amount depending on the dataset's length, but this is **not a good method** if you want a quality model.

- Since using a semi-arbitrary number makes you prone to **underfitting** or **overtraining** your model, which negatively impacts the quality. (explained later)     
‎ 
#### *:icon-chevron-down: Do more epochs equal a better model?*
- It doesn't, since **overtraining** is an actual phenomenon that negatively affects the quality of a model.             
***
###### ‎ 
:::content-center
## What is Overtraining?
:::
###### ‎       
- It's a phenomenon that ocurrs in the **AI training** field. It's when an AI model learns the dataset too well, to the point where it gets too fixated on it & begins learning undesired/unnecesesary data.  

- The model performs very well when dealing with inputs containing the dataset, but poorly on new/unseen data.     
It became too specialized on the dataset and has lost its ability to replicate anything that deviates from it.    

- This happens when the model is **trained for too long**/is too complex.

==- ***A simple analogy:***     
:icon-triangle-right: Imagine you (an AI) have an exam next month about Michael Jackson.    
‎       
:icon-triangle-right: Your study content is a biography book about MJ (dataset).    
‎       
:icon-triangle-right: For the next 30 days, you'll read the entire book **10 times** everyday (training time).  
‎       
:icon-triangle-right: In the day of the exam, a question says "``When is Michael Jackson's birthday?``"     
‎       
:icon-triangle-right: The book you read only said "``Michael Jackson was born on August 29, 1958``", so you respond the question poorly.

>Although the question was very simple, your mind became too fixated on the study content, that you can't correctly answer anything that deviates from exactly it.
===
‎   
Now, to avoid overtraining an RVC voice model, RVC users use a tool called ***TensorBoard***.
***   
:::content-center
<img src="../tensorboard-img/1.png" alt="image" width="350" height="auto"> 

###### ‎
## What is TensorBoard?   
:::   
###### ‎
- TensorBoard is a tool that allows you to visualize & measure the training of an AI model, through graphs & metrics.

- It's specially useful for determining when to stop training a voice model, since you can detect when the [<u>overtraining</u>](https://aihubdocs.github.io/en/rvc-resources/epochs-overtraining--tensorboard/#what-is-overtraining) point begins.    

- Because of this,  TB is the most convenient tool for RVC users for perfecting a voice model.     
***
###### ‎
### :icon-chevron-down: How to Install & Open
!!!
• ‎ This method might not work for every fork.      
• ‎ For [<u>RVC Disconnected</u>](https://aihubdocs.github.io/en/rvc/cloud/training/rvc-disconnected/) users, ignore this, it opens up by itself when you begin training.
!!!
###### ‎       
- Download this file move it inside RVC's folder:       
  
    [!file](./tensorboardfiles/TensorVENV.bat)    
     
- Now execute. It will open a console window & create some folders inside RVC.    
If you get the `Windows protected your PC` issue, click <u>**More info**</u> & `Run anyway`.

- Once it's done, your default browser should open with TensorBoard app.           

- If it doesn't, copy the address of the console at the bottom, and paste it in your browser.       
Said address will say "**https://localhost**" followed by a number.

    <img src="../tensorboard-img/11.png" alt="image" width="500" height="auto">

***
###### ‎
### :icon-chevron-down: How to Use TensorBoard
  ‎     
    There are two ways of going over training with TB:       
- The **<u>simple</u>** guide goes over the **essentials** without going in-depth.      
Recommended for **first-timers**.

- The **<u>advanced</u>** one goes in-depth on AI training & TB. You'll actually understand how it works to clear most doubts. Ideal after having **some experience** with TB, & for making quality models on the **long-term**.        
‎       
+++ Simple guide
‎       
- #### <u>Setting up TB.</u>
    - Open TB & begin training in RVC.     

        If you get the ``No dashboards are active`` issue, select `SCALARS` in the top left corner dropdown.

        <img src="../tensorboard-img/17.png" alt="image" width="230" height="auto">‎    
‎       
    - First ensure **auto-refresh** is on, so the graphs update constantly.    

        Click the gear (:icon-gear:) in the top left corner & turn on **``Reload data``**.      
    You can always manually refresh with the refresh symbol (🔄) in the top left.  
            
        <img src="../tensorboard-img/2.png" alt="image" width="280" height="auto">
       
        ‎       
    - Go to the `SCALARS` tab.      
        ‎       
        <img src="../tensorboard-img/12.png" alt="image" width="280" height="auto">     
        ‎        
    - <u>In the **left panel**:</u>     
        1.‎ Ensure `Ignore outliners in chart scaling` is **ticked**.       
        2. Set **Smoothing** to ``0.987``.      
        3. Ensure **your model** is selected in the `Runs` section below. The models you tick will show in the graphs.      
        (untick `/eval` if you want)        
        ‎       
        <img src="../tensorboard-img/18.png" alt="image" width="240" height="auto">       

***
###### ‎
- #### <u>Setting up graph.</u>
    - In the search bar, type "**g/total**". This will be the graph you'll monitor.        
    ‎   
        <img src="../tensorboard-img/19.png" alt="image" width="390" height="auto">‎        

    ‎   
    {.list-icon}    
    - Each graph has three buttons in the corner:       
    :icon-dash: Left one is for going **fullscreen**.       
    :icon-dash: Middle one to **disable** Y axis, for a fuller view.       
    :icon-dash: And the right one is to **center** the view.      
        ‎      
        <img src="../tensorboard-img/15.png" alt="image" width="300" height="auto">‎    
‎       
    - To **zoom** in & out the graphs, press the **ALT** key + the **scroll** wheel of your mouse.     
Remember to center the view as you move around.
***
###### ‎       
- #### <u> Monitoring the training.</u>
    - Now let the training go for some time.  

        You'll detect **OT** (overtraining) when **g/total** hits a **lowest point** in the graph, & then stay **flat**/**rising** indefinetely.  
        ‎       
        **<u>Example:</u>**
        
        <img src="../tensorboard-img/10.png" alt="image" width="370" height="auto">‎     
    ‎    
    - Don't be too anxious about if it's OT or not, the checkpoints get automatically saved either way. Run it for **longer** until it's **very clear** that it is.

    - When you detect OT, zoom in & place your mouse over the **lowest point**, & note down the ``Step`` number.
    Use the .PTH that was **closest** to **before** the OT point.   

        <img src="../tensorboard-img/8.png" alt="image" width="400" height="auto">‎    

        You can now stop training.      
        To learn about the training process onwards, check the training page of your RVC in this site.

+++ Advanced guide
:::content-center
‎   
:icon-alert: ~ *Work in progress.* ~ :icon-alert:
:::
+++
***
:::content-right
||| *Did I miss anything?*        
Send any feedback [<u>here</u>](https://forms.gle/5i6hTJRVkXRohvVF9) 👈
|||
:::
