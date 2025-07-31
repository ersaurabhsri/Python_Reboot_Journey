import subprocess
from datetime import datetime
import os

# Get latest commit info
commit_msg = subprocess.getoutput("git log -1 --pretty=format:%s")
commit_hash = subprocess.getoutput("git log -1 --pretty=format:%H")
author = subprocess.getoutput("git log -1 --pretty=format:%an")
date = datetime.today().strftime('%Y-%m-%d')

log_path = "process-md.log"

# Ensure the log file exists
if not os.path.exists(log_path):
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("# Python Reboot Journey Log\n_Auto-generated process record based on Git commits_\n\n")

# Read current contents
with open(log_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Check if today's date header exists
header = f"## 📅 {date}\n"
if header not in lines:
    lines.append(f"\n{header}\n")

# Append commit log under date
entry = f"- **{commit_msg}** by {author} — `{commit_hash}`\n"
lines.append(entry)

# Write back updated log
with open(log_path, "w", encoding="utf-8") as f:
    f.writelines(lines)
