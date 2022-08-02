import logging

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from app.db.session import SessionLocal

# from fisherman.app.db.session import SessionLocal
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


@retry(
    stop=stop_after_attempt(5),  # 5s
    wait=wait_fixed(1),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    db = SessionLocal()
    db.execute("SELECT 1")


def main() -> None:
    logger.info("init service")
    init()
    logger.info("Load finished")


if __name__ == "__main__":
    main()
