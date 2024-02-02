import re

txt="The rain in Odisha"
x = re.search("\o",txt)
print("the dirst white space character is located in position: ",x.start())