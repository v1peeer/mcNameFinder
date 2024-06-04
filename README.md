# mcNameFinder
mcNameFinder is a python script you can use to find short usernames (e.g. 4-letter names)

# tutorial
1. clone/download & extract this repo
2. install python3 (and the "socks" package using pip if you want to use a socks proxy)
3. run ```python3 .\stringgen.py``` and generate strings/names
4. finally run ```python3 .\namefinder.py``` and wait
5. in the ```.\output\``` folder you will find three .txt files
   - ```available.txt``` (usernames which aren't taken, you can use these)
   - ```unavailable.txt``` (usernames which are taken, you can't use these)
   - ```ratelimited.txt``` (usernames which couldn't get checked because you were being rate-limited)
