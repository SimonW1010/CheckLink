# CheckLink
A Reddit bot that when mentioned checks parent comment's link for malicious content.

# Imports
```
import praw
import re
import vt
```

# Setup Virus Total
![download](https://user-images.githubusercontent.com/93505099/146694566-f11115e1-81f1-4f6f-a44f-c065b6640d0c.png)
>
Virus total is the website checklink uses to scan URL's an account must be made to use it's API
>Click [here](https://support.virustotal.com/hc/en-us/articles/115002100149-API) for instructions on how to get your VirusTotal API
>
Place API in line 5 of CheckLink script

# Reddit account setup

The first few minutes of this video will show you how to easily setup reddit and find your ID,secret and user agent.
https://www.youtube.com/watch?v=3FpqXyJsd1s
>
Fill in lines 8-12

# Limitations
>CheckLink cannot read more than 1 link per mention for best expirience at the moment (build 1.0)
>
>CheckLink cannot be used for link posts only links within the comment section
