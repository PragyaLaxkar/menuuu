#!/usr/bin/python3
print("Content-type: text/html")
print("\n")

import subprocess
output = subprocess.getoutput("cal")
print("<pre>")
print(output)
print("</pre>")