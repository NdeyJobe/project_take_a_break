import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())
while (break_count < total_breaks):
#to make the program wait
  time.sleep(7200) 
  #to open the web browser
  webbrowser.open("https://www.youtube.com/watch?v=izGwDsrQ1eQ")
  break_count =+ 1
