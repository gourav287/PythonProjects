# 🧮 CLI Tracker

A simple Python command-line application to **track daily activities**, including meals, water intake, physical activity, and notes. Data is stored locally in a JSON file, and the app supports adding, viewing, and deleting entries.

---

## 📦 Features

- 📅 Add entries with date, category (meal, water, activity, notes), and details  
- 🔍 View entries with filters and limits  
- 🗑️ Delete specific entries or all entries  
- 🧪 Validates user input for accuracy  
- 🧾 Saves entries in a readable JSON format  
- 🪵 Logs actions to `tracker.log`

---

## 🖥️ Installation

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/cli-tracker.git
cd cli-tracker
```

2. **(Optional) Create a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Run the tracker**:

```bash
python tracker.py --help
```

---

## 🚀 Usage

➕ Add an Entry

```bash
python tracker.py add --category meal --details "Lunch: rice and veggies"
Optional flags:
--date YYYY-MM-DD – Defaults to today if not provided
--category – One of meal, water, activity, notes
--details – Required
```

👀 View Entries

```bash
python tracker.py view
Optional filters:
--limit 10 – Show up to 10 entries (default: 5)
--date YYYY-MM-DD – Filter by date
--category – Filter by category
```

🗑️ Delete Entries

Delete a specific entry:
```bash
python tracker.py delete --date 2025-05-26 --category water
```

Delete all entries:
```bash
python tracker.py delete --all
```

---

## 📁 Project Structure

```bash
cli-tracker/
├── tracker.py                 # Main script
├── parser_arguments.py        # Argument parsing logic
├── validations.py             # Input validation helpers
├── database_util.py           # JSON and file operations
├── cli_tracker.json           # Stored data
├── tracker.log                # Action logs
└── README.md                  # Documentation
```

---

## 🛠️ Planned Enhancements

 Add keyword search in details

 Export to CSV

 Add summary stats (e.g., water per day)

 ---

 ## 🤝 Contributing

Pull requests and feedback are welcome. If you'd like to contribute:
- Fork the repo
- Create your feature branch (git checkout -b feature/YourFeature)
- Commit your changes (git commit -m 'Add feature')
- Push to the branch (git push origin feature/YourFeature)
- Open a pull request

## 🧠 Credits
Created by Gourav
