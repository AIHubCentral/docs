---
icon: ":rocket:"
order: 3000
---

``Last update: April 1, 2026``

***
:::content-center
## Introduction
:::
- This is a [cloud-based](https://docs.aihub.gg/extra/glossary/#cloud-based) alternative to run [Wokada Tg-Develop's Fork](https://docs.aihub.gg/realtime-voice-changer/local/tg-develops-w-okada-fork/), for users without a powerful local PC GPU, via Google Colab, Kaggle, or Lightning.AI.

{{ include "cloud-services/warnings/cloud-server-audio.md" }}

{{ include "cloud-services/setups/virtual-audio-cable.md" }}

{{ include "cloud-services/start-decision.md" }}
{{ include "cloud-services/grid-cards/google-colab-card.md" }}
{{ include "cloud-services/grid-cards/kaggle-card.md" }}
{{ include "cloud-services/grid-cards/lightning-ai-card.md" }}
{{ include "cloud-services/end-decision.md" }}


***
:::content-center
### Google Colab
:::

{{ include "cloud-services/warnings/google-colab.md" }}

!!!danger Paid
You need the Google Colab Paid Tier to run this, as it uses a Web UI; otherwise, you could risk getting disconnected or banned.
!!!

- **1. Access:** Go to the [Tg-Develop Colab](https://colab.research.google.com/github/tg-develop/voice-changer/blob/master-custom/Colab_RealtimeVoiceChanger.ipynb).

- **2. Install:** Start from the top and run the first cell.
<img src="../wokada-colab-img/colab1.png" alt="Colab Install" width="900">

- **3. Second Cell:** When it finishes (it will output `Done! Proceed with the next steps`), run the second cell.
<img src="../wokada-colab-img/colab2.png" alt="Colab Second Cell" width="600">

- **4. Ngrok:** Scroll to the last cell, place your [Ngrok token](https://dashboard.ngrok.com/get-started/your-authtoken) in the `TOKEN_HERE` field.
<img src="../wokada-colab-img/colab3.png" alt="Ngrok Token" width="600">

- **5. Launch:** Run the cell. (Optional) Under the token field, you can change the region selection for lower latency. Once it finishes downloading, click the generated Ngrok link to start the Web UI.


***
:::content-center
### Kaggle
:::

{{ include "cloud-services/warnings/kaggle.md" }}

{{ include "cloud-services/setups/kaggle-account.md" }}

#### <u>Notebook Creation & Setup</u>

- **Create:** Go to [Kaggle](https://www.kaggle.com) and click **Create** then **New Notebook** at the top left. 
<img src="/img/cloud-services/kaggle-img/new.png" alt="New Notebook" width="400"> 

- **Import:** Under your session's name click **File** then **Import Notebook**.
<img src="/img/cloud-services/kaggle-img/import.png" alt="Import Notebook" width="450">     

- **Link:** In the new window, click the **Link** tab and paste the following URL: `https://github.com/tg-develop/voice-changer/blob/master-custom/Kaggle_RealtimeVoiceChanger.ipynb`. Click **Import**.
<img src="/img/cloud-services/kaggle-img/link.png" alt="Link Tab" width="700"> 

- **Settings:** In the sidebar on the right, turn on the **Internet** switch. Make sure persistence is set to **Files and variables**.

<img src="/img/cloud-services/kaggle-img/kaggle-internet.png" alt="Internet" width="250"> 

- **GPU:** Turn on T4 x2 GPUs in the Accelerator settings.
<img src="/img/cloud-services/kaggle-img/kaggle-gpu.png" alt="GPU" width="250"> 

- **Save:** (Optional) Turn on "Save version" to save your progress.
<img src="/img/cloud-services/kaggle-img/kaggle-pers.png" alt="Persistence" width="250"> 

!!!warning
Your runtime will continue draining when you're not running any cells with this option on. 
!!!

#### <u>Installation & Tunnels</u>

- **Install:** Starting from the top, run the first installation cell. When it outputs `Done! Proceed with the next steps`, run the third cell.
<img src="../wokada-kaggle-img/install-1.png" alt="Install 1" width="900"> 
<img src="../wokada-kaggle-img/install-2.png" alt="Install 2" width="600"> 

- **Ngrok:** Put your token in the last cell.
<img src="../wokada-kaggle-img/token.png" alt="Token" width="600"> 


***
:::content-center
### Lightning.AI
:::

{{ include "cloud-services/warnings/lightning-ai.md" }}

{{ include "cloud-services/setups/lightning-ai-account.md" }}

- **Studio:** Clone the [Wokada-TgDevelop-Fork Studio](https://lightning.ai/nick088/studios/wokada-tg-develop-fork).

<img src="/img/cloud-services/lightning-ai-img/lightning-ai-clone-studio.png" alt="Clone" width="300">

- **GPU:** Switch to a GPU environment (Studio Environment -> Switch To GPU).

<img src="/img/cloud-services/lightning-ai-img/gpu-setting.png" alt="GPU Settings" width="500">

- **Install:** Run the first cell to install, run the second cell to configure.

- **Tunnels:** In the third cell, choose your tunnel (Port Viewer recommended) and run it. Use the provided file drive to upload models and TensorBoard to monitor training.

- **File Management:** Use the **Teamspace Drive** button on the right sidebar to upload files.
<img src="/img/cloud-services/lightning-ai-img/teamspace-drive.png" alt="LightningAI Teamspace Drive" width="500">

- **Maintenance:** If you need to update the Program or start fresh, you can run the final cell in the notebook, "Delete everything". This will remove all downloaded files and configurations from your persistent storage, allowing for a clean installation by re-following the notebook with perhaps a changed branch variable.


***
:::content-center
## Usage
:::
Now that you have the Web UI running, the rest of the process is **identical to using a local installation.**

[!button text="Continue with the Local Guide" icon="arrow-right" target="blank"](https://docs.aihub.gg/realtime-voice-changer/local/tg-develops-w-okada-fork/#voice-models)


***
:::content-center
## Troubleshooting
:::

{{ include "troubleshooting/wokada-cloud-logs.md" }}

!!!info General Troubleshooting
Because the web interface and core server function the exact same way, most common errorsare identical to the local version.

[!button text="View Local General Troubleshooting" icon="tools" variant="secondary"](https://docs.aihub.gg/realtime-voice-changer/local/tg-develops-w-okada-fork/#troubleshooting)
!!!

{{ include "end-badge.md" }}