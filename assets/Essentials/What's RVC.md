---
icon: chevron-right
order: 2000
visibility:
---

``Last update: Mar 1, 2024``

***

## Introduction :icon-book:
***
- RVC (*Retrieval-Based Voice Conversion*) is an advanced AI **voice cloning** software, developed by the <u>[RVC-Project team](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)</u>. It's considered the best **free & open-source** one to date.

- It was designed for desktop, requiring great **specs** to run it effectively, specially **GPU** for training models (specifically **NVIDIA**).

- Though it can be executed through the <u>[cloud](https://docs.aihub.wtf/extra/glossary/#cloud-based)</u> & be used in **any** device, in case you don't meet the previous requirement.        
‎       
***
## Forks :icon-repo-forked:
***
- A fork is a **copy** of a main GitHub project. It aims to make a different **version** of the project, with improvements, new features & modifications.

- RVC has quite a few forks made by the community, each one meeting different **needs** for the user, and with its pros & cons.     

- These are the main ones, along with their <u>[cloud-based](https://docs.aihub.wtf/extra/glossary/#cloud-based)</u> counterparts:       

    {.list-icon}
    - #### :icon-chevron-right: <u>[Mainline](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)</u> (Original RVC)
    ###### ‎    
    {.list-icon}
    - #### :icon-repo-forked: <u>[Applio](https://applio.org/)</u>
        - ##### :icon-cloud: <u>[Applio Colab](https://colab.research.google.com/github/iahispano/applio/blob/master/assets/Applio.ipynb)</u>
    ###### ‎   
    {.list-icon}
    - #### :icon-repo-forked: <u>[Mangio](https://github.com/Mangio621/Mangio-RVC-Fork)</u>
        - ##### :icon-cloud: <u>[RVC Disconnected](https://colab.research.google.com/drive/1XIPCP9ken63S7M6b5ui1b36Cs17sP-NS#scrollTo=ZodNcumpg-JM)</u>
        - ##### :icon-cloud: <u>[Ilaria RVC](https://colab.research.google.com/drive/16LkwvFZeudTpUOsE_6bMjOq2qkxFo8Hr?usp=sharing)</u>
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
- For **local** users, <u>[Mainline](https://docs.aihub.wtf/rvc/local/mainline/)</u> is a great starting point. For **cloud** users, the <u>[Applio Colab](https://docs.aihub.wtf/rvc/cloud/applio-colab/)</u>.
===

==- *What are the requirements for RVC locally?*
###### ‎      
> The minimum specs vary depending if it's for training models or <u>[inference](https://docs.aihub.wtf/extra/glossary/#inference)</u>.
+++ Training
**SPEC** | **REQUIREMENT** | 
:---: | :---: | :---: |
Operating System | Windows 10 | 
GPU | NVIDIA RTX 2060ti | 
RAM | 16GB
Storage | 30 GB

+++ Inference
**SPEC** | **REQUIREMENT** | 
:---: | :---: | :---: |
Operating System | Windows 10 | 
GPU | NVIDIA GTX 1050ti | 
RAM | 8GB
Storage | 6 GB 

+++

!!! NOTES:
- For inference, the storage requirement varies depending on the fork. It can be around 5 to 9 GB
- If you don't meet these requirements, it's more convenient to use RVC on the cloud.
- Regarding GPUs, RVC is only compatible with NVIDIA. Learn below why.
!!!

=== 

==- *Can I use it on my Intel/AMD GPU?*
###### ‎  
- You can, but it's not recommended, as they aren't compatible with AI software.
- Therefore RVC will be more prone to errors & rely on your CPU, slowing down the process significantly.
- So it's more convenient using RVC through the <u>[cloud](https://docs.aihub.wtf/extra/glossary/#cloud-based)</u>.
=== 

==- *How long does it take to train?*
###### ‎      
- The total time depends on a lot of factors, like dataset length, batch size, pretrains, specs, etc.

- A 10 min <u>[dataset](https://docs.aihub.wtf/rvc/resources/datasets/)</u> with <u>[RMVPE](https://docs.aihub.wtf/rvc/resources/inference-settings/#pitch-extraction-algorithm)</u> may take around 1 to 2 hours.
=== 

==- *Can I run it on a Mac?*
###### ‎      
- Yes, on Macs of recent generations.
- But you can only do <u>[inference](https://docs.aihub.wtf/extra/glossary/#inference)</u> & it's a little unstable.  
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

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.wtf/rvc/#contributions)
:::