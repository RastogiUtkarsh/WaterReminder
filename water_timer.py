#Timer Program
import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Drink Water Boss",
            message="Paani peele aalsi aadmi",
            timeout=10
        )
        time.sleep(60*60)