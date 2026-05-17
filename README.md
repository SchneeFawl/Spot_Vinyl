![Banner](repo_assets/Banner.gif)

<p align="center">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
    <img src="https://img.shields.io/badge/Windows-SMTC-0078D4?style=for-the-badge&logo=windows&logoColor=white" alt="Windows">
    <img src="https://img.shields.io/badge/Discord-Webhook-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord">
</p>

# 💿 About Spot_Vinyl

Spot_Vinyl is a minimalist, pixel-art desktop widget which brings a different aesthetic to your Windows workspace by displaying the current playin song.

Unlike other widgets, **Spot_Vinyl does not require a Spotify API**. It works by tapping directly into the **Windows Global System Media Transport Controls (GSMTC)** via **WinRT**. This means that it can listen to whatever Spotify is playing locally on your machine with zero configuration and zero privacy concerns regarding your Spotify account crredentials.

## 📸 Screenshots

|             Main menu              |               Settings Menu                |
| :--------------------------------: | :----------------------------------------: |
| ![Main](repo_assets/main_page.png) | ![Settings](repo_assets/settings_page.png) |

|             Discord embed              |               Discord test embed                |
| :------------------------------------: | :---------------------------------------------: |
| ![Main](repo_assets/discord_embed.png) | ![Settings](repo_assets/discord_embed_test.png) |

## 📦 Installation

1. Head over to [Releases](https://github.com/SchneeFawl/Spot_Vinyl/releases/tag/v1.0) tab
2. Download the latest `Spot_Vinyl.exe`
3. Paste that executable in a newly created folder and run it!
   (No installation required, its a portable app)

## ✨ Features

- **Zero-config setup**: Works out of the box with Spotify for Windows
- **Pixel-art aesthetic**: Custom UI built from scratch using [Aseprite](https://github.com/aseprite/aseprite)
- **Discord Webhooks**: Automatically post your current song to a Discord channel with an embed which includes a link Spotify song link
- **Intelligent Debouncing**: Skips rapid track changes (5s delay) to prevent Discord webhook spam
- **Always on Top mode**: Keep the vinyl spinning above all your other apps
- **Lightweight**: Optimized to use minimal CPU and RAM (only 45MB)

## 🛠 Development Setup

If you want to run the source code or contribute:

- **Environment**: Windows 10/11 (required for WinRT/GSMTC integration)

## 🤝 Support

- **Bugs and Suggestions**: Found a bug or have an idea? Open an [Issue](https://github.com/SchneeFawl/Spot_Vinyl/issues)
- **Questions**: Want to show off your custom themes or ask a question? Join the [Discussions](https://github.com/SchneeFawl/Spot_Vinyl/discussions)

---

Created with ♥ by SchneeFawl
