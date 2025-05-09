#Take all the Osint data and combine them into one list

#def compiner(osint_data):
    #Implement the code here
  #  pass

import sys, os

# أضف المسار الكامل إلى المجلد اللي فيه مجلد playwright (يعني osint نفسه)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../osint')))

from playwright.sync_api import sync_playwright
