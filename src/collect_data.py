from utils.logger import logger

def simulate():
    logger.info("Simulating telematics data collection...")
    data = [
        {'speed': 70, 'braking': False},
        {'speed': 90, 'braking': True},
        {'speed': 60, 'braking': False},
    ]
    logger.debug(f"Collected data: {data}")
    return data
