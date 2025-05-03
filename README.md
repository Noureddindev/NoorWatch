# NoorWatch
```markdown
NoorWatch – Folder Activity Monitor

Monitor file and folder activities in real-time using Python.  
*NoorWatch* is a lightweight script to detect any changes in a specific directory (creation, modification, deletion, moving of files).

---

📌 Features

- Real-time monitoring of file/folder changes
- Detects creation, deletion, modification, and moves
- Color-coded console output
- All events are logged automatically in `log.txt`
- Easy to use and cross-platform

---

⚙ Requirements

- Python 3.6+
- Required libraries:
  - `watchdog`
  - `colorama`

Install the dependencies with:

```bash
pip install watchdog colorama
```

---

▶️ Usage

1. Clone the repository:

```bash
git clone https://github.com/Noureddindev/NoorWatch.git
cd NoorWatch
```

2. Run the script:

```bash
python noorwatch.py
```

3. Enter the full path to the folder you want to monitor when prompted.

4. All file events will be displayed in the terminal and saved to `log.txt`.

---

📁 Example Output

```bash
[Created] /home/user/Desktop/test/new_file.txt
[Modified] /home/user/Desktop/test/info.docx
[Deleted] /home/user/Desktop/test/old_file.py
[Moved] from /home/user/Desktop/test/file.txt to /home/user/Desktop/test/archive/file.txt
```

---

🧑‍💻 Developer

- *Name:* Askal Noureddin  
- *GitHub:* [Noureddindev](https://github.com/Noureddindev)

---

📄 License

This project is open-source and free to use under the MIT License.
