Your script looks clean and should work correctly. Just ensure that `watchdog` and `colorama` are installed with:

```bash
pip install watchdog colorama
```

Now, here's your *README.md* file for *NoorWatch* , incorporating your GitHub username *@Noureddindev* and developer name *ASKAL NOUREDDIN* :

```markdown
# NoorWatch

## 📂 Folder Activity Monitor  
**NoorWatch** is a real-time file activity monitoring tool developed by **ASKAL NOUREDDIN**. It allows users to track changes in a specified folder, logging modifications, creations, deletions, and movements.

---

## 🚀 Features  
✔ **Real-time monitoring** of file changes.  
✔ **Logs all events** to `log.txt`.  
✔ **Color-coded terminal alerts** using `colorama`.  
✔ **Supports Linux, Windows, and Termux** environments.  

---

## 🛠️ Installation  

### **Linux & Windows**  
```bash
git clone https://github.com/Noureddindev/NoorWatch.git
cd NoorWatch
pip install -r requirements.txt
python3 NoorWatch.py
```

*Termux  *
```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/Noureddindev/NoorWatch.git
cd NoorWatch
pip install -r requirements.txt
python NoorWatch.py
```

---

*⚡ Usage  *

To start monitoring a folder:  
```bash
python NoorWatch.py
```
📂 Enter the *full path* of the folder to monitor when prompted.  
📜 All changes will be displayed in the terminal and logged into *log.txt* .

---

*📝 Example Output  *
```bash
[Created] /home/user/Projects/new_script.py
[Modified] /home/user/Docs/README.md
[Deleted] /home/user/Temp/test.log
[Moved] from /home/user/Old/file.txt to /home/user/New/file.txt
```

---

*🤝 Contributions  *

Contributions are welcome! Feel free to submit *Pull Requests* or report issues.  
*GitHub:* [@Noureddindev](https://github.com/Noureddindev)  

---

*📜 License  *
This project is *open-source* and available under the *MIT License* .

---

Let me know if you'd like modifications or additional sections! 🚀✨  
```

Your project is now well-documented and ready for GitHub. Let me know if you need further refinements!
