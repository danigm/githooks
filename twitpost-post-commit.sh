#!/bin/bash

SERVER="http://twitter.com"
SERVICE="/statuses/update.json"
PREFIX="[myproject commit] "
POSTFIX=" -> http://git.myserver.com/myproject"

URL=$SERVER$SERVICE

USER=pepe
PASSWD=123

MSG=$PREFIX$(git log -n 1 --oneline)$POSTFIX
echo "---"
echo $MSG
echo "---"
echo "twit that? y/n"
read confirm
if [ $confirm = "y" ]
then
    curl -u $USER:$PASSWD -d status="$MSG" $URL > /dev/null 2> /dev/null
fi
