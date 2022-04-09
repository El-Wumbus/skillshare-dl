#!/usr/bin/env python3
from downloader import Downloader
import cookie
import getopt
import sys

# Declare variables to prevent errors later
course_id = None
ID = None
URL = None
course_url = None


def yes_or_no(question):
    reply = str(input(question + ' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False


def usage():
    try:
        print("error: this command requires options [4].\n\
            Availible options:\n\
            [-i]: Download course by ID, e.g. 'skillshare-dl.py -i 189505397'\n\
            [-u]: Download course by URL, e.g. 'skillshare-dl -u https://www.skillshare.com/classes/Art-Fundementals-in-One-Hour/189505397'\n\
            ")
    except:
        return 1

argv = sys.argv[0:]  # parsing the argument list

try:
    opts, args = getopt.gnu_getopt(argv, "i:u:")
except:
    print("error: getopts error! [2]")
    exit(2)

for opt, arg in opts:

    if opt in ['-i']:
        ID = True
        if arg == '':
            print("error: this option requires an argument [3]")
            exit(3)
        course_id = arg

    elif opt in ['-u']:
        URL = True
        if arg == '':
            print("error: this option requires an argument [3]")
            exit(3)
        course_url = arg
    else:
        usage()
        exit(4)

if len(sys.argv) == 1:
    usage()
    exit(4)
# bool for downloading subtitle
subs = yes_or_no("Download Subtitles?")
if subs:
    boolSubtitle, all_subs = True, True
else:
    boolSubtitle, all_subs = False, False
dl = Downloader(cookie=cookie.cookie)
boolResources = yes_or_no("Download Resources?")

try:
    if ID:
        dl.download_course_by_class_id(
            course_id, boolSubtitle, all_subs, boolResources)
    elif URL:
        dl.download_course_by_url(
            course_url, boolSubtitle, all_subs, boolResources)
except:
    print("there was an error [1]")
    exit(1)
