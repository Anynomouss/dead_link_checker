import re
import urllib
import requests


## Open input file, create pattern to find URLs
file= open("all_links.txt",mode='r')
p = re.compile('https?://(?:www\\.)?[a-zA-Z0-9./_=+-]+') ## compiles re pattern for url's 
allowed_errors = [200,202,301,302,303]

## For each line, extract URL
for line in file:
    line = line.strip()
    if line == "":
        continue
    if ".git" in line:
        continue
    m = p.search(line)
    #print(line)
    # print(url)
    ## If URL in line, get response from header of the url
    if m != None:
        url = m.group()
        url = url.strip()
        ## Catch all errors
        try:    
            response = requests.head(url)
            if response.status_code in allowed_errors:
                pass
            else:
                print("{} | {} |{}".format(line,url,response.status_code))
        except requests.exceptions.ConnectionError:
            print("{} | {} | {}".format(line,url,666)) ## 666 is used for dead link      