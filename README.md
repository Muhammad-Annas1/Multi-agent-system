# 🧠 Multi-Agent Console System (Gemini API)

A **console-based multi-agent system** using **Google Gemini API** that:
- Handles **different user queries** (Billing, Technical, General)
- Supports **agent-to-agent handoffs**
- Uses **tools with dynamic `is_enabled()` logic**
- Passes **context** between agents
- (Optional) Uses **guardrails** to block unwanted words in output

---

## 📌 Features
- **Dynamic Tool Gating**
  - `refund()` only if `is_premium_user == True`
  - `restart_service()` only if `issue_type == "technical"`
- **Automatic Handoffs**
  - Triage Agent routes query to correct specialized agent
- **Context Injection**
  - Uses `pydantic` model to pass data like `name`, `is_premium_user`, `issue_type`
- **Optional Output Guardrail**
  - Blocks output containing `"sorry"` or `"apologize"`
- **Gemini API Integration**
  - Fully uses Google Gemini LLM for AI-powered responses

---

## Agent Flow Diagram

flowchart LR
    User[User Input] --> TriageAgent
    TriageAgent -->|Billing query| BillingAgent
    TriageAgent -->|Technical query| TechnicalAgent
    TriageAgent -->|General query| GeneralAgent

    BillingAgent -->|Refund Tool| RefundAction
    TechnicalAgent -->|Restart Service Tool| RestartAction
    GeneralAgent -->|FAQ Tool| FAQAction

    RefundAction --> Output
    RestartAction --> Output
    FAQAction --> Output

## 🛠 Tech Stack

- Python

- Google Gemini API (google-generativeai)

- pydantic for data modeling

- dotenv for environment management

- asyncio for asynchronous execution


---

## 🔑 Getting Gemini API Key
1. Go to **[Google AI Studio](https://aistudio.google.com)**
2. Login with your Google account
3. Click **"Get API Key"**
4. Select **"Create API Key in new project"**
5. Copy your API key
6. Create a `.env` file in your project root and paste:


---


## Run
- python main.py


---

## Sample Output
Enable output guardrail to block apologies? (y/N): y
Multi-agent console. Type 'exit' to quit.
Enter your name: Annas

Annas> I want a refund
Are you a premium user? (y/N): y
[triage_agent] Routing to billing agent...
[billing_agent::tool:refund] Processing refund...
→ Final result: Refund processed for Annas.

---

## Note
- You will need a virtual environment to run the program





