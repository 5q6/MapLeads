# 🔍 MapLeads

> A desktop tool that finds cafes, restaurants, and local businesses on **Google Maps** and scores them as sales leads — then exports everything to Excel in one click.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🗺️ **Google Places Search** | Search any city + keyword via the Places API (New) |
| 📊 **Lead Scoring** | Automatically scores each business (0–100) based on missing website, phone, and low ratings |
| 📧 **Email Extraction** | Scrapes the business website for contact emails |
| 📥 **Excel Export** | One-click export to `.xlsx` with all lead data |
| 🗄️ **SQLite Storage** | Persists all results locally for later use |

---

## 🖥️ Screenshot

> Search → Score → Export. All in a simple desktop GUI.

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/5q6/MapLeads.git
cd MapLeads
```

### 2. Create and activate a virtual environment *(recommended)*
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
```bash
# Copy the example file
copy .env.example .env       # Windows
cp .env.example .env         # macOS / Linux
```
Then open `.env` and replace `YOUR_GOOGLE_PLACES_API_KEY` with your real key.

### 5. Run the app
```bash
python app.py
```

---

## 🔑 Getting a Google Places API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select an existing one)
3. Navigate to **APIs & Services → Library**
4. Search for **"Places API (New)"** and click **Enable**
5. Go to **APIs & Services → Credentials**
6. Click **Create Credentials → API Key**
7. Copy the key and paste it into your `.env` file

> **Tip:** Restrict your key to the Places API only under *API restrictions* to keep it secure.

---

## 📁 Project Structure

```
MapLeads/
├── app.py              # Entry point — initializes DB and launches GUI
├── gui.py              # Tkinter desktop interface
├── google_places.py    # Google Places API integration
├── lead_score.py       # Lead opportunity scoring logic
├── email_finder.py     # Email scraper from business websites
├── excel_export.py     # Excel (.xlsx) export
├── database.py         # SQLite storage
├── config.py           # Loads API key from .env
├── requirements.txt    # Python dependencies (pinned versions)
├── .env.example        # Template for environment variables
└── .gitignore          # Protects secrets and output files
```

---

## ⚙️ How Lead Scoring Works

Each business is scored out of **100**. A higher score means a better sales opportunity (e.g., a business with no website is easier to sell web services to).

| Condition | Points Added |
|---|---|
| Base score | 50 |
| No website | +20 |
| No phone number | +10 |
| Rating < 4.0 | +15 |
| **Maximum** | **100** |

---

## 📦 Dependencies

| Package | Version | Purpose |
|---|---|---|
| `requests` | 2.32.3 | HTTP calls to Google Places API and websites |
| `openpyxl` | 3.1.5 | Excel file generation |
| `python-dotenv` | 1.0.1 | Loads API key from `.env` file securely |

> `tkinter` and `sqlite3` are included in the Python standard library — no extra install needed.

---

## 🔒 Security Notes

- **Never commit your `.env` file.** It is listed in `.gitignore` by default.
- The `output/` and `data/` folders (Excel files and the SQLite database) are also excluded from Git to protect any scraped personal data.
- Rotate your Google API key if you ever accidentally expose it.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create your branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request
