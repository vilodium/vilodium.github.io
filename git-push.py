#!/bin/python3
# Python script to git pull/push for me
# i use it for almost every repostery i have
# i wrote it :P

# import libs

import os

# commands

os.system('git pull')

os.system('git add .')

commit = input('commit name [Home-Page] : ') # if i didn't enter any thing (pressed enter) set it to Home-page (when I'm lazy :P)

if commit == '':
	commit = 'Home-Page'

# the commit itself ^^

os.system('git commit -m \"' + commit + '\"')

os.system('git push')

print("\nDone MASTER Successfully (I Think :|)\n") # of course the script greets me

# ---------------
