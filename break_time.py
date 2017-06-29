import webbrowser
import time
t=1
print('this started at'+time.ctime())
#breaks after 2hours 
while(t<5):
  time.sleep(7200)
  t=t+1
  webbrowser.open("https://www.youtube.com/")
