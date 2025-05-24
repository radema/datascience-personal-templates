from .logging_utils import setup_logger

log = setup_logger()

def main():
    log.info("🚀 Starting main process...")
    try:
        # Your code logic here
        print("Hello World!")
        log.info("✅ Main process completed.")
    except Exception as e:
        log.exception("❌ An error occurred")

if __name__ == "__main__":
    main()
