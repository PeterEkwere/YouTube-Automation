#!/usr/bin/python3
"""
    This Module Contains the entry point for the Youtube Bot
    Author: Peter Ekwere
"""
#import selenium
import time
#from selenium import webdriver
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
import time
import random

# Add some random delays to mimic human behavior
def random_delay():
    time.sleep(random.uniform(1, 3))


            
                    
class Youtube:
    """ The Youtube class will handle every method regarding Youtube
    """
    
    def like_comment(self, video_url, email, password, backup_email):
        """ This is the method that will handle liking comments on youtube

        Args:
            video_url (str): This is a link to the video where the comment exist
            username (str): This is the username of the person that made the comment
            email (str): This is a bot email
            password (str): This is a bot password
        """
        #global driver
        start_time = time.time()
        profile = GoogleProfile(email, password, backup_email)
        driver = profile.retrieve_driver()
        profile.start()
        
        if video_url != "":
                if email != "" and password != "":
                    print("Getting URL")
                    driver.get(video_url)
                    # Opening YouTube and navigating to video
                    print("About to Sleep For 30 Seconds")
                    time.sleep(20)
                    # Navigating to comments section
                    print("Finished Sleeping for 30 seconds for youtube page to load")
                    comments_section = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer"))
                                                        #"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments"))
                        )
                    # Scrolling down
                    print("Scrolling To comments Section")
                    driver.execute_script("arguments[0].scrollIntoView(true)", comments_section)                 
                    print("About to sleep for 20 Seconds")
                    time.sleep(10)
                    print("Finished sleeping for 20 Seconds Now Extracting First Comment")
                    
                    # Find the first comment
                    first_comment = comments_section.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[1]/ytd-comment-view-model/div[3]")

                    print("Extracting First like Button")
                    # Getting like button for comment
                    like_button = first_comment.find_element(By.ID, "like-button")
                    print("About to click like button")     
                    like_button.click()
                    
                    time.sleep(3)  # Adjust timeout as needed
                    try:
                        popup = WebDriverWait(driver, 5).until(
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
                            # Click the "create-channel-button" within the popup
                            create_youtube_account_button.click()
                            print("POPUP Button Clicked about to sleep for 10 seconds")
                            time.sleep(10)
                            print("Finished sleeping Now About to refresh page ")
                            driver.refresh()
                            print("Finished refreshing now sleeping for 15 seconds ")
                            time.sleep(15)
                            print("Finished sleeping Now About to scroll to comment again")
                            driver.execute_script("arguments[0].scrollIntoView(true)", first_comment)
                            time.sleep(2)
                            print("Finished sleeping for 2 sec Now About to click like button again ")
                            like_button.click()
                            print("Finished Clicking like Button")



                    # Close the browser
                    print("Sleeping For 15 Seconds")
                    time.sleep(5)
                    print("Now Quiting after Finished Task")
                    
                    
                    end_time = time.time()  # Record end time after the simulated like operation
                    elapsed_time = end_time - start_time
                    print(f"Start Time: {time.strftime('%H:%M:%S', time.localtime(start_time))}")
                    print(f"End Time:   {time.strftime('%H:%M:%S', time.localtime(end_time))}")
                    print(f"Elapsed Time: {elapsed_time:.2f} seconds")

                    driver.close()
                    time.sleep(1)
                    driver.quit()
                else:
                    raise(f"Error: No Email or Password was Passed for {email} with password: {password}")
        else:
            raise(f"Error: No Video URL WAS PASSED: {video_url}")



if __name__=="__main__":
    #backup_email = "j8166462@gmail.com"
    #new_email = "jokejohnson4@gmail.com"
    #new_password = "JokesonJohnson"
    #password = "Joe2036$"
    #video_url = "https://www.youtube.com/watch?v=1GOzHcR7gHM&lc=UgyyygNf1OawWyAAozJ4AaABAg"
    #url_parts = video_url.split("?")
    #if len(url_parts) > 1:
    #    link = url_parts[1]
    #else:
    #    print(f"Error: Splitting url parts is {url_parts}")
    #if link:
    #    comment_link = f"https://www.youtube.com/watch?app=desktop&{link}"
    #else:
    #    raise "Error with youtube link"
    #yt = Youtube()
    #yt.like_comment(comment_link, "ghosttt871@gmail.com", "ghostduke", "")
    pass