import os
import logging
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pythonProject1Modeldz.settings')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    application = get_asgi_application()
    logger.info("ASGI application setup was successful.")
except Exception as e:
    logger.error("Failed to setup ASGI application.", exc_info=True)
    raise

