---
icon: chevron-right
order: 2000
---

``Last update: Feb 10, 2024``
‎             
***
###### ‎ 
### Introduction        
In RVC, artifacting refers to an anomaly where the output voice sounds "robotic" & glitchy.     
This occurs after the <u>[inference](https://docs.ai-hub.wtf/extra/glossary/#inference)</u> or model training process.     
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
- If possible, it's best if your audio is in a <u>[lossless format](https://docs.ai-hub.wtf/extra/glossary/#lossless-formats)</u> like **WAV** or **FLAC**, preserving its original quality.

- Avoid using lossy ones like MP3 or OGG.
‎   
#### 2. If doing inference:
- Remove undesired noises with an <u>[vocal isolation</u>](https://docs.ai-hub.wtf/rvc/resources/vocal-isolation/) software.

- Lowering the <u>[search feature ratio</u>](https://docs.ai-hub.wtf/rvc/resources/inference-settings/) can also minimize this issue.

- If breathing sounds produce it, lower the <u>[Protection](https://docs.ai-hub.wtf/rvc/resources/inference-settings/)</u> value.
‎   
#### 3. If training models:
- Ensure to <u>[clean your dataset](https://docs.ai-hub.wtf/rvc/resources/datasets/#cleaning-datasets)</u> properly, this includes removing silences and distortions.

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/rvc/contributions/)
:::