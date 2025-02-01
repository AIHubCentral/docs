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

- Though it can be executed through the <u>[cloud](https://docs.ai-hub.wtf/extra/glossary/#cloud-based)</u> & be used in **any** device, in case you don't meet the previous requirement.        
‎       
***
## Forks :icon-repo-forked:
***
- A fork is a **copy** of a main GitHub project. It aims to make a different **version** of the project, with improvements, new features & modifications.

- RVC has quite a few forks made by the community, each one meeting different **needs** for the user, and with its pros & cons.     

- These are the main ones, along with their <u>[cloud-based](https://docs.ai-hub.wtf/extra/glossary/#cloud-based)</u> counterparts:       

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
        - ##### :icon-cloud: <u>[Applio Lighting Ai](https://lightning.ai/guilhermecardoso1/studios/applio-latest?section=all&query=applio)</u>
    ###### ‎ 
    {.list-icon} 
    - #### :icon-repo-forked: <u>[Codename Fork](https://github.com/codename0og/codename-rvc-fork-3)</u>
    ###### ‎   
    {.list-icon}
    - #### :icon-repo-forked: <u>[Mangio](https://github.com/Mangio621/Mangio-RVC-Fork)</u>
        
    ###### ‎  
    {.list-icon} 
    - #### :icon-repo-forked: <u>[AICoverGen](https://github.com/SociallyIneptWeeb/AICoverGen)</u>     
        - ##### :icon-cloud: <u>[AICoverGen NO UI](https://colab.research.google.com/drive/1u1brjK8IZt647UsbZuGYfW29oFM2I4tk?usp%3Dsharing&sa=D&source=editors&ust=1704303145687891&usg=AOvVaw3M9tmokG80RXF-GD1LJqCL)</u>
        - ##### :icon-cloud: <u>[AICoverGen UI](https://colab.research.google.com/github/hinabl/AICoverGen-Colab/blob/main/Hina_Mod_AICoverGen_colab.ipynb)</u>     
    ‎       
***
## FAQ :icon-question:
#### `Frequently asked questions.`
***

==- *What's the best fork?*
###### ‎       
- As explained before, it depends on your needs. It's best to try them yourself.
- For **local** users, <u>[Applio](https://docs.ai-hub.wtf/rvc/local/applio/)</u> is a great starting point. For **cloud** users you can use either the <u>[Applio Colab](https://docs.ai-hub.wtf/rvc/cloud/applio-colab/)</u> or <u>[mainline kaggle](https://docs.ai-hub.wtf/rvc/cloud/mainline-kaggle/)</u>.
===

==- *What are the requirements for RVC locally?*
###### ‎      
> The minimum specs vary depending if it's for training models or <u>[inference](https://docs.ai-hub.wtf/extra/glossary/#inference)</u>.
+++ Training
**SPEC** | **REQUIREMENT** | 
:---: | :---: | :---: |
GPU | NVIDIA RTX 1060 / AMD RX5700 | 
RAM | 6GB
Storage | 30 GB

+++ Inference
**SPEC** | **REQUIREMENT** | 
:---: | :---: | :---: | 
RAM | 6GB
Storage | 6 GB 

+++

!!! NOTES:
- For inference, the storage requirement varies depending on the fork. It can be around 5 to 9 GB
- If you don't meet these requirements, it's more convenient to use RVC on the cloud.
!!!

=== 

==- *Can I use it on my AMD GPU?*
###### ‎  
- You can, but it's going to be slower, as they don't have CUDA cores.
- So it's more convenient using RVC through the <u>[cloud](https://docs.ai-hub.wtf/extra/glossary/#cloud-based)</u>.
- If you're willing to use a slower version you can go ahead and follow this guide on how to get zluda working with <u>[Applio](https://docs.applio.org/getting-started/installation#amd-gpu-support-windows)</u>.
=== 

==- *How long does it take to train?*
###### ‎      
- The total time depends on a lot of factors, like dataset length, batch size, pretrains, specs, etc.

- A 10 min <u>[dataset](https://docs.ai-hub.wtf/rvc/resources/dataset-isolation/)</u> with <u>[RMVPE](https://docs.ai-hub.wtf/rvc/resources/inference-settings/#pitch-extraction-algorithm)</u> may take around 1 to 2 hours.
=== 

==- *Can I run it on a Mac?*
###### ‎      
- Yes, on Macs of recent generations.
- But you can only do <u>[inference](https://docs.ai-hub.wtf/extra/glossary/#inference)</u> & it's a little unstable.  
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

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/contributions/)
:::
