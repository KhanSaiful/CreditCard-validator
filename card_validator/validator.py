def get_issuer(number: str) ->str:

    number = "".join(number.split())
    if number.startswith('4') and len(number) == 16:
        return "Visa"

    if (number.startswith('34') or number.startswith('37')) and len(number) == 15:
        return "American Express"

    startswith_mastercard = number.startswith('51') or number.startswith('52') or number.startswith('53') or number.startswith(
        '54') or number.startswith('55')
    if startswith_mastercard and len(number) == 16:
        return "MasterCard"

    raise ValueError("Invalid Card Number")
