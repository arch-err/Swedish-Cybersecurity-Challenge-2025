# RizzClicker
*If only it were that simple...😔*

## Solution
1. A zip-archive of the servers code, and a link to a website...
2. Upon closer inspection of the code we realize that the field `kid` (key-id) in the JWT token that the site saves data in is important. We can change this key-id to point to a known file, (the key-id is used to point out a file used as the key when signing the JWT). This means that we can generate out own JWT with our own payload and use this to get the flag.
3. `./solve.py`, then set the cookie `token` to the output of the code (our generated JWT).


## Flag
**Flag:** `SNHT{ult1m4t3_r1zz_l0rd}`
