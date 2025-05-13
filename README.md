# 🕶️ Smart Specs for the Deaf

**Smart Spectacles that display real-time subtitles on a transparent lens using speech-to-text technology — designed to empower the Deaf and Hard-of-Hearing.**
---

## 🌟 Overview

**Smart Specs for the Deaf** is an open-source assistive technology project that uses a Raspberry Pi, microphone, and transparent OLED display to convert spoken language into **real-time captions** directly in the user's field of view. Built with affordability and accessibility in mind, it allows people with hearing impairments to understand conversations on the go — **without depending on cloud services**.

---

## 🎯 Features

- ✅ **Offline Speech-to-Text** using Wav2Vec2 Through HuggingFace
- 🖥️ **Transparent OLED Display Output** for in-glass captions  
- 🎤 **Real-Time Audio Capture** via onboard microphone  
- 💬 **Minimalist UI** for clear and readable subtitles  
- 🔌 **Portable & Rechargeable** – powered by Raspberry Pi and power bank  
- 🧠 **Completely Open Source** – Build, modify, and contribute!

---

## 💡 Inspiration

While several commercial products exist, most are:
- ❌ Expensive
- ❌ Not open-source
- ❌ Cloud-reliant (raising privacy concerns)

This project is a **low-cost, offline, DIY alternative** aimed at **empowering individuals** and **promoting innovation in accessibility tech**.

---

## 🛠️ Tech Stack

| Component        | Tech Used |
|------------------|-----------|
| 🧠 Compute Unit   | Raspberry Pi 4 / Zero 2 W |
| 🗣️ Speech-to-Text | Whisper.cpp / Vosk |
| 🎤 Audio Input    | ReSpeaker / USB mic |
| 🖥️ Display        | Transparent OLED / HUD screen |
| 🧪 UI             | PyGame / Custom framebuffer renderer |
| ⚡ Power Supply   | 5V 2A Power Bank |

---

## 🧪 Getting Started

> 💡 *This is an evolving MVP project. Expect hardware integration details soon!*

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/smart-specs-for-deaf.git
cd smart-specs-for-deaf
