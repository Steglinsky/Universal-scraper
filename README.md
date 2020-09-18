### Objective of the programme
The program is used to extract **all e-mail addresses** found in the given list of websites. The program is designed for quick scalability, the launch of the next instance on a virtual machine is only 3 minutes.

### Requirements:
- re
- http
- urllib
- socket
- request
- BeautifulSoup


### Quick start

##### 1. Prepare a list of pages to be scraped.
The list for scrapping should consist of web addresses written one under another in the form of a list in a .csv file.
The file should be called input.csv

The file should look like this:

| input.csv  |
| ------------ |
| http://www.lovecats.com  |
| http://www.thic-cats.com  |
|  http://www.bald-cats.com |
| etc |

Please note that the web **address must have the http:// character string in its structure**. It is very important for the programme to work.
The website www.cats.com will not be searched.
The website http://www.cats.com will be searched

In future, I will improve the address reading format and both formats will work.

#####  2. Preparing the environment.

The program works well on Windows (10 - preferred) and Linux VPN (tested on Debian).

###### 2.1 Windows
Create a new folder, place the uniscrap.py file in it and the prepared input.csv file

###### 2.2 Linux VPS
Using any FTP client (for example, WinSCP), you must log on to the machine.
Then create a directory (any name) in any location (preferably in your home folder).

Next, the prepared input file and scraper script should be placed in the created folder.

#####  3. Launching the script
###### 3.1 Windows
Just run the uniscrap.py script
Ready, the program runs and writes e-mail addresses to output.csv file

After starting the program will print out in the console the currently processed pages and possible messages about lack of access to the site (this happens when there is no content or server error is returned).
###### 3.2 Linux VPS
Using any SSH (PuTTY/Solar-PuTTY &hearts;) client, log in to the machine and go to the created catalogue.

Start the script using the command:
`python3 uniscrap.py`

Ready, the program runs and writes e-mail addresses to output.csv file

After starting the program will print out in the console the currently processed pages and possible messages about lack of access to the site (this happens when there is no content or server error is returned).

##### 4. Debugging
If the program encounters an unsupported exception to access a particular page, the action will be terminated. An error message will appear in the console. Then you should:
1. Add the exception to the code

2. For a quick resume, you need to find the last entered domain in the output.csv file. Then find it in the input and delete all records until it occurs.

##### 5. TODO LIST
- Output filtering from links 
- Filtering output from duplicates
- Input reading improvement (http://)
