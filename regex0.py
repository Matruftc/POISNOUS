import re

txt="The rain in Odisha"
x=re.search("^The.*Odisha$",txt)       #x=re.search("elements",txt)

if x:
    print("Match")
else:
    print("NotMatch")