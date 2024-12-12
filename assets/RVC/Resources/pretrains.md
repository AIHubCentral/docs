---
icon: chevron-right
order: 6000
---

``Last update: Oct 23, 2024``
‎             
***
###### ‎ 
### Introduction        
Pretrains are an integral part of making a model, they are basically models that have been trained with many different types of voices, genders, ages, languages, manor of speech and are much longer then normal models. The objective of pretrains is to reduce training time and increase the quality of your model.

 <img src="../pretrain-img/pretrain.png" alt="image" width="1000" height="auto">
 

- There are three types of pretrains:
     - Scratch: Trained with no previous pretrain.
     - Finetune: Trained with a pretrain.
     - Merge: Made by merging pretrains. (These are considered the worst)
***
###### ‎ 
### How do i use Pretrains?

[!badge size="xl" variant="success" text="Applio"]        
- Go into the training tab and check the 'Custom Pretrained' box and use the drop down to select the pretrain's D and G file.
     - If you dont see a pretrain in the dropdown that means you need to download a pretrain, go into the 'Downloads' tab then go to 'Download Pretrained Models' then use the dropdown to select your sample rate and what pretrain you would like to download, then finally click download.
     - If you want to upload pretrains manually go into your Applio folder then go to `rvc\models\pretraineds\pretraineds_custom` and place your D and G files there.

[!badge size="xl" text="Mainline"] 
- Asssuming you have the pretrain you want to use go into your mainline folder then go to `assets\pretrained_v2` and place you D and G files there.
- Then in the 'Train' tab near the train button you can input the location of your pretrain, replace the ending so it's the name of the pretrain you put in `pretrained_v2`. 

<img src="../pretrain-img/pretrain-mainline.png" alt="image" width="200" height="auto">

***
###### ‎ 
### Where do i find Pretrains?       
You can find all of the community made pretrains in the "pretrain-models" channel in AI HUB. 

Here is a quick list of all publicly available pretrains: 

