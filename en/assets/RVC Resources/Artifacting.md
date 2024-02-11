``Last update: Feb 10, 2024``
‎             
***
###### ‎ 
### Introduction        
In RVC, artifacting refers to an anomaly where the output voice sounds "robotic" & glitchy.     
This occurs after the <u>[inference](https://aihubdocs.github.io/en/other/glossary/#inference)</u> or model training process.     
***
###### ‎ 
### Causes    
It usually occurs when the dataset/vocal sample meets any of these criteria: 

‎ ‎ ‎ • ‎ Audio is low-quality      
‎ ‎ ‎ • ‎ Voice model was overall poorly trained        
‎ ‎ ‎ • ‎ There are overlapping voices      
‎ ‎ ‎ • ‎ There is reverb       
‎ ‎ ‎ • ‎ There is noise
             
As you noticed, most of the issues boil down to the audio sample not being properly **clean**. RVC is built for purely working with voices, not other sounds.         

Remember that the cleaner your input audio is, the better the results.
***
###### ‎ 
### Solutions    
#### 1. Use a lossless format:
- If possible, it's best if your audio is in a <u>[lossless format](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/)</u> like **WAV** or **FLAC**, preserving its original quality.

- Avoid using lossy ones like MP3 or OGG.
‎   
#### 2. If doing inference:
- Remove undesired noises with an <u>[audio isolation</u>](https://aihubdocs.github.io/en/vocal-isolation--datasets/vocal-isolation/) software.

- Lowering the <u>[search feature ratio</u>](https://aihubdocs.github.io/en/rvc-resources/inference-settings/) can also minimize this issue.

- If breathing sounds produce it, lower the <u>[Protection](https://aihubdocs.github.io/en/rvc-resources/inference-settings/)</u> value.
‎   
#### 3. If training models:
- Ensure to <u>[clean your dataset](https://aihubdocs.github.io/en/vocal-isolation--datasets/datasets/#cleaning-datasets)</u> properly, this includes removing silences and distortions.

***
:::content-right
`Written by Julia`
:::
‎   
:::content-right
[!button variant="primary" corners="pill" icon="feed-discussion" iconAlign="right" text="Send Suggestions"](https://forms.gle/3GVR7opzpQrhgRCj9)
:::
‎   
‎   
***