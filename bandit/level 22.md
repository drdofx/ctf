- ssh bandit22@bandit.labs.overthewire.org -p2220
- cd /etc/cron.d
- cat cronjob_bandit23 -> **found that it's executing /usr/bin/cronjob.bandit23.sh**
- cd /usr/bin/
- cat cronjob_bandit23.sh
>#!/bin/bash
myname=$(whoami) 
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1) 
echo "Copying passwordfile /etc/bandit_pass/`$myname` to /tmp/$mytarget" 
cat /etc/bandit_pass/`$myname` > /tmp/$mytarget
- mkdir /tmp/drdofx
- cp cronjob_bandit23.sh /tmp/drdofx/
- cd /tmp/drdofx
- nano cronjob_bandit23.sh -> **change myname=bandit23**
- ./cronjob_bandit23.sh
> Copying passwordfile /etc/bandit_pass/bandit23 to /tmp/8ca319486bfbbc3663ea0fbe81326349
- cat /tmp/8ca319486bfbbc3663ea0fbe81326349
> jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

continue to [[level 23]]
