
# Minimal dead link checker
This is a very simple dead link checker for any local resource that contains links. It was made to automate dead link checking for https://github.com/mimblewimble/docs, but could be applied to any locally stored copy of a website. The script contains a list where you can specify which errors to report/print and which not

## Step 1 search the cloned document directory for all links (exclude output file)
`grep -roE --exclude=all_links.txt "(http|https)://[a-zA-Z0-9./?=_%:-]*"  > all_links.txt`

## Step 2, use Python to parse these links and print list of broken links to "broken_links.txt"
`python3 check_for_broken_links.py |sort| uniq > broken_links.txt`

## Step3, check most important, server not found (404) and server can't be reached/dead link (666)
`cat broken_links.txt | grep "404|666"> 404_666_links.txt`
  
## How to merge changes to main GitHub branch
First online update my own fork, https://github.com/Anynomouss/grindocs
Make a clone, or if you cloned form mimblewimble/doc master, add it as a external ref (only ones needed:
`git remote add myfork https://github.com/Anynomouss/grindocs.git`
git pull 
git push myfork master

Go to https://github.com/Anynomouss/grindocs and click make pull request