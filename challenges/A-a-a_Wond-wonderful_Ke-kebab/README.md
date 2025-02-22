# A-a-a_Wond-wonderful_Ke-kebab
*I think my computer has started stuttering!*

## Solution
1. We get a file of binary data. Based on the first bytes it looks like it's supposed to be a `PNG` image, but it can't be viewed as one right now.
2. Upon closer inspection I realized that every few bytes are duplicated, so we'll just need to create a script that can remove these duplicated bytes.
3. `./solve.py`
4. The script gives us a new file as output, `solve.bin` that indeed is a `PNG` image, a picture of a kebab with the flag in the top left corner
5. ![solve.jpg](./solve.png)


## Flag
**Flag:** `SNHT{I_d1dnt_kn0w_c0mput3r5_stutt3r3d}`
