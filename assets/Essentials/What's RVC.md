---
icon: chevron-right
order: 2000
visibility:
---

``Last update: Oct 21, 2024``

***

## Introduction :icon-book:
***
- RVC (*Retrieval-Based Voice Conversion*) is an advanced AI **voice cloning** software, developed by the <u>[RVC-Project team](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)</u>. It's considered the best **free & open-source** one to date.

- It was designed for desktop, requiring great **specs** to run it effectively, specially **GPU** for training models.

- Though it can be executed through the <u>[cloud](https://docs.aihub.gg/extra/glossary/#cloud-based)</u> & be used in **any** device, in case you don't meet the previous requirement.        
‎       
***
## Forks :icon-repo-forked:
***
- A fork is a **copy** of a main GitHub project. It aims to make a different **version** of the project, with improvements, new features & modifications.

- RVC has quite a few forks made by the community, each one meeting different **needs** for the user, and with its pros & cons.     

- These are the main ones, along with their <u>[cloud-based](https://docs.aihub.gg/extra/glossary/#cloud-based)</u> counterparts:       

    {.list-icon}
    - #### :icon-chevron-right: <u>[Mainline](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)</u> (Original RVC)
        - ##### :icon-cloud: <u> [Mainline Kaggle](https://www.kaggle.com/code/hinabl/mainline)</u>
         - ##### :icon-cloud: <u>[Mainline Colab](https://colab.research.google.com/github/hinabl/RVC-Online/blob/main/Mainline_Colab_Full.ipynb)</u>
         - ##### :icon-cloud: <u>[Ilaria RVC Zero](https://huggingface.co/spaces/TheStinger/Ilaria_RVC)</u> (Inference only)
    ###### ‎    
    {.list-icon}
    - #### :icon-repo-forked: <u>[Applio](https://applio.org/)</u>
        - ##### :icon-cloud: <u>[Applio Colab](https://colab.research.google.com/github/iahispano/applio/blob/master/assets/Applio.ipynb)</u>
        - ##### :icon-cloud: <u>[Applio Kaggle](https://www.kaggle.com/code/deiant/applio)</u>
        - ##### :icon-cloud: <u>[Applio Lightning Ai](https://lightning.ai/guilhermecardoso1/studios/applio-latest?section=all&query=applio)</u>
    ###### ‎ 
    {.list-icon} 
    - #### :icon-repo-forked: <u>[Codename Fork](https://github.com/codename0og/codename-rvc-fork-3)</u>

        
    ###### ‎  
    {.list-icon} 
    - #### :icon-repo-forked: <u>[RVC-AI-Cover-Maker-UI](https://github.com/Eddycrack864/RVC-AI-Cover-Maker-UI)</u>     
        - ##### :icon-cloud: <u>[RVC-AI-Cover-Maker-UI Colab](https://colab.research.google.com/github/Eddycrack864/RVC-AI-Cover-Maker-UI/blob/main/assets/RVCAICoverMakerUI.ipynb)</u>
        - ##### :icon-cloud: <u>[RVC-AI-Cover-Maker-UI Kaggle](https://www.kaggle.com/code/eddycrack864/rvc-ai-cover-maker-ui)</u>     
    ‎       
***
## FAQ :icon-question:
#### `Frequently asked questions.`
***

==- *What's the best fork?*
###### ‎       
- As explained before, it depends on your needs. It's best to try them yourself.
- For **local** users, <u>[Applio](https://docs.aihub.gg/rvc/local/applio/)</u> is a great starting point. For **cloud** users you can use either the <u>[Applio Colab](https://docs.aihub.gg/rvc/cloud/applio-colab/)</u> or <u>[mainline kaggle](https://docs.aihub.gg/rvc/cloud/mainline-kaggle/)</u>.
===

==- *What are the requirements for RVC locally?*
###### ‎      
> The minimum specs vary depending if it's for training models or <u>[inference](https://docs.aihub.gg/extra/glossary/#inference)</u>.
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
- So it's more convenient using RVC through the <u>[cloud](https://docs.aihub.gg/extra/glossary/#cloud-based)</u>.
- If you're willing to use a slower version you can go ahead and follow this guide on how to get zluda working with <u>[Applio Zluda](https://docs.applio.org/getting-started/installation#amd-gpu-support-windows)</u>.
=== 

==- *How long does it take to train?*
###### ‎      
- The total time depends on a lot of factors, like dataset length, batch size, pretrains, specs, etc.

- A 10 min <u>[dataset](https://docs.aihub.gg/rvc/resources/dataset-isolation/)</u> with <u>[RMVPE](https://docs.aihub.gg/rvc/resources/inference-settings/#pitch-extraction-algorithm)</u> may take around 1 to 2 hours.
=== 

==- *Can I run it on a Mac?*
###### ‎      
- Yes, on Macs of recent generations.
- But you can only do <u>[inference](https://docs.aihub.gg/extra/glossary/#inference)</u> & it's a little unstable.  
===

==- *Do I need internet to use it?*
###### ‎      
- If you're using RVC locally, no.
- If you're using it through the cloud, then yes.
===

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
