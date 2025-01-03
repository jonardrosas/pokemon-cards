import logging
import datetime

today = datetime.datetime.today()
format_date = today.strftime("%y-%m-%d")
logging.basicConfig(
    filename=f"log_main_{format_date}.log",
    filemode="a",
    level=logging.DEBUG,
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

logger = logging.getLogger(__name__)
