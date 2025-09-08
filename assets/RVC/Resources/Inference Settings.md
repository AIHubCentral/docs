---
icon: chevron-right
order: 100
---

``Last update: August 14, 2025``

***
###### ‎ 
:::content-center
## Introduction
:::
- When doing [<u>inference</u>](https://docs.aihub.gg/extra/glossary/#inference)</u> in RVC, you'll come across to quite a few options that you can tweak, that influence the conversion process.

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

#### :icon-chevron-down: Also known as <u>Index Rate</u>, it determines the level of influence of model's [<u>.INDEX</u>](https://docs.aihub.gg/essentials/voice-models/#voice-model-files) file:

- Higher values will apply more of the .INDEX's characteristics.   

- Lowering it can **reduce [<u>artifacting</u>](https://docs.aihub.gg/rvc/resources/dataset-making/#artifacts)**.      
     
>Remember, if the <u>[dataset](https://docs.aihub.gg/rvc/resources/datasets/)</u> had other sounds like background noise, there will be noise in the .INDEX too.


***
###### ‎
:::content-center
### <u>Pitch Extraction Algorithm</u>
<img src="../infsettings-img/3.png" alt="image" width="440" height="auto"> 
:::
‎ 

#### :icon-chevron-down: They're the algorithms for converting the vocals.        

- Each one works in its own way, and has its pros & cons.       

- There's a <u>[Pitch Benchmark](https://github.com/lars76/pitch-benchmark)</u>, but this is generally speaking and not only taken in the context of RVC.

- As the majority of them are obsolete, we'll focus on the 3 best ones: **RMVPE**, **Mangio-Crepe** & **FCPE**.

    ==- *RMVPE*
    ###### ‎       
    - A Robust Model for Vocal Pitch Estimation in Polyphonic 
    - Fast        
    - Decent precision       
    - Usually sounds a little harsh   
    - Should be your **go-to** algorithm, due to its convenience      
    - Better with harmonic-rich voices / fuller voices 
    ***
    Some <u>[forks](https://docs.aihub.gg/essentials/whats-rvc/#forks)</u> include **RMVPE_GPU** & **RMVPE+**. Same algorithm, but with a modification:         

    <u>**RMVPE GPU**</u>:
    :   Training only. Uses more GPU power, making you train faster.

    <u>**RMVPE+**</u>:
    :   Inference only. Allows you to set the maximum/minimum frequency, to reduce small distortions. Recommended for advanced users.

    ===

    ==- *Mangio-Crepe / Crepe*
    ###### ‎  
    - **NOTE THAT MANGIO CREPE IS ONLY A PLACEBO**: 160 hop is required to match with feature extraction, if you ran hop 40, that made f0 output 4x longer than needed and it had to be interpolated back required size. That's why it got removed from Applio, it would be better to use Crepe, or even better just use RMVPE.
    - Mangio Crepe: It's crepe, but you can adjust its hop_length. It determines the time it takes the voice to hit a note. The lower the value, the more detailed results you'll get, but will take longer to process
    - If you have really clean audio use this over RMVPE
    - Better with soft, whspery or voices with feminine timbres
    ###### ‎ 
    >Lowering it too much might lead to voice cracks so it's recommended to not lower it below 64.

    ===

    ==- *FCPE*
    ###### ‎  
    - Fast Context-base Pitch Estimator
    - Very fast, less precise and prone to noise
    - Useful for Realtime. If you have poor performance in Realtime, use this over RMVPE
    - Might be better with human softness
    ###### ‎ 

    ===

    ==- *Switft*
    ###### ‎  
    - Pretty new
    - Might be more precise than RMVPE, but it's not as much tested yet for RVC
    - Fast, which is good for realtime
    - Check https://github.com/lars76/swift-f0/ for more info
    ###### ‎ 

    ===

>They also work the same for training models.


***
###### ‎
:::content-center
### <u>Embedder Model</u>
<img src="../infsettings-img/embedder-options.png" alt="Embedder Models Options" width="440" height="auto"> 
:::
‎ 

#### :icon-chevron-down: They're the Models used for learning speaker embedding.        

- Each one works in its own way, and has its pros & cons.       

- This model analyzes an audio sample to extract a "speaker embedding", it's like a digital fingerprint of a voice's unique timbre and characteristics.

    ==- *ContentVec*
    ###### ‎       
    - The **default and original one, used for the great majority of RVC models**.
    - An advanced model adapted from the HuBERT framework, specifically designed to be better at separating speech *content* from the *speaker's* unique vocal characteristics.
    - This helps to prevent the original speaker's pronunciation or words from "bleeding" into the final output.
    - Often considered a high-quality choice for getting a clean and accurate speaker identity.

    ===

    ==- *Chinese-Hubert-Base*
    ###### ‎  
    - A HuBERT (Hidden-Unit BERT) model that was pre-trained specifically on a very large dataset (10,000 hours) of Chinese speech.
    - Because it is specialized for the Chinese language, it can be particularly effective at capturing the nuances of Mandarin-speaking voices.
    - While optimized for Chinese, it can still function as a general-purpose embedder for other languages.

    ===

    ==- *Japanese-Hubert-Base*
    ###### ‎  
    - A HuBERT model pre-trained on a large-scale Japanese speech corpus (approximately 19,000 hours).
    - Its specialization in Japanese makes it adept at creating embeddings from Japanese speakers, as it's tuned to the phonetic and acoustic characteristics of the language.
    - Can also be used for other languages, but may show a performance advantage with Japanese source audio.

    ===

    ==- *Korean-Hubert-Base*
    ###### ‎  
    - A HuBERT model pre-trained on a large dataset of Korean speech.
    - Like the other language-specific models, it is optimized for capturing the vocal characteristics of Korean speakers.
    - Using a model pre-trained in the target language can sometimes yield more accurate speaker similarity.

    ===

    ==- *Spin*
    ###### ‎  
    - A newer, more advanced embedder based on the "Speaker-invariant Clustering" method.
    - Excels at separating the speaker's unique vocal timbre from the actual phonetic content (the words being spoken).
    - This could result in clearer and more accurate pronunciation compared to older models like ContentVec.
    - Its architecture is well-suited for realtime models.
    - It can be downloaded at: https://huggingface.co/IAHispano/Applio/tree/main/Resources/embedders/spin .

    ===

    ==- *Custom*
    ###### ‎  
    - This option allows for the use of a user-provided, custom-trained embedder model.

    ===


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

#### :icon-chevron-down: Also known as <u>Remix Mix Rate</u>, controls the loudness of the output:
- The closer to ``0``, the more the output will **match** the **loudness** of the **input** audio.

- The closer to ``1``, the more it will match the loudness of the [<u>dataset</u>](https://docs.aihub.gg/rvc/resources/dataset-making/) the **model** was trained on.

>Basically, leave it at 0 if you want the audio to try to keep its original volume.
***
###### ‎
:::content-center
### <u>Split Audio</u>
<img src="../infsettings-img/6.png" alt="image" width="200" height="auto"> 
:::
‎   

#### :icon-chevron-down: Gives a faster inference & more consistent output volume:
- In RVC sometimes there's an error where the volume of the output lowers in some parts.

- To prevent this, Split Audio divides the audio & infers them one by one. Then unites them at the end.

- Doing it this way is faster too.


***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
