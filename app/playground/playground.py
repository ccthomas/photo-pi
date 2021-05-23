path_a = "\\a\\b\c.png"
path_b = "a/b/c.png"

import re
a = re.findall("(\S)+(\.png)", path_a)
print(a[0][0])

b = re.findall("(\S)+(\.png)", path_b)
print(b[0][0])