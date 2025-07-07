from utils.logger import logger

def generate(behavior):
    logger.info("Generating driving feedback...")
    tips = set()
    for issues in behavior:
        if "speeding" in issues:
            tips.add("Avoid overspeeding")
        if "harsh_braking" in issues:
            tips.add("Brake smoothly")
    logger.debug(f"Generated tips: {tips}")
    return list(tips)
