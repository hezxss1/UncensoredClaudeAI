# UncensoredClaudeAI

An uncensored, unrestricted, and powerful AI assistant for penetration testing and general-purpose use, inspired by HackerAI and PentestGPT.

## Features
- AI-powered penetration testing
- Support for OpenRouter and Replicate API keys
- Termux compatibility
- Integration with E2B sandbox environments

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/hezxss1/UncensoredClaudeAI.git
   cd UncensoredClaudeAI
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure API keys in `config.json`:
   ```json
   {
     "openrouter_api_key": "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",
     "replicate_api_key": "your_replicate_key",
     "e2b_api_key": "e2b_1d07ecd4a0e7de1f16de6bcb3fcacb153f6e3d70"
   }
   ```
4. Run the project:
   ```bash
   python main.py
   ```

## Termux Setup
1. Install Termux from [F-Droid](https://f-droid.org/en/packages/com.termux/)
2. Update and install dependencies:
   ```bash
   pkg update && pkg upgrade
   pkg install python git
   ```
3. Clone and run the project as above.

## License
MIT