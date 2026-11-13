import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Application started")

def calculate_order(price: str, quantity: str) -> float:
    price = float(price)
    quantity = int(quantity)
    if price <= 0:
        raise ValueError("Price must be greater than 0")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    return price * quantity

test_cases = [
    ("100", "3"),
    ("49.5", "2"),
    ("abc", "2"),
    ("100", "hello"),
    ("-50", "3"),
    ("100", "0"),
]
    
for price, quantity in test_cases:
    try:
        logging.debug(f"Processing order: {price}, {quantity}")
        result = calculate_order(price, quantity)
        logging.info(f"Order calculated successfully: {result}")

    except ValueError as error:
        logging.warning(error)
