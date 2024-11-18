---
icon: chevron-right
order: 6000
---

``Last update: Feb 10, 2024``   
***
###### ‎
:::content-center
## Epochs
:::     
- "Epoch" is a unit of measuring the training cycles of an AI model.     

- In other words, the amount of times the model went over its <u>[dataset](https://docs.ai-hub.wtf/rvc/resources/datasets/)</u> and learned from it.         
###### ‎ 
#### *:icon-chevron-right: How many epochs should I use for my dataset?*
- There isn't a way to know the right amount previous to training. It depends on the size, length & quality of the dataset.

- If you aim towards a quality model, it's not convenient to input a semi-arbitrary amount of epochs, as it makes it prone to underfitting/overtraining. (explained later)

- So it's best to use TensorBoard. WIth it you can determine **exactly** for how long you should train. (explained later) 
###### ‎ 
#### *:icon-chevron-right: Do more epochs equal a better model?*
- It doesn't, since using a disproportionate amount will overtrain the model, which will affect the quality of it.             
***
###### ‎ 
:::content-center
## Overtraining
:::
###### ‎       
- In the field of AI, is when an AI model learns its <u>[dataset](https://docs.ai-hub.wtf/rvc/resources/datasets/)</u> too well, to the point where it centers too much around it & starts replicating undesired data.

- The model performs very well with data of the dataset, but poorly with new data, as it has lost its ability to replicate anything that deviates from it.

- It happens when the model is trained for **too long**/is too complex. So to avoid this, RVC users use a tool called ***TensorBoard***.
***   
:::content-center
<img src="../tensorboard-img/1.png" alt="image" width="350" height="auto"> 

###### ‎
## TensorBoard
:::   
###### ‎
- TensorBoard is a tool that allows you to visualize & measure the training of an AI model, through graphs & metrics.

- It's specially useful for determining when to stop training a voice model, since with it you can detect when the <u><u>[overtraining</u>](https://docs.ai-hub.wtf/rvc/resources/epochs--tensorboard/#overtraining)</u> point begins.    

- Because of this, TB is the most convenient tool for RVC users for perfecting a voice model.     
***
###### ‎
### :icon-chevron-down: Installing & Opening

!!!success
For <u>[RVC Disconnected</u>](https://docs.ai-hub.wtf/rvc/cloud/rvc-disconnected/) users, ignore this, it opens up by itself when you start training.
!!!

###### ‎       
1. Download this file & move it inside RVC's folder. Ensure the file path doesn't contain spaces/special characters.
  
    [!file](./tensorboardfiles/TensorVENV.bat)    
###### ‎
2. Now execute it. It will open a console window & create some folders inside RVC.    
    - If you get the `Windows protected your PC` issue, click <u>**More info**</u> & **Run anyway**.         
‎   
3. Once it's done, your default browser should open with TensorBoard app.           
‎  
    - If it doesn't, copy the address of the console at the bottom, and paste it in your browser.       
    Said address will say "**https://localhost**" followed by some numbers.     
    ‎  
    <img src="../tensorboard-img/11.png" alt="image" width="500" height="auto">

***
###### ‎
### :icon-chevron-down: Usage Guide
    
+++ Simple Guide
###### ‎     
#### :icon-chevron-down: <u>SETTING UP</u>
***
- Open TB & begin training in RVC.     

    - If you get the ``No dashboards are active`` issue, select `SCALARS` in the top right corner dropdown.

        <img src="../tensorboard-img/17.png" alt="image" width="230" height="auto">‎    
‎       
- First ensure **auto-refresh** is on, so the graphs update constantly.    

    Click the gear (:icon-gear:) in the top left corner & turn on **``Reload data``**.      
    You can always manually refresh with the refresh symbol (🔄) in the top right.  
            
    <img src="../tensorboard-img/2.png" alt="image" width="280" height="auto">
       
    ‎       
- Go to the `SCALARS` tab.      
        ‎       
        <img src="../tensorboard-img/12.png" alt="image" width="280" height="auto">     
        ‎        

***
#### :icon-chevron-down: <u>GRAPH</u>
***
- #### In the left panel:  
    1. Activate `Ignore outliers in chart scaling`.  

    2. Set **Smoothing** to ``0.987``.     

    3. Select your model in the `Runs` section below. The models you tick will show in the graphs. (untick `/eval` if you want)        
    ‎       
    <img src="../tensorboard-img/18.png" alt="image" width="240" height="auto">‎      
‎       
- In the search bar, type "**g/total**". This will be the graph you'll monitor.        
    ‎   
        <img src="../tensorboard-img/19.png" alt="image" width="390" height="auto">‎        
‎    
‎  
- Each graph has three buttons in the corner:       
    - Left one is for going **fullscreen**.       
    - Middle one to **disable** Y axis, for a fuller view.       
    - And the right one is to **center** the view.      
        ‎       
        <img src="../tensorboard-img/15.png" alt="image" width="300" height="auto">‎    
‎       
- To **zoom** in & out the graphs, press the ALT key + mouse wheel. Remember to center the view after moving around, and after the graph updates.
***
 #### :icon-chevron-down: <u> MONITORING</u>
***
- Now let the training go for some time.  

- You'll detect **OT** (overtraining) when the graph hits the **lowest point**, then stay **flat**/**rising** indefinitely.  
    ‎       
     **<u>Example of OT for hours:</u>**
        
    <img src="../tensorboard-img/10.png" alt="image" width="370" height="auto">‎     
    ‎    
- There will be various low points, one after the other, so don't get too anxious if it's OT or not. You can always use a previous checkpoint either way.

- If it reaches a low point, let it run for **longer** until it's **very clear** it's OT.

- When you detect OT, zoom in & place your mouse over the **lowest point**. Note down the ``Step`` number.

    <img src="../tensorboard-img/8.png" alt="image" width="400" height="auto">‎    

- Use the model that was **closest** to ***before*** the OT point.      
    For more information, check the guide for your RVC in this website.

+++ Advanced Guide ‎     
#### :icon-chevron-down: <u>Other Graphs</u>
***
The other graphs within RVC are:

1. `FM` (Feature Matching): FM shows how well the model is able to recreate the features of the audio (lower is better).

2. `KL` (Kullback-Leibler): Kl shows how similar the audio sounds to the source (lower is better).

3. `Mel`: Mel shows how well the model can recreate the mel spectrogram (lower is better).

4. `Grad_g`: This shows how well the model is capable of making new stuff (lower is better).

5. `d/total`: This shows the discriminator's average loss. The discriminator tells the difference between what's Ai generated and what's not (lower is better).

***
#### :icon-chevron-down: <u>Mel Images</u>
***
- While looking through the Tensor Board you may come across `slice/mel_gen` and `slice/mel_org`. 
     - `slice/mel_gen` Is an image of a mel spectrogram that the generator created in attempt to make it match `mel_org`.
     <img src="../tensorboard-img/mel_gen.png" alt="image" width="700" height="700">‎ 

     - `slice/mel_org` Is an image of a mel spectrogram view of audio from your dataset. 
     <img src="../tensorboard-img/mel_og.png" alt="image" width="700" height="700">‎ 
***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/rvc/contributions/)
:::
