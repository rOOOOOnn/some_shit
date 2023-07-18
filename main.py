import os
import re

for filename in os.listdir("test"):
    file_path = os.path.join("test", filename)
    with open(file_path, "r") as f1:
        string = f1.read()
        new_string = re.sub(r"f\*ck|fuck", "F^_^k", string, flags=re.I)
        with open(os.path.join("test", "new_"+filename), "w") as f2:
            f2.write(new_string)