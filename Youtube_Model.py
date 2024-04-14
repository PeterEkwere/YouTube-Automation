#!/usr/bin/python3
"""
    This Module Contains the entry point for the Youtube Bot
    Author: Peter Ekwere
"""
#import selenium
import time
#from selenium import webdriver
import concurrent.futures
import csv
from csv import reader
import json
from login_gmail_selenium.util.profiles.google_profile import GoogleProfile
from login_gmail_selenium.util.profiles.profile import Profile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import multiprocessing as mp
import time
import random
from threading import Thread
from itertools import cycle, repeat

# Add some random delays to mimic human behavior
def random_delay():
    time.sleep(random.uniform(1, 3))

#driver = None
            
                    
class Youtube:
    """ The Youtube class will handle every method regarding Youtube
    """
        
    
    def launch_profile(self, email, password, backup_email):
        if email != "" and password != "":
            profile = GoogleProfile(email, password, backup_email)
            driver = profile.retrieve_driver()
            profile.start()
        else:
            raise(f"Error: No Email or Password was Passed for {email} with password: {password}")
        return driver
    
    
    def like_comment(self, comment_url, email, password, backup_email):
        """ This is the method that will handle liking comments on youtube

        Args:
            comment_url (list): This is the links to the video where the comment exist
            email (str): This is a bot email
            password (str): This is a bot password
        """
        #global driver
        driver = self.launch_profile(email, password, backup_email)
        
        if comment_url:
            for url in comment_url:
                for attempt in range(2):  # Try up to 2 times before continuing
                    try:
                        #driver = self.launch_profile(email, password, backup_email)
                        print("Getting URL")
                        driver.get(url)
                        # Opening YouTube and navigating to video
                        print("About to Sleep For 20 Seconds")
                        time.sleep(15)
                        # Navigating to comments section
                        print("Finished Sleeping for 20 seconds for youtube page to load")
                        comments_section = WebDriverWait(driver, 15).until(
                            EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer"))
                                                            #"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments"))
                            )
                        # Scrolling down
                        print("Scrolling To comments Section")
                        #time.sleep(5)
                        driver.execute_script("arguments[0].scrollIntoView(true)", comments_section)                 
                        print("About to sleep for 3 Seconds")
                        time.sleep(3)
                        print("Finished sleeping for 3 Seconds Now Extracting First Comment")
                        
                        # Find the first comment
                        first_comment = comments_section.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[1]/ytd-comment-view-model/div[3]")

                        print("Extracting First like Button")
                        # Getting like button for comment
                        like_button = first_comment.find_element(By.ID, "like-button")
                        print("About to click like button")     
                        like_button.click()
                        print("Finished Clicking like Button")
                        
                        #time.sleep(5)  # Adjust timeout as needed
                        try:
                            popup = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-creation-dialog-renderer/div")) 
                                                            #"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer"))
                                                            #"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments"))
                            )
                            create_youtube_account_button = popup.find_element(By.ID,"create-channel-button")
                        except Exception as e:
                            popup = None
                            pass
                        if popup:
                            print(f"POPUP EXIST")
                            if create_youtube_account_button:
                                print(f"popup button found")
                                time.sleep(5)
                                # Click the "create-channel-button" within the popup
                                create_youtube_account_button.click()
                                print("POPUP Button Clicked about to sleep for 5 seconds")
                                time.sleep(3)
                                print("Finished sleeping Now About to refresh page ")
                                driver.refresh()
                                print("Finished refreshing now sleeping for 5 seconds ")
                                time.sleep(6)
                                print("Finished sleeping Now About to scroll to comment again")
                                driver.execute_script("arguments[0].scrollIntoView(true)", first_comment)
                                time.sleep(3)
                                print("Finished sleeping for 2 sec Now About to click like button again ")
                                like_button.click()
                                print("Finished Clicking like Button")
                        break  # Exit the loop if successful
                    except Exception as e:
                        print(f"Attempt {attempt+1} for url: {url}: Exception occurred -  with email {email}")
                        pass  # Retry on the next attempt
                else:  # If all attempts fail, silently continue
                    print(f"Failed to access url with email: {email} after 2 attempts.")



            # Close the browser
            #print("Sleeping For 5 Seconds")
            #time.sleep(5)
            print("Now Quiting after Finished Task")

            try:
                driver.close()
            except Exception as e:
                print(f"Error closing window: {e}")
            time.sleep(2)
            driver.quit()
        else:
            raise(f"Error: No Incorrect URL WAS PASSED: {comment_url}")
        
        
    
    def extract_urls(self, url_file):
        """
        Extracts a list of URLs from the specified file.

        Args:
            url_file (str): Path to the file containing URLs.

        Returns:
            list: A list of URLs extracted from the file.
        """
        with open('urls.json', 'r') as infile:
            urls = json.load(infile)
        
        urls_list = []
        for url in urls:
            try:
                url_parts = url.split("?")
                if len(url_parts) > 1:
                    link = url_parts[1]
                else:
                    raise (f"Error: Splitting url is {url} This Url Might Not be a valid Youtube Comment Link") 
                if link:
                    comment_link = f"https://www.youtube.com/watch?app=desktop&{link}"
                    urls_list.append(comment_link)
                else:
                    raise "Error with youtube link"
            except Exception as e:
                print(f"Error Extracting URL {e}")
        return urls_list
            

    def extract_accounts(self, account_file):
        """
        Extracts a list of email, password, and backup email tuples from the specified file.

        Args:
            account_file (str): Path to the file containing account information.

        Returns:
            list: A list of tuples containing (email, password, backup_email).
        """
        with open('accounts.json', 'r') as f:
            retrieved_email_data = json.load(f)
        return retrieved_email_data


    def process_account(self, account, urls):
        email = account.get("email", None)
        password = account.get("password", None)
        backup_email = account.get("backup_email", None)
        
        if email and password:
            try:
                print("Please Hold")
                self.like_comment(urls, email, password, backup_email)
            except Exception as e:
                print(e)



if __name__=="__main__":
    print("DO NOT RUN THIS DIRECTLY")
    pass
    