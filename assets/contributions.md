---
icon: code-of-conduct
order: 90
---

``Last update: March 8, 2026``  

# Contributions :icon-code-of-conduct:

👍🎉 **Thank you for considering contributing to the AI HUB Docs!** 🤖🌍

We welcome contributions from everyone, whatever their level of expertise. By contributing, you're helping us improve our guides and promoting the growth of the AI community worldwide. 

To ensure a smooth collaboration experience, please review the following guidelines.

---

## Code of Conduct & Ethics :icon-shield:
AI HUB follows a strict **[Code of Conduct](https://github.com/AIHubCentral/docs/blob/main/.github/CODE_OF_CONDUCT.md)** that establishes standards for respectful and inclusive participation.
* **Ethical Use:** We strictly prohibit the use of our guides for illegal activities, scamming, catfishing, and any form of fraud. 
* **Respect:** We ask all contributors to adhere to these guidelines, show empathy, and respect different opinions when participating in AI HUB projects.

---

## Issues & Feedback :icon-comment-discussion:
If you don't want to write code/markdown but still want to help, we appreciate any feedback!
- **Suggestions:** Leave suggestions in the [#suggestions](https://discord.com/channels/1159260121998827560/1159516963014451302) channel. 
- **Report Issues/Bugs:** Use the [#ai-help-forum](https://discord.com/channels/1159260121998827560/1192011222023950368) or open an Issue on our [GitHub Repository](https://github.com/AIHubCentral/docs/issues).
- **Direct Contact:** Reach out to **@eddycrack864** in the [AI Hub Discord](https://discord.gg/aihub).

---

## How to Contribute to the Docs :icon-tools:

We use **[Retype](https://retype.com/)** for building our docs. It's simply Markdown with special effects. You can use two types of environments to start editing the docs:

### A. GitHub Codespaces (Cloud - Recommended)
**Pros:** Easy to use, doesn't take up local storage.
**Cons:** Limited free time per month.

1. Navigate to our [GitHub Repository](https://github.com/AIHubCentral/docs) and Fork it.
2. Go to[GitHub Codespaces](https://github.com/codespaces), click **New codespace**, select your forked repo, and click **Create Codespace**.
3. Create a new branch for your edits: `git checkout -b your-branch-name`
4. In the Terminal, insert: `npm install retypeapp --global`
5. In the `retype.yml` file, insert a `#` before the docs link in `url: `, so it looks like `url: # https://docs.aihub.gg/`. *(This allows local previews to route correctly).*
6. In the terminal, insert: `retype start`
7. Press the green button on the popup or click the **Ports** tab and check the `5001` port to see the live preview.
8. Make your changes. When finished, **remove the `#`** from `retype.yml`.
9. Commit your changes, push to your branch, and open a Pull Request (PR).
10. *Delete the codespace when finished to save on usage.*

### B. Local Environment
**Pros:** Unlimited time.
**Cons:** Takes up storage, slightly harder to set up.

1. [Make a Fork of the AI Hub Docs](https://github.com/AIHubCentral/docs/fork).
2. [Install Git](https://git-scm.com/downloads) and [Install Node.js with npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).
3. Open your terminal/cmd/powershell, and clone your fork: `git clone <your-fork-url-here>`
4. Navigate into the folder and create a branch: `git checkout -b your-branch-name`
5. In the Terminal, insert: `npm install retypeapp --global`
6. In the `retype.yml` file, insert a `#` before the docs link in `url: `, so it looks like `url: # https://docs.aihub.gg/`.
7. In the terminal, insert: `retype start` and open `localhost:5001` in your browser.
8. Make your changes. When finished, **remove the `#`** from `retype.yml`.
9. Commit your changes, push to your fork, and submit a PR.

---

## Pull Request Guidelines :icon-git-pull-request:
When submitting a pull request, please ensure:
- You provide a clear and descriptive title for the PR.
- You include a summary of the changes made and why they were made.
- You reference any related GitHub issues or Discord suggestions.
- **AI-Assisted Content Policy:** You can use AI tools (LLMs/Chatbots) to help refine or reword your contributions. However, since chatbots are not always up-to-date with every AI tool like RVC, **every piece of content must be human-reviewed** to ensure it is accurate before submitting.

---

## Current To-Do List :icon-checklist:
Looking for something to work on? Here is our current roadmap of things we need help adding or fixing:
- General Revamps
- Add some useful r3gm tools like: AICoverGen [CPU](https://huggingface.co/spaces/r3gm/AICoverGen_old_stable_cpu)/[ZeroGPU](https://huggingface.co/spaces/r3gm/AICoverGen)/[Colab](https://github.com/R3gm/AICoverGen?tab=readme-ov-file#aicovergen), [UltimateVocalRemoverWebUI CPU](https://huggingface.co/spaces/r3gm/Ultimate-Vocal-Remover-WebUI), Audio Separator [ZeroGPU](https://huggingface.co/spaces/r3gm/Audio_separator)/[Colab](https://github.com/R3gm/Audio_separator_ui?tab=readme-ov-file#audio-separator), [RVC Voice Model Finder](https://huggingface.co/spaces/r3gm/Model_Voice_Finder). Need to check which is still working.
- Add the other [Mainline Download methods](<https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/main/docs/en/README.en.md>) (AMD/Intel Windows, AMD Linux, Intel Linux) and more info https://discord.com/channels/1159260121998827560/1159290096458149938/1403086698895638570, https://discord.com/channels/1159260121998827560/1159290096458149938/1419361265314431067.
- Update TTS Section constantly with new tools. The GPT-SoVITS Guide is included.
- Add more to the Image Gen Section.
- Add and update other AI stuff, such as LLMs.
- Adapt all guides in the #guides discord channel to the Docs, to replace that channel.
- Remove/Archive Weights.gg/.com related things after its shutdown on March 31st 2026.

---

## Communication :icon-people:
We value open and transparent communication. 
- **Website:** [docs.aihub.gg](https://docs.aihub.gg)
- **Discord:** [AI HUB](https://discord.gg/aihub)
- **Twitter:**[@AiHubCentral](https://twitter.com/AiHubCentral)

***
###### ‎
:::content-center
#### `You have reached the end.`
:::