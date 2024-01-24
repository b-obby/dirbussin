# dirbussin
a script to brute force a web application's directory

As a future penetration tester, it is very likely that I will encounter an instance where I must attempt to enumerate the directory for a web application. I have created a script that automates this process. This is a much simpler version than the popular DirBuster / GoBuster

The following must be imported for this script to be successful
* `requests` - enabling HTTP requests
* `BeautifulSoup` - html parsing libary: pulls XML / HTML data from webpages
* `threading` - enables multi-threading to help the script run faster
* `argparse` - enables user friendly interactions, enabling the user to include parameters when executing dirbussin.py
* `sys` - checks for command-line arguments
* `logging` - allows the user to export results as file

Executing the script
To strengthen the user-experience, users are able to include some command line arguments
* Number of Threads: `--threads <number of threads>`
* Quiet Mode - `--quiet`
* File Logging - `--log_file <file name>`

The following is an example of what a full command line argument looks like

`python dirbussin.py --threads 4 wordlists.txt --quiet --log_file dirbussin.log`

The script is also capable of handling both HTTP and HTTPS requests


>[!CAUTION]
>This program has been written only for educational purposes with the goal of strengthening my professional resume. This program should not be used on webpages without direct legal consent. I do not hold any legal responsability nor liablity for how others might use this tool. 
