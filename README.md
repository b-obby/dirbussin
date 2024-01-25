# dirbussin
A script to brute force a web application's directory. A wordlist is not included (for now) but there are plenty of open source options available online.

This is a MUCH simpler version of dirbuster I have created to practice my proficiency in Python.

### The following functions and libraries must be imported for this script to work
* `requests` - enabling HTTP requests
* `BeautifulSoup` - html parsing libary: pulls XML / HTML data from webpages
* `threading` - enables multi-threading to help the script run faster
* `argparse` - enables user friendly interactions, enabling the user to include parameters or use -help for further information 
* `sys` - checks for command-line arguments
* `logging` - allows the user to export results as file

### Executing the script
To strengthen the user-experience, users are able to include some command line arguments
* Adjust Number of Threads: `--threads <number of threads>`
* Quiet Mode - `--quiet` Does not print results in the terminal / CLI. 
* File Logging - `--log_file <file name>`

> It is reccomended that Quiet mode is used in tandem with creating a log file, as you would not be able to see results otherwise.

The following is an example of what a full command line argument looks like

`python dirbussin.py --threads 4 wordlists.txt --quiet --log_file dirbussin.log`

The script is also capable of handling both HTTP and HTTPS requests


>[!CAUTION]
>This program has been written only for educational purposes with the goal of strengthening my professional resume. This program should not be used on webpages without direct legal consent. I do not hold any legal responsability nor liablity for how others might use this tool. 
