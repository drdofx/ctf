- ssh bandit21@bandit.labs.overthewire.org -p2220
- cd /etc/cron.d
- cat cronjob_bandit22 -> **found that it's executing /usr/bin/cronjob.bandit22.sh**
- ls /usr/bin | grep cron
- cd /usr/bin
- cat cronjob_bandit22.sh
>#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
- cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
> Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

continue to [[level 22]]
