#!/usr/bin/env python3

import sys
import socket
import time
import threading


def banner():
  font = """
  ooooooooo.     .oooooo.   ooooooooo.   ooooooooooooo                                             
  `888   `Y88.  d8P'  `Y8b  `888   `Y88. 8'   888   `8                                             
   888   .d88' 888      888  888   .d88'      888                                                  
   888ooo88P'  888      888  888ooo88P'       888                                                  
   888         888      888  888`88b.         888                                                  
   888         `88b    d88'  888  `88b.       888                                                  
  o888o         `Y8bood8P'  o888o  o888o     o888o                                                 
                                                                                                   
                                                                                                   
                                                                                                   
   .oooooo..o   .oooooo.         .o.       ooooo      ooo ooooo      ooo oooooooooooo ooooooooo.   
  d8P'    `Y8  d8P'  `Y8b       .888.      `888b.     `8' `888b.     `8' `888'     `8 `888   `Y88. 
  Y88bo.      888              .8"888.      8 `88b.    8   8 `88b.    8   888          888   .d88' 
   `"Y8888o.  888             .8' `888.     8   `88b.  8   8   `88b.  8   888oooo8     888ooo88P'  
       `"Y88b 888            .88ooo8888.    8     `88b.8   8     `88b.8   888    "     888`88b.    
  oo     .d8P `88b    ooo   .8'     `888.   8       `888   8       `888   888       o  888  `88b.  
  8""88888P'   `Y8bood8P'  o88o     o8888o o8o        `8  o8o        `8  o888ooooood8 o888o  o888o 
  """
  print(font)                                                                                               

                                                                                                 
                                                                                                 

if __name__ == '__main__':
  banner()

  print("-"*100)
  
  print("-"*100)
  print("Scanning the Target:",sys.argv[1])

  usage = "python3 <fileName> <target> <startPort> <endPort>" 


  startTime=time.time()

  if(len(sys.argv)!=4):
    print(usage)
    sys.exit()

  try:
    target = socket.gethostbyname(sys.argv[1])


  except scoket.gaierror:
    print("Name resoultion error")
    sys.exit()

  startPort = int(sys.argv[2])
  endPort = int(sys.argv[3])


  def scanPortThreading(port):
    # print(f"scannign port:{port}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2) # setting the time for the connection receive
    connection = s.connect_ex((target, port)) 
    '''return 0 if connection established otherwise any random nubmer generates'''

    if(not connection):
      print(f"{port} is OPEN.")
      s.close()

  for port in range(startPort, endPort+1):

    thread = threading.Thread(target = scanPortThreading, args = (port,))
    thread.start()

  endTime= time.time()
  print(f"Time elapsed: {endTime - startTime:.2f} sec")


