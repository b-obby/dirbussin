# import the following functionalities and libraries to successfully run this script
import requests
from bs4 import BeatifulSoup
import threading
import argparse
import sys
import logging

def scan_directory(directory, target_url, quiet_mode, log_file):
    """
    Function to scan a directory and print/log the results

    Parameters:
    - directory: The directory to scan
    - target_url: The target URL
    - quiet_mode: Surpress output
    - log_file: path to the log file
    """
    
    url = f"{target_url}/{directory}"

    try:
        #disable SSL verification for simplicity 
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            print(f"Found: {url}")
            if not quiet_mode:
                logging.info(f"Found: {url}")
            elif response.status_code == 404:
                if not quiet_mode:
                    print{f"Not Found: {url}"}
                    logging.info(f"Not FOund: {url}")
            else:
                if not quiet_mode: 
                        print(f"Error ({response.status_code}): {url}")
                        logging.warning(f"Error ({response.status_code}): {url}")
    except requests.RequestException as e:
        if not quiet_mode:
            print(f"Error {e}")
            logging.error(f"Error: {e}")

def main():
    """
    Function to handle command-line arguments and initiate directory scanning
    """

    #set up argument parser
    parser = argparse.ArgumentParser(description='Directory Buster Script for Educational Purposes')
    parser.add_argument('target_url', help='Target URL to Scan')
    parser.add_argument('wordlist_path', help='Path to wordlist file')
    parser.add_argument('--threads', type=int, default=1, help='Number of Threads (Default: 1)')
    parser.add_argument('--quiet', action='store_true', help='Quiet mode: Surpress Output')
    parser.add_argument('--log_file', default='dirbussin.log', help='Log file path')

    #parse command-line arguments
    args = parser.parse_args()

    #extract word-line arguments
    target_url = args.target_url
    wordlist_path = args.wordlist_path
    num_threads = args.threads
    quiet_mode = args.quiet
    log_file = args.log_file

    #configure logging to write to the specified log file
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    #read directories from the wordlist file
    with open(wordlist_path, 'r') as file:
        directories = [line.strip() for line in file.readLines()]

    #create thread for each directory
    threads = []
    for directory in directories:
        thread = threading.Thread(target=scan_directory, args=(directory, target_url, quiet_mode, log_file))
        threads.append(thread)
        thread.start()

    # wait for threads to finish
    for threads in threads:
        thread.join()

if __name__ == "__main__"
    main()