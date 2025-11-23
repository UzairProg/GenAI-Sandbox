# 🤖 GenAI Sandbox

A practical playground for experimenting with Generative AI concepts, prompt engineering techniques, and LLM integrations using OpenAI and Google Gemini APIs.

## 📚 Repository Structure

```
GenAI-Sandbox/
├── Basics/                          # Core GenAI concepts & fundamentals
│   ├── 01_tokenization/            # Token basics, tiktoken examples
│   ├── 02_vectorEmbedings/         # Vector embeddings & similarity
│   ├── 03_positionalEncodings/     # Positional encodings & self-attention
│   ├── 04_testingApiKeysOpenAi/    # OpenAI API setup & testing
│   └── 05_testingApiKeysGemini/    # Gemini API setup & testing
│
└── prompts/                         # Prompt engineering techniques
    ├── zeroShort.py                # Zero-shot prompting
    ├── fewShort.py                 # Few-shot prompting
    ├── cot.py                      # Chain of Thought (CoT) prompting
    ├── cotAutomated.py             # Automated CoT with step tracking
    ├── persona.py                  # Persona/role-based prompting
    ├── systemPrompt.py             # System prompt experiments
    └── structuredOutputs.py        # Structured JSON outputs
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+**
- **API Keys:**
  - [OpenAI API Key](https://platform.openai.com/api-keys)
  - [Google Gemini API Key](https://ai.google.dev/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/UzairProg/GenAI-Sandbox.git
   cd GenAI-Sandbox
   ```

2. **Create and activate virtual environment**
   ```powershell
   # Windows PowerShell
   python -m venv .venv
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   .\.venv\Scripts\Activate.ps1
   ```

   ```bash
   # Linux/macOS or Git Bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install openai python-dotenv tiktoken
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the `prompts/` directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## 📖 Topics Covered

### Basics
- **Tokenization**: How LLMs break text into tokens
- **Vector Embeddings**: Text representation in high-dimensional space
- **Positional Encodings**: How models understand word order
- **Self-Attention**: Core mechanism behind transformers
- **API Integration**: Working with OpenAI and Gemini APIs

### Prompt Engineering Techniques
- **Zero-Shot Prompting**: Direct task execution without examples
- **Few-Shot Prompting**: Learning from provided examples
- **Chain of Thought (CoT)**: Step-by-step reasoning
- **Persona Prompting**: Role-based response generation
- **System Prompts**: Controlling model behavior
- **Structured Outputs**: Generating JSON and formatted responses

## 🎯 Usage Examples

### Run a Zero-Shot Prompt
```bash
python prompts/zeroShort.py
```

### Try Chain of Thought
```bash
python prompts/cotAutomated.py
# Type your question and watch the AI think step-by-step
# Type 'exit' to quit
```

### Test API Keys
```bash
python Basics/04_testingApiKeysOpenAi/main.py
python Basics/05_testingApiKeysGemini/main.py
```

## 🛠️ Technologies Used

- **Python 3.12**
- **OpenAI API** (GPT models)
- **Google Gemini API** (Gemini 2.0 Flash)
- **tiktoken** (Tokenization)
- **python-dotenv** (Environment management)

## 📝 Notes

- All prompt engineering examples use both OpenAI and Gemini models
- The `.env` file is gitignored to protect API keys
- Each script is standalone and can be run independently
- Virtual environment (`.venv/`) is excluded from version control

## 🤝 Contributing

This is a personal learning sandbox, but feel free to:
- Fork and experiment
- Open issues for bugs or suggestions
- Share your own prompt engineering discoveries

## 📄 License

MIT License - Feel free to use this code for learning and experimentation.

## 🔗 Resources

- [OpenAI Documentation](https://platform.openai.com/docs)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Transformer Architecture Paper](https://arxiv.org/abs/1706.03762)

---

**Happy Experimenting! 🚀**
