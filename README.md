# mcNameFinder
mcNameFinder is a python script you can use to find short usernames (e.g. 4-letter names)

# tutorial
1. clone/download & extract this repo
2. install python3 (and the "socks" package using pip if you want to use a socks proxy)
3. run ```python3 .\stringgen.py``` and generate strings (e.g. 1000 strings with 4 characters each)
4. edit all the proxy variables in ```.\namefinder.py``` if you want to use a proxy
5. finally run ```python3 .\namefinder.py``` and wait
6. in the ```.\output\``` folder you will find three .txt files
   - ```available.txt``` (usernames which aren't taken, you can use these)
   - ```unavailable.txt``` (usernames which are taken, you can't use these)
   - ```ratelimited.txt``` (usernames which couldn't be checked because you were being rate-limited)
