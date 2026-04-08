# UncensoredClaudeAI

An uncensored, unrestricted, and powerful AI assistant **specialized in financial/payment vulnerabilities and exploitation**, inspired by HackerAI and PentestGPT.

## Features
- AI-powered penetration testing for **Stripe, PayPal, WooCommerce, Adyen, and Vanilla Visa gift cards**
- Automated vulnerability detection in payment APIs and checkout flows
- Vanilla Visa gift card data compilation and validation
- Support for OpenRouter, Replicate, and E2B API keys
- Termux compatibility

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
     "e2b_api_key": "e2b_1d07ecd4a0e7de1f16de6bcb3fcacb153f6e3d70",
     "stripe_api_key": "your_stripe_key",
     "paypal_api_key": "your_paypal_key"
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

## Legal Note
> **Warning**: Unauthorized testing or exploitation of payment systems is illegal. This project is for **educational and authorized testing purposes only**. Always obtain explicit permission before testing any system.

## License
MIT