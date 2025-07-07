from utils.logger import logger

def calculate(behavior):
    logger.info("Calculating risk score...")
    risk = 0
    for issues in behavior:
        risk += len(issues)
    score = min(risk * 10, 100)
    logger.debug(f"Calculated risk score: {score}")
    return score
