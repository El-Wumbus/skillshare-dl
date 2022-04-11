#!/usr/bin/env bash

get_cookie() {
  printf "Get cookies from https://skillshare.com.\n\
  for help with this see the git repo.\n"

  read -rp "Paste your cookie here: " cookie_raw
  
  if [ "$cookie_raw" == "" ]; then
    clear
    echo "error: input string is empty"
    exit 1
  fi

  cookie="cookie = \"${cookie_raw}\"" # format the string in the correct way for python.
}

clear

get_cookie
eho "Working..."
echo "$cookie" >./cookie.py

clear
echo "done"
exit 0
