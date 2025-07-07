from utils.logger import logger

def detect(data):
    logger.info("Analyzing driving behavior...")
    behavior = []
    for record in data:
        issues = []
        if record['speed'] > 80:
            issues.append("speeding")
        if record['braking']:
            issues.append("harsh_braking")
        behavior.append(issues)
    logger.debug(f"Behavior flags: {behavior}")
    return behavior
