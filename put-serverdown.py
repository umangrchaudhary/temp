import time

def consume_ram():
    data = []
    try:
        while True:
            data.append(" " * 10**6)
            print(f"Current list size: {len(data)} MB")
            time.sleep(0.1)
    except MemoryError:
        print("Memory limit reached! RAM is full.")
    except KeyboardInterrupt:
        print("Stopped by user.")
        input("Press Enter to release memory and exit...")
    finally:
        data.clear()
        print("Memory released.")

if __name__ == "__main__":
    print("Starting RAM consumption. Press Ctrl+C to stop.")
    consume_ram()
