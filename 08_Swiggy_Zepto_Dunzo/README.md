# 🤖 AI Delivery Assistant — Telegram Bot
### Powered by N8N + GPT-4o | Swiggy 🍔 · Zepto 🛒 · Dunzo 🟣

![N8N](https://img.shields.io/badge/Built%20with-N8N-orange?style=for-the-badge&logo=n8n)
![OpenAI](https://img.shields.io/badge/GPT--4o-OpenAI-412991?style=for-the-badge&logo=openai)
![Telegram](https://img.shields.io/badge/Telegram-Bot-2CA5E0?style=for-the-badge&logo=telegram)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📌 Project Overview

A fully automated **AI-powered Telegram Bot** that acts as a personal delivery assistant — allowing users to place orders across **Swiggy**, **Zepto**, and **Dunzo** through a single conversational interface on Telegram.

Built entirely using **N8N (no-code automation)** and **OpenAI GPT-4o**, this bot understands natural language, collects order details step by step, and confirms structured orders — all without any coding required.

---

## ✨ Features

- 🍔 **Swiggy** — Order food from any restaurant
- 🛒 **Zepto** — Order groceries & essentials in under 10 minutes
- 🟣 **Dunzo** — Order from any store OR send parcels via Pick & Drop
- 🧠 **Conversation Memory** — Remembers context per user session
- 🤖 **AI Intent Routing** — Automatically picks the right app based on what user asks
- ❓ **Smart Missing Detail Detection** — Asks for missing info one question at a time
- ✅ **Order Confirmation Summary** — Clean structured summary before every order
- 💬 **Natural Language** — Users type freely, no commands needed
- 📲 **Telegram Native** — Works on mobile, desktop, any Telegram client

---

## 🏗️ Architecture

```
Telegram User
     │
     ▼
┌─────────────────────┐
│   Telegram Trigger   │  ← Listens for incoming messages
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│    AI Agent Node     │  ← GPT-4o brain with memory
│  (N8N LangChain)    │
└──────┬──────┬───────┘
       │      │
  ┌────┘  ┌───┘
  │       │
  ▼       ▼
Tools connected to AI Agent:
  │
  ├── 🍔 Swiggy Sub Workflow Tool
  │       └── When Executed Trigger → Extract Input
  │           → OpenAI (Order Processor) → Format Reply
  │
  ├── 🛒 Zepto Sub Workflow Tool
  │       └── When Executed Trigger → Extract Input
  │           → OpenAI (Order Processor) → Format Reply
  │
  └── 🟣 Dunzo Sub Workflow Tool
          └── When Executed Trigger → Extract Input
              → OpenAI (Order Processor) → Format Reply
                    │
                    ▼
          ┌─────────────────────┐
          │  Send Text Message   │  ← Reply back to Telegram user
          │  (Telegram Node)     │
          └─────────────────────┘
```

---

## 📁 Project Structure

```
📦 ai-delivery-telegram-bot
 ┣ 📜 README.md
 ┣ 📂 workflows
 ┃ ┣ 📄 swiggy_MAIN_workflow.json       ← Main AI Agent workflow
 ┃ ┣ 📄 swiggy_SUB_workflow.json        ← Swiggy order processor
 ┃ ┣ 📄 zepto_SUB_workflow.json         ← Zepto order processor
 ┃ ┗ 📄 dunzo_SUB_workflow.json         ← Dunzo order processor
 ┣ 📂 prompts
 ┃ ┣ 📄 main_system_prompt.md           ← AI Agent combined system prompt
 ┃ ┣ 📄 swiggy_sub_prompt.md            ← Swiggy sub-workflow prompt
 ┃ ┣ 📄 zepto_sub_prompt.md             ← Zepto sub-workflow prompt
 ┃ ┗ 📄 dunzo_sub_prompt.md             ← Dunzo sub-workflow prompt
 ┗ 📂 docs
   ┗ 📄 setup-guide.md                  ← Step by step setup instructions
```

---

## 🚀 Getting Started

### Prerequisites

| Tool | Purpose |
|------|---------|
| [N8N](https://n8n.io) | Workflow automation platform |
| [OpenAI API Key](https://platform.openai.com) | GPT-4o for AI processing |
| [Telegram Bot Token](https://t.me/BotFather) | Create a bot via @BotFather |

---

### Step 1 — Create Your Telegram Bot

1. Open Telegram → search **@BotFather**
2. Send `/newbot` → follow the steps
3. Copy the **Bot Token** (looks like `123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ`)

---

### Step 2 — Set Up N8N Credentials

In N8N → **Credentials** → add:

| Credential | Name to Use | Details |
|------------|-------------|---------|
| Telegram API | `Telegram Bot Account` | Paste your Bot Token |
| OpenAI API | `OpenAI API Key` | Paste your OpenAI key |

---

### Step 3 — Import Sub Workflows (Import in this order)

> ⚠️ Sub workflows MUST be imported and activated before the MAIN workflow.

1. Go to N8N → **New Workflow** → `⋮` menu → **Import from JSON**
2. Import `swiggy_SUB_workflow.json` → Save → **Activate** ✅
3. Import `zepto_SUB_workflow.json` → Save → **Activate** ✅
4. Import `dunzo_SUB_workflow.json` → Save → **Activate** ✅

---

### Step 4 — Import MAIN Workflow

1. Import `swiggy_MAIN_workflow.json`
2. Save as `AI Delivery Assistant - MAIN`

---

### Step 5 — Configure AI Agent Node

Click the **AI Agent** node and set:

| Field | Value |
|-------|-------|
| Model | OpenAI Chat Model (GPT-4o) |
| Temperature | 0.4 |
| Max Tokens | 600 |
| System Message | Paste from `prompts/main_system_prompt.md` |
| Text (User Message) | `={{ $json.message.text }}` |

---

### Step 6 — Configure Simple Memory Node

| Field | Value |
|-------|-------|
| Session ID Type | From Input |
| Session Key | `={{ $('Telegram Trigger').item.json.message.chat.id }}` |
| Context Window | 10 |

---

### Step 7 — Link Sub Workflow Tools

For each tool connected to the AI Agent, click it and configure:

**Swiggy Tool:**
| Field | Value |
|-------|-------|
| Name | `Swiggy Sub Workflow Tool` |
| Workflow | `Swiggy Agent - SUB Workflow` |
| Response Property | `output` |
| Description | Use when user wants to order food from a restaurant via Swiggy. Call after collecting: restaurant name, food items with quantity, full delivery address, contact number. |

**Zepto Tool:**
| Field | Value |
|-------|-------|
| Name | `Zepto Workflow Tool` |
| Workflow | `Zepto Agent - SUB Workflow` |
| Response Property | `output` |
| Description | Use when user wants to order groceries, essentials, dairy, snacks or household items via Zepto for under 10-minute delivery. Call after collecting: product list with quantity, delivery pincode or area, contact number. |

**Dunzo Tool:**
| Field | Value |
|-------|-------|
| Name | `Dunzo Workflow Tool` |
| Workflow | `Dunzo Agent - SUB Workflow` |
| Response Property | `output` |
| Description | Use when user wants to order from any store (groceries, medicines, alcohol, pet supplies) OR send a parcel/document via Dunzo Pick & Drop. Call after collecting all required details. |

---

### Step 8 — Activate MAIN Workflow & Test 🎉

Activate the MAIN workflow and test in Telegram:

| Test Message | Expected Result |
|---|---|
| `hi` | Welcome menu showing all 3 apps |
| `Order 2 Mutton Biryani from Hotel Annachi, Anna Nagar Chennai, 9980077567` | Swiggy order summary + confirmation |
| `Get 2 litres milk and eggs, Koramangala Bengaluru, 9876543210` | Zepto order summary + confirmation |
| `Order Dolo 650 from Apollo Pharmacy, Anna Nagar Chennai, 9980077567` | Dunzo order summary + confirmation |
| `Order tablet from Apollo` | Bot asks: "Which tablet do you need?" |
| `Send my documents from T Nagar to Adyar` | Dunzo Pick & Drop flow |

---

## 🧠 How the AI Routing Works

```
User: "Get me milk and bread"
         │
         ▼
   AI Agent reads intent
         │
         ▼
   Matches → ZEPTO (groceries)
         │
         ▼
   Asks: "What's your delivery area/pincode?"
         │
         ▼
   Asks: "What's your contact number?"
         │
         ▼
   Shows Zepto Order Summary
         │
         ▼
   User confirms → Calls Zepto Sub Workflow Tool
         │
         ▼
   ✅ Order Confirmed reply sent to Telegram
```

---

## 💬 Sample Conversations

**Swiggy Order:**
```
User: Order biryani from Annachi Hotel
Bot:  How many portions would you like?
User: 2 Mutton Biryani and 1 Mutton Chukka
Bot:  What's the delivery address?
User: Anna Nagar, Chennai
Bot:  Contact number?
User: 9980077567
Bot:  🧾 Swiggy Order Summary:
      🏪 Restaurant: Annachi Hotel
      📍 Delivering to: Anna Nagar, Chennai
      🍽️ Items:
         - Mutton Biryani x2
         - Mutton Chukka x1
      📞 Contact: 9980077567
      ⏱️ Estimated Delivery: 30–45 minutes
      Shall I confirm this order? ✅
User: Yes
Bot:  ✅ Order Confirmed! ...
```

**Dunzo (Missing Detail Handling):**
```
User: Order tablet from Apollo
Bot:  Which tablet do you need? Please share the exact name.
User: Dolo 650, 2 strips
Bot:  What's the delivery address?
User: No 11, Sai Apartment, Anna Nagar, Chennai
Bot:  Contact number?
User: 9980077567
Bot:  🧾 Dunzo Order Summary:
      🏪 Store: Apollo Pharmacy
      📍 Delivering to: No 11, Sai Apartment, Anna Nagar, Chennai
      🛍️ Items: - Dolo 650 x2 strips
      📞 Contact: 9980077567
      ⏱️ Estimated Delivery: 30–45 minutes
      Shall I confirm this order? ✅
```

---

## 🔮 Roadmap — Upcoming Features

- [ ] 🟡 **Blinkit** sub-workflow (groceries, North India focus)
- [ ] 🚛 **Porter** sub-workflow (bike/truck pickup & drop)
- [ ] 📊 **Google Sheets Logging** — auto-log every order
- [ ] 📣 **Order Status Updates** — push notifications after X minutes
- [ ] 👤 **User Profiles** — save default address via Airtable
- [ ] ⌨️ **Telegram Inline Buttons** — tap instead of type
- [ ] 🌐 **Multi-language** — Tamil, Hindi, Telugu support
- [ ] 🔔 **Confirmation Receipts** — formatted PDF receipt

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Automation | N8N (self-hosted or cloud) |
| AI Model | OpenAI GPT-4o |
| Memory | N8N LangChain Buffer Window Memory |
| Messaging | Telegram Bot API |
| Orchestration | N8N AI Agent (LangChain) |
| Sub-workflows | N8N Execute Workflow nodes |

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/add-blinkit`
3. Commit your changes: `git commit -m 'Add Blinkit sub workflow'`
4. Push to the branch: `git push origin feature/add-blinkit`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify and distribute.

---

## 👨‍💻 Author

Built with ❤️ using N8N + OpenAI GPT-4o + Telegram Bot API

> ⭐ If this project helped you, please give it a star on GitHub!
