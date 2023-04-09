import os
import threading

from pkg.HAL9000 import HAL9000

if __name__ == "__main__":
    friend = HAL9000()

    # Show image on different thread to prevent blocking
    download_thread = threading.Thread(target=os.system, args=('python show_hal.py',))
    download_thread.start()

    friend.start()    
