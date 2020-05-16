import time
from plyer import notification      
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "pls drink water now !!",
            message = "8 litter requied",
            app_icon ="C:\\Users\\shree\\Desktop\\drinkwater_app\\icon.ico",
            timeout= 10
        )
        time.sleep(6)
