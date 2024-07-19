# This Repo Contains the source code For a Bot That logs in to youtube and likes a comment using profiles

1- unzip folder and open in a work space on your IDE

2 - cd Youtube_comment_liker on your gitbash terminal (important)

3 - open chrome and download python with version 3.9 on your system

4 - once installation complete, type python --version if its python 3.9 skip to task 7 else follow through

5 - On terminal type which python
    you should see a path like this 👉 /c/Users/mofe/AppData/Local/Programs/Python/(YOURCURRENT PYTHON VERISON HERE)/python
    copy the path exempting the last two folders like this 👉 /c/Users/mofe/AppData/Local/Programs/Python
    open your file manager and paste it on the path search and invert the slashes like this 👉C:\Users\mofe\AppData\Local\Programs\Python once you click you should see multiple python version folders
    if you see python 39 then it was installed and it's in the path
    then paste this path on your terminal
    C:\Users\(PC OWNERS NAME HERE)\AppData\Local\Programs\Python\Python39\python --version
    if you see python 3.9 move to task 6 else chat me

6 - create a virtual environment
    type -> C:\Users\(PC OWNERS NAME HERE)\AppData\Local\Programs\Python\Python39\python -m venv liker_venv

7 - Enter virtual environment 
    type -> source liker_venv/Scripts/activate or source liker_venv/bin/activate

8 - install dependencies
    pip install -r requirements.txt

9 - Update the undetected Chrome package
    type -> mv patcher_01.py patcher.py
    type -> mv patcher.py liker_venv/Lib/site-packages/undetected_chromedriver/ (if this doesnt work try swithing the slashes to "\")

10 - add newly created gmail accounts to the accounts.json file (i just kept that account there so you understand how to add new accounts, Dont run the script with the account there so it doesnt get flagged for multiple IPs)

11 - add your comments link to the urls.json file (Note if you run using the same urls it will unlike already liked comments)

12 - There are two ways to run the script
    1 - type -> python run.py (This is running the script directly)
    2 - type -> python -m application (This way will render a flask server Like the one you currently tested
                                        open chrome and go to the address(http://127...))


THINGS TO NOTE

1 - When creating an email address make sure to add backup email as a mode of verification not Numbers

2 - if you want to see the way the script functions 
    with chrome working in the background go to this path 
    👉 liker_venv_2\Lib\site-packages\login_gmail_selenium\util\base_profile.py
    go to line 81 and remove # in   #options.add_argument("--headless=new")

