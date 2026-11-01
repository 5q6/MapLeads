import logging
from database import init_db
from gui import start_gui

# Configure logging for the whole application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

if __name__ == "__main__":
    init_db()        # Ensure DB & tables exist before anything else
    start_gui()
