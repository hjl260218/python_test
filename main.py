import requests
import os

def start() :
  print("Welcome to main.py""\nPlease write a URL or URLs you went to check. (separated by comma)")
  url_list = input().split(",")
  check(url_list)

def check(url_list):
  for x in range(len(url_list)):
    url_list[x] = url_list[x].lower()
    url_list[x] = url_list[x].strip()
    if "." not in url_list[x] :
      print(url_list[x]+" is not a valid URL")
      break
    elif "http://" not in url_list[x] :
      url_list[x] = "http://"+ url_list[x]
    try :
      result = requests.get(url_list[x])
      if result.status_code == 200 :
        print(url_list[x]+" is up!")        
    except :
      print(url_list[x]+" is down!")
  exit()

def exit():
  re = input("Do you want to start over? y/n")
  if re == "y":
    os.system('clear')
    start()
  elif re == "n":
    print("ok. bye.")
  else:
    print("That's not a vaild answer")
    exit()

url_list=[]
start()
'''
def haha():
  start()
  check(url_list)
  exit()
'''

'''
for a in url_list (range i):
  a = a.strip(" ")
  print(a.lower())
  if "http" not in a:
    print(url_list)
  else:
    print("a")

>>> lists = [[] for i in range(3)]
>>> lists[0].append(3)
>>> lists[1].append(5)
>>> lists[2].append(7)
>>> lists
[[3], [5], [7]]
'''
   
  