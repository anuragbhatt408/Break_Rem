
#  (Schedule/Run your code in background) with Windows Task Scheduler

import time
import webbrowser
from plyer import notification


while True:
    #  sleep code for 60*60 second that is for 1 Hour
    time.sleep(60*60)
    
    #  It gives the notification on windows
    notification.notify(title = "Please Take Break",
            message="Our brains have two functioning modes: focused, and ‘diffused’. When operating in diffused mode, our brain is more relaxed and in a ‘daydream’ type state.",
            timeout = "5")
    
    # It will open Youtube in your default browser, you can choose different links
    webbrowser.open_new_tab("http://youtube.com")