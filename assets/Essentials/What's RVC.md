---
icon: chevron-right
order: 2000
visibility:
---

``Last update: November 9, 2025``

***

## Introduction :icon-book:
***
- RVC (*Retrieval-Based Voice Conversion*) is an advanced AI **voice cloning** software based on [VITS](https://github.com/jaywalnut310/vits), developed by the [RVC-Project team](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI). It's considered the best **free & open-source** one to date.

- It was designed for desktop, requiring **great specs** to run it effectively, specially **GPU** for training models.

- Though it can be executed through the [cloud](https://docs.aihub.gg/extra/glossary/#cloud-based) & be used in **any** device, in case you don't meet the previous requirement.        

- RVC doesn't have any major *quality* improvements since 2023, since its original devs are focused on other projects, RVC is hard to optimize, and it has limitations like non speech sounds such as realistic laughing, screaming, etc. Though, there are commmunity driven Forks that try to experiment with it, mostly about adding new features and performance improvements.


***
## Forks :icon-repo-forked:
***
- A fork is a **copy** of a main GitHub Project. It aims to make a **modified version** of the project, with improvements, new features & modifications.

- RVC has quite a few forks made by the community, each one meeting different **needs** for the user, and with its pros & cons.     

- These are the main ones, along with their [cloud-based](https://docs.aihub.gg/extra/glossary/#cloud-based) counterparts:       

    {.list-icon}
    - #### :icon-chevron-right: [Mainline](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) (Original RVC)
    ###### ‎    
    {.list-icon}
    - #### :icon-repo-forked: [Applio](https://applio.org/)
        - ##### :icon-cloud: [Applio Colab](https://colab.research.google.com/github/iahispano/applio/blob/master/assets/Applio.ipynb)
        - ##### :icon-cloud: [Applio Kaggle](https://www.kaggle.com/code/deiant/applio)
        - ##### :icon-cloud: [Applio Lightning Ai](https://lightning.ai/guilhermecardoso1/studios/applio-latest?section=all&query=applio)

        
    ###### ‎  
    {.list-icon} 
    - #### :icon-repo-forked: [RVC-AI-Cover-Maker-UI](https://github.com/Eddycrack864/RVC-AI-Cover-Maker-UI)     
        - ##### :icon-cloud: [RVC-AI-Cover-Maker-UI Colab](https://colab.research.google.com/github/Eddycrack864/RVC-AI-Cover-Maker-UI/blob/main/assets/RVCAICoverMakerUI.ipynb)
        - ##### :icon-cloud: [RVC-AI-Cover-Maker-UI Kaggle](https://www.kaggle.com/code/eddycrack864/rvc-ai-cover-maker-ui)     
    ‎       
***
## FAQ :icon-question:
#### `Frequently asked questions.`
***

==- *What's the best fork?*
###### ‎       
- As explained before, it depends on your needs. It's best to try them yourself.
- For **local** users, [Applio](https://docs.aihub.gg/rvc/local/applio/) is a great starting point. For **cloud** users you can use either the [Applio Colab](https://docs.aihub.gg/rvc/cloud/applio-colab/) or [applio kaggle](https://docs.aihub.gg/rvc/cloud/applio-kaggle/).
===

==- *What are the requirements for RVC locally?*
###### ‎      
> The minimum specs vary depending if it's for training models or [inference](https://docs.aihub.gg/extra/glossary/#inference).
+++ Training
**SPEC** | **MINIMUM REQUIREMENT** | 
:---: | :---: | :---: |
GPU | NVIDIA GTX 900 Series / AMD RX580 (Mac isn't supported) | 
RAM | 6GB
Storage | 30 GB


**SPEC** | **SUGGESTED REQUIREMENT** | 
:---: | :---: | :---: |
GPU | NVIDIA RTX 20 Series or later / AMD Radeon RX 5xxx or later (Mac isn't supported) | 
VRAM | 8GB
RAM | 8GB
Storage | 30 GB


+++ Inference
**SPEC** | **MINIMUM REQUIREMENT** | 
:---: | :---: | :---: | 
RAM | 6GB
Storage | 6 GB 

**SPEC** | **SUGGESTED REQUIREMENT** | 
:---: | :---: | :---: | 
GPU | NVIDIA RTX 20 Series or later / AMD Radeon RX 5xxx or later / Apple M3 | 
RAM | 6GB
Storage | 6 GB 

+++

!!! NOTES:
- For inference, the storage requirement varies depending on the fork. It can be around 5 to 9 GB
- If you don't meet the minimum requirements, it's more convenient to use RVC on the cloud.
!!!

=== 

==- *Can I use it on my AMD GPU?*
###### ‎  
- You can, but it's going to be slower, as they don't have CUDA cores.
- So it's more convenient using RVC through the [cloud](https://docs.aihub.gg/extra/glossary/#cloud-based).
- If you're willing to use a slower version you can go ahead and follow this guide on how to get zluda working with [Applio Zluda](https://docs.aihub.gg/rvc/local/applio/#amd-on-windows-precompiled-fix).
=== 

==- *How long does it take to train?*
###### ‎      
- The total time depends on a lot of factors, like dataset length, batch size, pretrains, specs, etc.

- A 10 min [dataset](https://docs.aihub.gg/rvc/resources/dataset-isolation/) with [RMVPE](https://docs.aihub.gg/rvc/resources/inference-settings/#pitch-extraction-algorithm) may take around 1 to 2 hours.
=== 

==- *Can I run it on a Mac?*
###### ‎      
- Yes, on Macs of recent generations.
- But you can only do [inference](https://docs.aihub.gg/extra/glossary/#inference) & it's a little unstable.  
===

==- *Do I need internet to use it?*
###### ‎      
- If you're using RVC locally, no (the only exception would be Applio TTS as it uses Microsoft's Edge TTS as a base).
- If you're using it through the cloud, then yes.
===

==- *Is there a scientific paper for RVC to understand more about it?*
###### ‎      
- There isn't an official one, but there's an [unofficial complex blog](https://gudgud96.github.io/2024/09/26/annotated-rvc/) to understand how it works.
===


***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
