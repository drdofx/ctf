- ssh bandit12@bandit.labs.overthewire.org -p2220
- mkdir /tmp/rofx
- cd /tmp/rofx
- cp /home/bandit12/data.txt .
- xxd -r data.txt > data.gz (**for reversing hex dump**)
- gzip -d data.gz (**decompress gzip**)
- bzip2 -d data (**decompress bzip2**)
- mv data.out data.gz (**rename output file to gzip file**)
- gzip -d data.gz (**decompress gzip again**)
- tar -xvf data (**extract tar**)
- tar -xvf data5.bin
- tar -xvf data6.bin
- mv data8.bin data8.gz
- gzip -d data8.gz (**rename and decompress gzip**)
- cat data8
> 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

continue to [[level 13]]
