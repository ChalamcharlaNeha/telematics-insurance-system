from utils.logger import logger

def adjust(score):
    logger.info("Adjusting insurance premium based on risk score...")
    base = 5000
    if score > 80:
        premium = base * 1.5
    elif score > 50:
        premium = base * 1.2
    else:
        premium = base
    logger.debug(f"Adjusted premium: {premium}")
    return premium
