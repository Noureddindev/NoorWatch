
# NoorWatch

## 📂 Folder Activity Monitor  
**NoorWatch** is a real-time folder monitoring tool developed by **ASKAL NOUREDDIN**.  
It tracks changes within a specified folder, detecting file **creation, modification, deletion, and movement**, while logging all events in `log.txt`.

---

## 🚀 Features  
✔ **Real-time monitoring** of folder activity.  
✔ **Logs all detected changes** in `log.txt`.  
✔ **Color-coded notifications** using `colorama`.  
✔ **Compatible with Linux, Windows, and Termux (Android).**  
✔ **Lightweight and easy to use** without unnecessary complexity.  

---

## 🛠️ Installation  

### 🔹 **Linux & Windows**  
```bash
git clone https://github.com/Noureddindev/NoorWatch.git
cd NoorWatch
pip install watchdog colorama
python3 NoorWatch.py
```

*🔹 Termux (Android)  *
```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/Noureddindev/NoorWatch.git
cd NoorWatch
pip install watchdog colorama
termux-setup-storage  # Grant file access permissions
python NoorWatch.py
```

---

*⚡ Usage  *

💡 *Run the program:*  
```bash
python NoorWatch.py
```
📂 Enter the *full path* of the folder when prompted, for example:  
```bash
/storage/emulated/0/Download
```
📜 All changes will be displayed in the terminal and logged in *log.txt* .

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

💡 Contributions are welcome! You can submit *Pull Requests* or report issues.  
🔗 *GitHub:* [ASKAL](https://github.com/Noureddindev)  

---

*📜 License  *
This project is *open-source* and available under the *MIT License* .
