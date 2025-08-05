# 🏛️ Court Data Fetcher & Mini Dashboard

This is a simple Flask web app that allows users to enter court case details (case type, number, year) and fetches dummy scraped data. It also logs each query to a local SQLite database and provides a view of past queries.

---

## ✨ Features

- 📥 Form to enter court case details
- 🧠 Dynamic dummy data generation based on input
- 📄 Simulated PDF order links
- 📚 Query logging using SQLite
- 📊 Query log page to view all past queries
- ✅ Clean UI with HTML/CSS styling

---

## 🛠️ Technologies Used

- Python
- Flask
- SQLite3
- HTML + CSS

---

## 🚀 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/mohammedsohail45/court-dashboard.git
cd court-dashboard
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
python app.py
```

Visit: `http://127.0.0.1:5000`
```
## 📂 Project Structure

```
court-dashboard/
│
├── app.py               # Main Flask app
├── scraper.py           # Simulated scraping logic
├── log_query.py         # Logging logic using SQLite
├── templates/
│   ├── index.html       # Main form + results page
│   └── queries.html     # Query logs
├── static/              # (Optional for CSS/images)
├── requirements.txt     # Python dependencies
└── README.md            # Project overview
```

---

## 🧠 Additional Notes

- This project uses dummy data instead of real scraping (due to captcha restrictions).
- PDF links are simulated and dynamically generated.
- All queries are logged and visible at `/queries` route.

---

## 📜 Attribution

> ⚙️ **Note:** This project was built with guidance and help from **ChatGPT by OpenAI** for code assistance, bug fixing, and overall project structuring.

---

## 📬 Contact

For questions or suggestions:
📧 [mohammedsohail45@yourmail.com](mailto:mohdsohail96638@gmail.com)

---

