all = input()
 
import re
num = re.sub(r"\D", "", all)
alf = re.sub(r"[^a-zA-Z]", "", all)

 
if len(alf) != 2:
  print("No")
elif len(num) != 6:
  print("No")
elif all[0].isupper() == "False":
  print("No")
elif all[7].isupper() == "False":
  print("No")
elif int(num) > 999999:
  print("No")
elif int(num) < 100000:
  print("No")
else:
  print("Yes")