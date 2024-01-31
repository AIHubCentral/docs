*`Written by Julia`*      
``Last update: Jan 27, 2024``
‎             
***
###### ‎ 
### What is artifacting?        
In RVC, artifacting refers to an anomaly where the output voice sounds "robotic" & glitchy.     
This occurs during the [<u>inference</u>](https://legendary-eureka-x5xwvp97wpp2vj49-5000.app.github.dev/other/glossary/#inference) or model training process.     
***
###### ‎ 
### Why does it happen?     
Artifacting usually ocurrs when the dataset/vocal sample meets any of these criteria: 

‎ ‎ ‎ • ‎ Audio is low-quality      
‎ ‎ ‎ • ‎ Voice model was overall poorly trained        
‎ ‎ ‎ • ‎ There are overlapping voices      
‎ ‎ ‎ • ‎ There is reverb       
‎ ‎ ‎ • ‎ Or there is noise
             
As you noticed, most of the issues boil down to the audio sample not being properly **clean**.

Remember, RVC is built for purely working with **clear voices only**, not other sounds.         
That's when it performs the most accurately.

So when RVC tries to handle with these noises, this anomaly happens.
***
###### ‎ 
### How do you fix it?      
1. You can remove undesired noises with an [<u>audio isolation</u>](https://aihubdocs.github.io/en/vocal-isolation--datasets/uvr5--mvsep/) software.

2. If you are doing inference, lowering the [<u>search feature ratio</u>](https://aihubdocs.github.io/en/rvc-resources/inference-settings/#search-feature-ratio-or-index-rate) can also minimize this issue.

3. Ensure your audios are in a [<u>lossless format</u>](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/) like `WAV` or `FLAC` to preserve their quality, not a lossy one like `MP3`.
***
:::content-right
||| *Did I miss anything?*        
Send any feedback [<u>here</u>](https://forms.gle/5i6hTJRVkXRohvVF9) 👈
|||
:::
