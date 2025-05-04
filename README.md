```markdown
# NoorWatch.py

## 👋 Welcome  
Hello! I'm **ASKAL NOUREDDIN**, the developer behind **NoorWatch.py**—a lightweight and efficient file monitoring tool designed for real-time directory activity tracking.  

This script enables you to track changes in any folder, detecting file **creation, deletion, modification, and movement**, while providing instant logging and colorful terminal output.  

> 🚨 **DISCLAIMER:** This tool is strictly intended for **educational and authorized purposes**. I am **not responsible** for any **illegal or unethical** usage.

---

## 📌 Features  
✔ **Real-time Directory Monitoring** – Automatically detects file activities.  
✔ **Event Tracking** – Monitors file **creation, deletion, modification, and movement**.  
✔ **Log System** – Saves changes to a `log.txt` file for reference.  
✔ **Color-coded Terminal Output** – Enhances visibility using `colorama`.  
✔ **Multi-platform Support** – Works seamlessly on **Linux, Windows, and Termux**.  

---

## 🛠 Installation  

### **For Linux & Windows**  
```bash
git clone https://github.com/Noureddindev/NoorWatch.git
cd NoorWatch
pip install -r requirements.txt
python3 noorwatch.py
```

*For Termux  *
```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/Noureddindev/NoorWatch.git
cd NoorWatch
pip install -r requirements.txt
python noorwatch.py
```

---

*⚡ Usage  *

To start monitoring a folder:  
```bash
python noorwatch.py
```
📂 When prompted, enter the *full path* of the folder you wish to monitor.  
📜 Changes will be displayed in the terminal and logged into *log.txt* .

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

Contributions are welcome! Feel free to submit *Pull Requests* or report any issues.  
Let's collaborate to make *NoorWatch* even better!  

🛠 *Developer:* [ASKAL NOUREDDIN](https://github.com/Noureddindev)  

---

*📜 License  *
This project is *open-source* and available under the *MIT License* .
