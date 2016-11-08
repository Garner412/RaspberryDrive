import os
import sys
from time import sleep
sys.path.insert(0, os.getcwd())
print sys.path
# import models.analyze
from models.analyze import check_blob_in_direct_path
from get_images_from_pi import get_image, valid_image
from connect import new_connection, send_command, receive_confirmation

#start the camera taking pictures on contr pi
#start the server listening on camera pi
#start the server connection on this current server


s = new_connection()

#x times do:
  #retrieve image.  mage, check if its in path.
  #send instruction over server
count = 0
while (count < 100):
  get_image()
  if valid_image(os.getcwd() + "/images/gregTest.jpg"):
    instruction = check_blob_in_direct_path(os.getcwd() + "/images/gregTest.jpg")
    send_command(s, instruction, "0.5")
    receive_confirmation(s)
    count += 1

s.close()
