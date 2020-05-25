import time
from plyer import notification
if __name__=='__main__':
    while True:
        notification .notify(
        title='Please drink water',
        message='Water is the most abundant molecule in the human body that undergoes continuous recycling. Numerous functions have been recognized for body water, including its function as a solvent',
        timeout=15
        )
        time.sleep(60*1)
       
