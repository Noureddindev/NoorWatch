```markdown
NoorWatch.py

Hello World, I'm ASKAL 👋

Welcome to the official repository for *NoorWatch.py*, a lightweight real-time *folder and file activity monitoring* tool. This script allows you to track any changes in a target directory — such as file creation, deletion, modification, and movement — with live logs and clear colored output.

#🚨 *DISCLAIMER:* I take *NO responsibility* for any *illegal or unethical* use of this script. It is meant for *educational and authorized purposes ONLY*.

---

📌 Features
- Monitor folders for real-time activity.
- Detect file creation, deletion, modification, and moving.
- Logs events into `log.txt`.
- Colored console output for easy tracking.
- Works perfectly on *Linux*, *Windows*, and *Termux*.

---

🛠 Installation

*On Linux / Windows*
Run the following commands:
```bash
git clone https://github.com/Noureddindev/NoorWatch.git
cd NoorWatch
pip install -r requirements.txt
python3 noorwatch.py
```

*On Termux*
Install Python and Git:
```bash
pkg update && pkg upgrade
pkg install python git
```

Then clone and run:
```bash
git clone https://github.com/Noureddindev/NoorWatch.git
cd NoorWatch
pip install -r requirements.txt
python noorwatch.py
```

---

⚡ Usage
To run the script:
```bash
python noorwatch.py
```

When prompted, enter the full path of the folder you want to monitor.  
All changes will be displayed in the terminal and logged in `log.txt`.

---

🧠 Example Use Case
```bash
[Created] /home/user/Projects/new_code.py
[Modified] /home/user/Projects/README.md
[Deleted] /home/user/Projects/test.log
[Moved] from /home/user/old_folder/file.txt to /home/user/new_folder/file.txt
```

---

📢 Contributions
Feel free to fork, improve, and submit a *Pull Request*.  
Found a bug? Open an issue and help make *NoorWatch* even better!

*Maintainer:* [ASKAL NOUREDDIN](https://github.com/Noureddindev)
