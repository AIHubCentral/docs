---
icon: chevron-right
order: 8000
---
 
``Last update: September 30, 2025``

***
:::content-center
<img src="..\appliocolab-img\banner.png" alt="image" width="600">

:::
###### ‎
:::content-center
## Introduction ‎
:::
- This is a <u>[cloud-based](http://docs.aihub.gg/extra/glossary/#cloud-based)</u> alternative to run [Applio](https://docs.aihub.gg/rvc/local/applio/), RVC Fork, for people who don't have a powerful local GPU. It runs via the <u>[Kaggle Service](http://docs.aihub.gg/extra/glossary/#kaggle)</u> and provides a Web User Interface.

!!!danger Kaggle Service
**Check the <u>[Kaggle Glossary](http://docs.aihub.gg/extra/glossary/#kaggle)</u> for more info on Free Tier, Limits, Verification, Pricing and other things.**
!!!


#### Pros & Cons :icon-tasklist:

==- ***Learn more***
!!! *The pros & cons are subjective to your necessities.*        
!!!
||| **✔️ PROS:**  
- Access to powerful GPUs.
- Includes 30 hours of free GPU usage per week.
- Fast processing speeds.
- TensorBoard is included for monitoring training.
- You can leave training unsupervised.  
||| ❌ **CONS**       
- Initial setup takes some time.
 
|||
===


***
###### ‎   
## Create an Account   
###### ‎   
#### 1. <u>Set up account.</u>
a. Start by making an account <u>[here](https://www.kaggle.com/account/login?phase=startRegisterTab&returnUrl=%2F)</u>.
‎  

   <img src="../kaggle-img/kaggle-sign-in.png" alt="image" width="575" height="auto">

‎  

b. Verify your account with a phone number. This is required to enable the "Internet" option in your notebooks, which is necessary for downloading models and dependencies.

 <img src="../kaggle-img/kaggle-phone.png" alt="image" width="575" height="auto">    
 

***  

###### ‎  
## Notebook Creation & Setup
###### ‎  
#### 2. <u>Clone Notebook</u>
a. Go to <u>[Kaggle](https://www.kaggle.com)</u> and click "Create" then "New Notebook" at the top left. 

   <img src="../applio-kaggle-img/new.png" alt="image" width="400" height="auto"> 

‎ 
b. Under your session's name click "File" then "Import Notebook".

   <img src="../applio-kaggle-img/import.png" alt="image" width="450" height="auto">     

‎   

c. In the new window, click the "Link" tab and paste the following URL into the box: `https://github.com/IAHispano/Applio/blob/main/assets/Applio_Kaggle.ipynb`.

   <img src="../applio-kaggle-img/link.png" alt="image" width="700" height="auto"> 

Click "Import" on the bottom right once you've done this.

d. When it's done importing it will display this text window.

   <img src="../applio-kaggle-img/settings-updated.png" alt="image" width="600" height="auto">

‎  
e. In the sidebar on the right, under "Session options", turn on the "Internet" switch. Make sure persistence is set to "Files and variables".

   <img src="../kaggle-img/kaggle-internet.png" alt="image" width="" height=""> 

f. Under "Accelerator", select the "T4 x2" GPU.           

   <img src="../kaggle-img/kaggle-gpu.png" alt="image" width="" height=""> 

‎ 
g: (Optional) To ensure your session doesn't time out during long training processes, you can enable "Save version". Go to the top right, click "Save version", and choose "Save & Run All (Commit)" from the dropdown. In the advanced settings, select "Always save output" for the notebook.

<img src="../kaggle-img/kaggle-pers.png" alt="image" width="" height=""> 

‎
!!!warning Warning
Your GPU quota will continue to be used as long as the session is active with this option. Remember to shut down the session when you are finished.
!!!
***

###### ‎   
## Installation & Tunnels Setup
###### ‎  
#### 3. <u>Run Installation Cells</u>
a. Start by running the first few cells of the notebook to install the necessary dependencies. The first cell will look like this:

   <img src="../kaggle-img/install-cell.png" alt="image" width="900" height=""> 

#### 4. <u>Configure and Run Tunnels</u>
a. The next cell is for setting up the tunneling service, which exposes the Applio interface to the internet.

!!!warning Warning about Tunneling Services Limitations
Keep in mind that all free tunneling methods, including Ngrok, have limitations and may stop working unexpectedly from one day to the next. If you get an Ngrok rate limit issue, to use it for free you could try to open the Ngrok Applio Tunnel, interact with anything to get the connection errored out issue, quickly refresh the page to see the request per minute error, then after 1 minute refresh the page and everything should be fine.
!!!

b. **Select a Tunnel:** A tunnel securely exposes the application running in your private cloud environment to the public internet. The notebook gives you four different services to do this. Choose one from the `Tunnel` dropdown menu in the code cell.

    - **Ngrok (Recommended & Default method)**
        - **How it works:** This is the default and recommended method. Ngrok is a popular service that creates secure tunnels. It requires a free account and an authentication token. Note that the free tier has limitations on request rates which can sometimes cause interruptions.
        - **Steps:**
            1. Go to the [Ngrok Dashboard](https://dashboard.ngrok.com/get-started/your-authtoken) to get your free authtoken.
            2. In the notebook cell, paste your token into the `ngrok_authtoken` field.
            3. Select "Ngrok" from the `Tunnel` dropdown.
            4. Run the cell. The public Ngrok URLs for Applio, Tensorboard, and the Filebrowser will be printed in the output once the server is ready. Click on them to access the services.

    - **Gradio + LocalTunnel (No Account & Password Protected) **
        - **How it works:** It uses Gradio's built-in tunnel for the main Applio interface and LocalTunnel for the Tensorboard and Filebrowser services. It does not require any external accounts or tokens.
        - **Steps:**
            1. Select "Gradio + LocalTunnel" from the `Tunnel` dropdown.
            2. Run the code cell. Wait for the output to show the public URLs.
            3. Click the **Gradio Public URL** to open the Applio UI.
            4. To access Tensorboard or the Filebrowser, click their respective **LocalTunnel Public URL**. A new page will ask for a password.
            5. Copy the **LocalTunnels Password** from the notebook output and paste it into the password prompt in your browser.

    - **LocalTunnel (No Account, Password Protected)**
        - **How it works:** LocalTunnel is another free service that doesn't require an account. For security, it generates a unique URL that is protected by a password.
        - **Steps:**
            1. Select "LocalTunnel" from the `Tunnel` dropdown.
            2. Run the cell.
            3. The output will display three public URLs (for Applio, Tensorboard, and Filebrowser) and a `LocalTunnels Password` below them.
            4. Click any of the URLs. A new page will ask for a password.
            5. Copy the password from the notebook output and paste it into the password prompt in your browser to access the service.

    - **Horizon (Fast, Requires Account & ID)**
        - **How it works:** Horizon is another tunneling service that requires a free account and a personal ID for authentication.
        - **Steps:**
            1. Go to the [Horizon Dashboard](https://hrzn.run/dashboard/) and sign up. On the second step of the setup, you will see a command like `hrzn login YOUR_ID`. Copy that `YOUR_ID` part.
            2. In the notebook cell, paste this ID into the `horizon_id` field.
            3. Select "Horizon" from the `Tunnel` dropdown.
            4. Run the cell. The first time you use it, the output may ask you to authorize the connection by clicking a link (`https://hrzn.run/dashboard/settings/cli-token-requests/...`). Click this link and approve the request in your Horizon dashboard.
            5. The public Horizon URLs for all services will then be printed in the output. Click them to access the UI.

c. Once you have configured your chosen tunnel, run the cell to start the services.

***

###### ‎   
## Using Applio
###### ‎  
#### 5. <u>Accessing the Links</u>

a. After the setup cell finishes running, it will output several public URLs. These links give you access to the Applio interface, Tensorboard for monitoring, and a file browser.

   <img src="../applio-kaggle-img/urls.png" alt="image" width="800" height=""> 

b. Click the **Applio Public URL** to open the user interface. For all subsequent steps, including application settings and model usage, please continue by following the Local PC guide.

[!button text="Continue with the Local PC Guide" icon="arrow-right" target="blank"](https://docs.aihub.gg/rvc/local/applio/#inference)

***

###### ‎   ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::