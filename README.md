Here is your *README.md* for the `NoorWatch.py` tool, written in *professional English*, with clear structure and bold formatting suitable for GitHub display:

---

```markdown
NoorWatch.py

👋 Hello World, I'm *ASKAL NOUREDDIN*

Welcome to the official repository of *NoorWatch.py*, a lightweight and efficient file monitoring tool for real-time directory activity tracking. This script helps you monitor any folder for changes such as file creation, deletion, modification, or movement — with live logging and colorful terminal output.

> 🚨 *DISCLAIMER:* I take *NO responsibility* for any *illegal or unethical* usage of this tool. It is intended for *educational and authorized purposes ONLY*.

---

📌 *Features*

- Real-time *directory monitoring*.
- Detects file *creation, deletion, modification, and movement*.
- Logs all events to a `log.txt` file.
- Colorful and informative terminal output.
- Compatible with *Linux*, *Windows*, and *Termux*.

---

🛠 *Installation*

On *Linux / Windows*

```bash
git clone https://github.com/Noureddindev/NoorWatch.git
cd NoorWatch
pip install -r requirements.txt
python3 noorwatch.py
```

On *Termux*

```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/Noureddindev/NoorWatch.git
cd NoorWatch
pip install -r requirements.txt
python noorwatch.py
```

---

⚡ *Usage*

To run the script:

```bash
python noorwatch.py
```

When prompted, enter the *full path* of the folder you want to monitor.  
All changes will be displayed in the terminal and logged to `log.txt`.

---

🧠 *Example Output*

```bash
[Created] /home/user/Projects/new_script.py
[Modified] /home/user/Docs/README.md
[Deleted] /home/user/Temp/test.log
[Moved] from /home/user/Old/file.txt to /home/user/New/file.txt
```

---

📢 *Contributions*

Feel free to contribute with *Pull Requests* or report bugs and improvements.  
Together, we can make *NoorWatch* even better!

*Developer:* [ASKAL NOUREDDIN](https://github.com/Noureddindev)

---

📄 *License*

This project is open source and licensed under the *MIT License*.
```
