#!/usr/bin/env python3
import json
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By

class Dorkinho(argparse.Action):
   def __init__(self):
      self.driver = webdriver.Firefox()
      self.dorks_file = json.load(open("lists/dorks.json"))

   def list_dorks(self):
      names = list(self.dorks_file.keys())
      for name in names:
         print(name) 

   def exclusive_dork(self, name_dork, domain):
      counter = 0
      names = list(self.dorks_file.keys())
      while counter < len(names):
         if (name_dork == list(self.dorks_file.keys())[counter]):
            print(f"Openning Dork[{name_dork}] and Domain[{domain}]")
            f_url = str(self.dorks_file[names[counter]]).format(domain)
            self.driver.get(f_url)
         counter += 1

   def all_requests(self, domain):
      counter = 0
      names = (list(self.dorks_file.keys()))
      while counter < 3:
         f_url = str(self.dorks_file[names[counter]]).format(domain)
         self.driver.execute_script(f"window.open('{f_url}');")
         counter += 1

   def close_pages(self):
      counter = 0
      while counter < len(self.driver.window_handles) - 1:
         import time 
         self.driver.switch_to.window(self.driver.window_handles[counter])
         try:
            time.sleep(4)
            element = self.driver.find_element(By.ID, "result-stats")
            if " 0 " in element.text:
               self.driver.close()
               print("[!] Tab closed, invalid result")
         except:
            print("Not found!")
         counter += 1
