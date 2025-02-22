# ClickMe
*Simply click me.*

## Solution
1. We're given a `.jar` (java archive), but after unpacking it we see a bunch of python (turns out this was some kind of *jython* nonsense).
2. In `clickme/__run__.py` we can find the code that should eventually give us a flag. We inspect this and eventually figure out a way to script and bruteforce the key, to get the flag
3. `./solve.py`


## Flag
**Flag:** `SNHT{jython_4r_13x1k0gr4f15k7_s70rr3_4n_python}`
