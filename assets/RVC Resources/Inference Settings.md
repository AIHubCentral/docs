`Written by Julia & Alex`     
``Last update: Jan 27, 2024``

***
###### ‎ 
:::content-center
## Introduction 📜
:::
- When doing [<u>inference</u>](https://aihubdocs.github.io/en/other/glossary/#inference) in RVC, you'll come across to quite a few options that you can tweak, that influence the convertion process.

- Configuring them accordingly can improve the output quality by a lot, so we highly recommend learning them.   

- There are some of them that are either obsolete or not important. So if a setting is not explained here, you can ignore it.
***
###### ‎ 
:::content-center
## Settings Explanation 📝
:::
!!!success <u>TIP:</u> 
I recommend using a small sample (like 20 secs) to test more efficiently.       
Same thing with special sounds like high notes/screams/growls/whispers etc., as these may be tricky to handle.
!!!
###### ‎   
### <u>Pitch</u> (or *Transpose*)
<img src="../infsettings-img/1.png" alt="image" width="" height="auto">  ‎      
‎   
#### :icon-chevron-down: Adjusts tone of voice:   
- Negative values lower the tone (e.g ``-2``).

- Positive ones raise it (e.g ``5.3``).

- Transposing audio means notes are transposed too. It could lead to mismatch of keys, if you're making an AI Cover.    
To prevent it, use numbers divisable by 12 & are integers.      
``12``, ``24``, ``36``, or ``-12``, ``-24``, ``-36``, etc.              

>You'll usually have to modify this for the pitch to sound perfect.      
>Modify it until it sounds just like the model.

***
###### ‎
### <u>Search Feature Ratio</u> (or *Index Rate*)
<img src="../infsettings-img/2.png" alt="image" width="" height="auto"> 

‎    

#### :icon-chevron-down: Determines level of influence of model's [<u>.INDEX</u>](https://aihubdocs.github.io/enessentials/voice-models--how-to-search-them/#voice-model-files) to the audio:
- Higher values will apply more of the INDEX to the output.   

- In other words, it determines (at some extent) some characteristics of the model's voice. 

- Lowering it can **reduce [<u>artifacting</u>](https://aihubdocs.github.io/en/rvc-resources/artifacting--how-to-fix-it/)**.      
     
>Remember, if the dataset had other sounds like (example) background noise, there will be noise in the .INDEX too.

***
###### ‎
### <u>Pitch Extraction Algorithm</u>
<img src="../infsettings-img/3.png" alt="image" width="440" height="auto"> 

‎ 

#### :icon-chevron-down: The algorithms (or methods) for converting the audio.        

Each algorithm works & sounds in its own way.     
As a lot of them are obsolete, we'll focus on the three main ones: **RMVPE**, **Crepe**, & **Mangio-Crepe**.

||| <u>RMVPE</u>
- Fast.
- Decent quality.
- Recommended for casual use.
- Usually sounds a little harsh.
- Should be your **go-to algorithm**.
||| <u>Crepe</u>
- Slower.
- More detailed.
- More prone to [<u>artifacting</u>](https://aihubdocs.github.io/enrvc-resources/artifacting--how-to-fix-it/).        
Use RMVPE if it happens.
- Recommended for more **professional** results.
||| <u>Mangio-Crepe</u>
- It's Crepe, but you can change its **hop_length**.
- It determines the time the voice takes to go from note to note.
- Lower values yield more precise, detailed results, but longer processing time.
- Useful when the vocals/model performs drastic note shifts.
|||

!!! <u> NOTES:</u>
- They also work the same for the training process.     
- Some forks include `RMVPE_GPU` & ``RMVPE+``. These are RMVPE but with a modification:
    - **RMVPE_GPU**: Training only. Uses more GPU power, for a faster process.        
    - **RMVPE+**: Inference only. Has a slider that sets the minimum/maximum frequency. Great for reducing small distorsions.   
    Recommended for advanced users.
!!!
***
###### ‎    
### Protect Voiceless Consonants (or Protection)
<img src="../infsettings-img/4.png" alt="image" width="" height="auto"> 

‎ 

#### :icon-chevron-down: Suppresses breath sounds, as they cause some artifacting:
- Decrease the value to remove more breath sounds.
- A value of ``0.5`` **disables** this feature.     
‎   

>Be careful, lowering it too much will make the voice sound "inhumane" and supress part of the words.

***
###### ‎
### Volume Envelope
<img src="../infsettings-img/5.png" alt="image" width="" height="auto"> 

‎  

#### :icon-chevron-down: Controls the loudness of the output:
- The closer to ``0``, the more the output will **match** the **loudness** of the **input** audio.
- The closer to ``1``, the more it will match the loudness of the [<u>dataset</u>](http://localhost:5000/Docs/vocal-isolation--datasets/datasets--how-to-clean-them/) the **model** was trained on.

>Basically, leave it at 0 if you want the audio to try to keep its original volume.
***
:::content-right
||| *Did I miss anything?*        
Send any feedback [<u>here</u>](https://forms.gle/5i6hTJRVkXRohvVF9) 👈
|||
:::
