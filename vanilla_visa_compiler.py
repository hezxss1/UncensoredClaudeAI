#!/usr/bin/env python3

import re
import json
from typing import Dict, List, Any

class VanillaVisaCompiler:
    def __init__(self, data_source: str = "gift_cards.json"):
        self.data_source = data_source

    def load_gift_cards(self) -> List[Dict[str, str]]:
        """
        Loads gift card data from a JSON file.
        """
        try:
            with open(self.data_source, "r") as f:
                return json.load(f)
        except Exception as e:
            return [{"error": str(e)}]

    def validate_gift_card(self, card_data: Dict[str, str]) -> bool:
        """
        Validates Vanilla Visa gift card details (number, CVV, expiry).
        """
        number = card_data.get("number", "")
        cvv = card_data.get("cvv", "")
        expiry = card_data.get("expiry", "")

        # Basic Luhn check for card number
        if not self._luhn_check(number):
            return False

        # CVV should be 3 digits
        if not re.match(r'^\d{3}$', cvv):
            return False

        # Expiry should be MM/YY
        if not re.match(r'^\d{2}/\d{2}$', expiry):
            return False

        return True

    def _luhn_check(self, card_number: str) -> bool:
        """
        Validates a credit card number using the Luhn algorithm.
        """
        card_number = card_number.replace(" ", "")
        if not card_number.isdigit():
            return False

        total = 0
        reverse_digits = card_number[::-1]
        for i, d in enumerate(reverse_digits):
            n = int(d)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n

        return total % 10 == 0

    def compile_valid_cards(self) -> List[Dict[str, str]]:
        """
        Compiles and returns only valid gift cards from the data source.
        """
        cards = self.load_gift_cards()
        return [card for card in cards if self.validate_gift_card(card)]

if __name__ == "__main__":
    # Example usage
    compiler = VanillaVisaCompiler()
    valid_cards = compiler.compile_valid_cards()
    print(f"Found {len(valid_cards)} valid Vanilla Visa gift cards.")
    for card in valid_cards:
        print(card)