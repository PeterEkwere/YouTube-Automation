#!/usr/bin/python3
"""
    This Module is the entry point for the application
    Author: Peter Ekwere
"""
from Youtube_Model import Youtube
import time
import concurrent.futures


def like_comments():
    try:
        yt = Youtube()
        print("Starting BOT")
        # Extracting the accounts and urls from the json files
        accounts = yt.extract_accounts("accounts.json")
        print("Extracting Accounts")
        urls = yt.extract_urls("urls.json")
        print("Extracting URLS")
        
        if not urls:
            print("Error: No URLs found in 'url.json'.")
        if not accounts:
            print("Error: No accounts found in 'accounts.json'.")
            
            
        for account in accounts:
            print(f"passing {account} and urls to bot")
            start_time = time.time()
            yt.process_account(account, urls)            
            end_time = time.time()  #Record end time after the simulated like operation
            elapsed_time = end_time - start_time
            print(f"Start Time: {time.strftime('%H:%M:%S', time.localtime(start_time))}")
            print(f"End Time:   {time.strftime('%H:%M:%S', time.localtime(end_time))}")
            print(f"Elapsed Time: {elapsed_time:.2f} seconds")
        return "Done"
    except Exception as e:
        print(f"Error in like Comments function are {e}")
        return "False"
    
    
def like_comments_faster():
    try:
        yt = Youtube()
        print("Starting BOT")
        # Extracting the accounts and urls from the json files
        accounts = yt.extract_accounts("accounts.json")
        print("Extracting Accounts")
        urls = yt.extract_urls("urls.json")
        print("Extracting URLS")
        
        if not urls:
            print("Error: No URLs found in 'url.json'.")
        if not accounts:
            print("Error: No accounts found in 'accounts.json'.")
                
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            # Submit each account processing to the executor
            futures = [executor.submit(yt.process_account, account, urls) for account in accounts]
            
            # Wait for all futures (threads) to complete
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()  # Get the result or exception of each thread
                except Exception as e:
                    print(f"An error occurred: {e}")
                    return "False"
        return "Done"
    except Exception as e:
        print(f"Error occured in fast like function :{e}")
        return "False"
        
        







if __name__=="__main__":
    like_comments()