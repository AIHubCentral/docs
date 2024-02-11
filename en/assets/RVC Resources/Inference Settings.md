``Last update: Feb 10, 2024``

***
###### ‎ 
:::content-center
## Introduction
:::
- When doing [<u>inference</u>](https://aihubdocs.github.io/en/other/glossary/#inference)</u> in RVC, you'll come across to quite a few options that you can tweak, that influence the conversion process.

- Configuring them accordingly can improve the output quality by a lot, as well as reduce artifacting, so we highly recommend learning them.   

- There are some of them that are either obsolete or not important. So if a setting is not explained here, you can ignore it.
***
###### ‎ 
:::content-center
## Explanation
:::
***
###### ‎   
:::content-center
### <u>Transpose</u>
<img src="../infsettings-img/1.png" alt="image" width="" height="auto">  ‎ 
:::

###### 
#### :icon-chevron-down: Also known as <u>Pitch</u>, it adjusts the tone of voice.
- Negative values lower the tone (e.g ``-2``).

- Positive ones raise it (e.g ``5``).

- You can use decimals if necessary (e.g `-4.3`).

>You'll usually have to modify this for the pitch to sound perfect. Modify it until it matches the tone of the model.

***
###### ‎
:::content-center
### <u>Search Feature Ratio</u>
<img src="../infsettings-img/2.png" alt="image" width="" height="auto"> 
:::
‎    

#### :icon-chevron-down: Also known as <u>Index Rate</u>, it determines the level of influence of model's [<u>.INDEX</u>](https://aihubdocs.github.io/en/essentials/voice-models/#voice-model-files) file:

- Higher values will apply more of the .INDEX's characteristics.   

- Lowering it can **reduce [<u>artifacting</u>](https://aihubdocs.github.io/en/vocal-isolation--datasets/datasets/)**.      
     
>Remember, if the <u>[dataset](https://aihubdocs.github.io/en/vocal-isolation--datasets/datasets/)</u> had other sounds like background noise, there will be noise in the .INDEX too.

***
###### ‎
:::content-center
### <u>Pitch Extraction Algorithm</u>
<img src="../infsettings-img/3.png" alt="image" width="440" height="auto"> 
:::
‎ 

#### :icon-chevron-down: Also known as <u>f0</u>, they're the algorithms for converting the vocals.        

- Each one works in its own way, and has its pros & cons.       

- As the majority of them are obsolete, we'll focus on the 3 best ones: **RMVPE**, **Crepe**, & **Mangio-Crepe**.

    ==- *RMVPE*
    ###### ‎       
    - Fast        
    - Decent quality       
    - Usually sounds a little harsh   
    - Should be your **go-to** algorithm, due to its convenience    

    *** 
    :::content-center 
    ##### Some <u>[forks](https://aihubdocs.github.io/en/other/glossary/#fork)</u> include *RMVPE_GPU* & *RMVPE+*. Same algorithm, but with a modification:       
    ###### ‎       
    :::
    **RMVPE GPU**
    :   Training only. Uses more GPU power, making you train faster.

    **RMVPE+**
    :   Inference only. You can set the maximum/minimum frequency, to reduce small distortions. Recommended for advanced users.

    ===

    ==- *Crepe*
    ###### ‎    
    - Slower
    - Has higher quality
    - More prone to noise & <u>[artifacting</u>](https://aihubdocs.github.io/en/rvc-resources/artifacting/). Switch to RMVPE if you can't fix it
    - Recommended for more **professional** results
    ===

    ==- *Mangio-Crepe*
    ###### ‎  
    - It's crepe, but you can adjust its **hop_length**
    - It determines the time it takes the voice to hit a note
    - The lower the value, the more detailed results you'll get, but will take longer to process
    - Useful when the audio/model performs drastic notes from note to note
    ###### ‎ 
    >Lowering it too much might lead to voice cracks.

    ===
>They also work the same for training models.
***
###### ‎    
:::content-center
### <u>Protect Voiceless Consonants</u>
<img src="../infsettings-img/4.png" alt="image" width="" height="auto"> 
:::
‎ 

#### :icon-chevron-down: Also known as <u>Protection</u>, they suppress breath sounds:

- Decrease the value to remove more breath sounds, as they cause some artifacting.

- A value of ``0.5`` **disables** this feature.     
‎   

>Be careful, lowering it too much will make it voice sound "inhumane" & suppress part of the words.

***
###### ‎
:::content-center
### <u>Volume Envelope</u>
<img src="../infsettings-img/5.png" alt="image" width="" height="auto"> 
:::
‎  

#### :icon-chevron-down: Controls the loudness of the output:
- The closer to ``0``, the more the output will **match** the **loudness** of the **input** audio.

- The closer to ``1``, the more it will match the loudness of the [<u>dataset</u>](https://aihubdocs.github.io/en/vocal-isolation--datasets/datasets) the **model** was trained on.

>Basically, leave it at 0 if you want the audio to try to keep its original volume.
***
:::content-right
`Written by Julia & Alex`     
:::
‎  
:::content-right
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Send Suggestions"](https://forms.gle/3GVR7opzpQrhgRCj9)
:::
‎  
‎  
***