from loguru import logger

from router_ip_watcher.utils import common

# logger.debug("That's it, beautiful and simple logging!")
log_path = common.get_recommended_log_path()
LOG = logger
LOG.add(log_path, rotation="10 MB", retention="7 day", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")

LOG.info('load logger')