Name   | 32k Download | 40k Downaload | 48k Download
---    | ---
DMR V1 by Razer | [32k](https://huggingface.co/Razer112/DMR_Pretrain/tree/main) | - | - 
Itaila V1.0 by Ilaria | [32k](https://huggingface.co/TheStinger/itaila/tree/main) | - | - 
IMA by Loren85 | [32k](https://huggingface.co/Loren85/IMA-TEST-V1/tree/main) | - | - 
KLM 4.1 by SeoulStreamingStation | [32k](https://huggingface.co/SeoulStreamingStation/KLM4.1/tree/main) | - | [48k](https://huggingface.co/SeoulStreamingStation/KLM4.1/tree/main) 
KLM 4.2 by SeoulStreamingStation | - | [40k](https://huggingface.co/SeoulStreamingStation/KLM4.2_TestVersion/tree/main) | - 
KLM BeatzForge by SeoulStreamingStation | [32k](https://huggingface.co/SeoulStreamingStation/KLM_BEATMASTER/tree/main) | - | [48k](https://huggingface.co/SeoulStreamingStation/KLM_BEATMASTER/tree/main) 
Nanashi V1.7 by shiromiya | [32k](https://huggingface.co/shiromiya/nanashi-pretrain/tree/main/v1.7) | - | - 
Nanashi Anime v1 by shiromiya | [32k](https://huggingface.co/shiromiya/nanashi-pretrain/tree/main/v1_anime) | - | - 
Ov2 Super by SimplCup | [32k](https://huggingface.co/poiqazwsx/Ov2Super32kfix/tree/main) | [40k](https://huggingface.co/ORVC/Ov2Super/tree/main) | [48k](https://huggingface.co/ORVC/Ov2Super/tree/main) 
RIN_E3 by MUSTAR | - | [40k](https://huggingface.co/MUSTAR/RIN_E3/tree/main) | - 
Rigel by MUSTAR | [32k](https://huggingface.co/MUSTAR/Rigel-rvc-base-pretrained-model/tree/main/Rigel_32k_Base_and_FineTuned/FineTuned-model_32k_fp32) | [40k](https://huggingface.co/MUSTAR/Rigel-rvc-base-pretrained-model/tree/main/Rigel_40k_Base_and_FineTuned/FineTuned-model_40k/Alpha) | - 
SingerPreTrain by Sztef | [32k](https://huggingface.co/Sztef/SingerPreTrained/tree/main/update) | - | - 
Snowie by MUSTAR | - | [40k](https://huggingface.co/MUSTAR/SnowyRuPretrain_EnP_40k/tree/main) | [48k](https://huggingface.co/MUSTAR/SnowyRuPretrain_EnP_48k/tree/main) 
SnowieV3 X RIN_E3 by MUSTAR | - | [40k](https://huggingface.co/MUSTAR/SnowieV3.1-X-RinE3-40K/tree/main) | - 
SnowieV3.1 by MUSTAR | [32k](https://huggingface.co/MUSTAR/SnowieV3.1-32k/tree/main) | [40k](https://huggingface.co/MUSTAR/SnowieV3.1-40k/tree/main) | [48k](https://huggingface.co/MUSTAR/SnowieV3.1-48k/tree/main) 
TITAN by blaise-tk | [32k](https://huggingface.co/blaise-tk/TITAN/tree/main/models/medium/32k/pretrained) | [40k](https://huggingface.co/blaise-tk/TITAN/tree/main/models/medium/40k/pretrained) | [48k](https://huggingface.co/blaise-tk/TITAN/tree/main/models/medium/48k/pretrained) 
UKA by PlasmaTi | [32k](https://huggingface.co/Plasmati/Pretrains/tree/main) | - | - 

***
###### ‎ 
### How do i make Pretrain?      
Creating a pretrain is pretty much the same as training a normal model but the dataset is bigger and longer. 

There are two ways of making a pretrain the first being:
- From scratch which means you don't use a pretrain when training this. To make a decent from scratch pretrain you are going to need at **least** 50 hours of low, mid and high quality speech with many different speakers. 
The second way being:
- Finetuning which means you use a pretrain to train this pretrain. To make a good you are going to need at **least** 10 hours of high quality speech with many speakers.
     - The big pro of making a Finetune is that you can tailor it to anything, like you can tailor it to improve a certain language, improve accents, types of speech and more. It can even improve the graphs (like grads, g/total etc.) if trained properly.
***
###### ‎ 
### Problems        
However there are a several of problems in making a pretrain which are:
1. Harmonic distortion. This is when the harmonics of the voice start mirroring. This occurs when you train any pretrain. 
2. Noise. If your pretrain is trained with noise it will add this to any model you train with it. 
3. 8k Line. This occurs when training a model from scratch.

But thanks to the efforts of noobies he has fixed both the harmonic distortion and the 8k line in the 3.2.8 version of applio. 
***
###### ‎ 
### Misc        
This section contains miscellaneous information about pretrains. 

+++ GPU 
To make a pretrain you are going to need a pretty good GPU, because without one it will take a very long time to train. Here is a GPU tier list for training pretrains:
- S Tier:
     - H100
     - A100 (80gb and 40gb)
- A Tier:
     - L40S
     - 4090
     - 4080 (Super)
- B Tier:
     - 4070 (Ti) (Super)
     - V 100
     - 3090 (Ti)
     - A40
- C Tier:
     - 4070 (Ti)
     - 3080 (Ti)
     - 3070 (Ti)
     - P 100
- D Tier:
     - L4
     - A10, T4
     - 4060 (Ti) (8/16gb)
     - 3060 (Ti)

+++ Batch Size
Batch size refers to the amount of samples used in one iteration. Batching is used to improve performence by using parallel processing instead of individual sample processing.

For RVC this means it can influence how well temporal dependencies are captured. A small batch size like 4 and below won't capture the variability in the audio, while a high batch size like 16 and above might smooth out these variations too much causing bad graphs.

Low Batch Size:
- Pros: Less memory consumption, better generalization, less prone to overtraining.
- Cons: Slower training due to reduced parallelism, potentially less stable gradient updates.

High Batch Size:
- Pros: Faster training due to increased parallelism, more stable gradient updates, potentially better convergence.
- Cons: Higher memory requirements, might lead to overtraining if the dataset is small.

+++ Q&A
Q: What is the best pretrain? 

A: There is no "best pretrain" it all depends on your needs and what you're ok with sacrificing to get those benefits.  
+++

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/contributions/)
:::
