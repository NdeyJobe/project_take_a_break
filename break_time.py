import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started on " , time.ctime())
while (break_count < total_breaks):
#to make my program wait
  time.sleep(7200)
  #to open a web browser
  webbrowser.open("https://www.youtube.com/watch?v=EM7Cp7qZiR4")
  time.sleep(7200)
  break_count =+ 1
