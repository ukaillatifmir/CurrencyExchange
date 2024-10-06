import random
from decimal import Decimal, ROUND_DOWN


class MockGenerator:

    def generate(self):
        # Generate the integer part (0 to 999999999999)
        integer_part = random.randint(0, 999999999999)  # Max 12 digits total

        # Generate the decimal part (0 to 999999)
        decimal_part = random.randint(0, 999999)

        # Combine integer and decimal parts, ensuring total length doesn't exceed 12
        combined_value = f"{integer_part}.{decimal_part:06d}"

        # Adjust for cases where total length exceeds 12 digits
        while len(combined_value) > 12:
            integer_part = random.randint(0, 999999999999)  # Re-generate integer part
            combined_value = f"{integer_part}.{decimal_part:06d}"

        # Convert to Decimal and round down to 6 decimal places
        decimal_value = Decimal(combined_value).quantize(Decimal('0.000000'), rounding=ROUND_DOWN)

        return decimal_value