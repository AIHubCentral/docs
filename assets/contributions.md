---
icon: code-of-conduct
---

``Last update: March 7, 2026``  

***

## Contributions :icon-code-of-conduct:
- We'll appreciate any **feedback**, big or small. If you wish to contact anyone who worked on this you can find them in <u>[AI Hub](https://discord.gg/aihub)</u>.
- Leave **suggestions** in the <u>[#suggestions](https://discord.com/channels/1159260121998827560/1159516963014451302)</u> channel. 
- To **report issues** use <u>[#ai-help-forum](https://discord.com/channels/1159260121998827560/1192011222023950368)</u>. You can also send issues to our <u>[GitHub Repository](https://github.com/AIHubCentral/docs)</u>.
- If you would like to contribute to our docs please check <u>[How to Contribute to the AI HUB Docs](https://docs.aihub.gg/contributions/#how-to-contribute-to-the-ai-hub-docs)</u>. 

---

## How to Contribute to the AI HUB Docs

### Introduction:
We use [Retype](https://retype.com/) for building our docs, checking their docs and resources about them can be helpful. It's markdown with special effects simply.

### Environment:
You can use 2 type of environments to start editing the docs:

#### A. GitHub Codespaces (Cloud)

**Pros:** 
- Easy to use
- Doesn't fill your storage up

**Cons:**
- Limited time (GitHub Free personal accounts receive 120 core hours/month; Pro/Student receive 180 core hours/month).

**How:**
1. [Make a new GitHub Codespace](https://github.com/codespaces).
2. Click new codespace, select the docs repo and click **Create Codespace**.
3. In the Terminal, insert: `npm install retypeapp --global`
4. In the `retype.yml` file, insert a `#` before the docs link in `url: `, so it will look like `url: # https://docs.aihub.gg/`.
5. In the terminal, insert: `retype start`
6. Press the green button of the popup or click the **Ports** tab and check the 5001 port. You should be able to see the preview.
7. Do your changes, remove the `#` from the `retype.yml`, then commit & PR.
8. Delete the codespace when finished to save on usage.

#### B. Local

**Pros:**
- Unlimited time

**Cons:**
- Can take up storage
- Slightly harder to set up

**How:**
1. [Make a Fork of the AI Hub Docs](https://github.com/AIHubCentral/docs/fork)
2. [Install Git](https://git-scm.com/downloads)
3. [Install Node.js with npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
4. Open your terminal/cmd/powershell, and type: `git clone <your-fork-url-here>`
5. In the Terminal, insert: `npm install retypeapp --global`
6. In the `retype.yml` file, insert a `#` before the docs link in `url: `, so it will look like `url: # https://docs.aihub.gg/`.
7. In the terminal, insert: `retype start`
8. Press the green button of the popup or click the **Ports** tab and check the 5001 port. You should be able to see the preview.
9. Do your changes, remove the `#` from the `retype.yml`, then commit & PR.


***
###### ‎
:::content-center
#### `You have reached the end.`

:::
