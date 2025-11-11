# 📚 WebScraperApp

A **full-stack web scraping application** built using **Python (Flask)** and **BeautifulSoup**, designed to extract, visualize, and manage structured data from [Books to Scrape](https://books.toscrape.com).

---

## 🌐 What is a Web Scraper?

A **web scraper** is an automated system that extracts useful information from websites.  
It works by requesting a web page, reading its HTML content, and filtering out relevant data fields.

In essence:
> **Web Scraping = Data Extraction Automation from the Web**

Organizations, researchers, and analysts use scrapers to collect **large-scale public data** for insights, product tracking, and decision-making — replacing manual data collection with fast, repeatable automation.

---

## 🤖 What This Scraper Does

**WebScraperApp** targets the open dataset site **Books to Scrape**, a sandbox for testing web data extraction.  
It automatically collects and organizes structured book details such as:

- 📘 **Title**  
- 💰 **Price**  
- 🏷️ **Availability**  
- ⭐ **Rating**

After extraction, the data is:
- Saved to a **CSV file (`data/scraped_data.csv`)**
- Displayed dynamically in an **interactive web interface**
- Made available for **download and further analytics**

---

## 🚀 Key Features (Action + What + How + Impact)

| # | Action | What | How | Impact / Application |
|---|---------|------|------|----------------------|
| 1️⃣ | **Developed** | a full-stack web scraping application | using Flask backend, BeautifulSoup parser, and JS frontend | Enables automated data collection and integration into analytics systems |
| 2️⃣ | **Extracted** | structured data fields from HTML content | by parsing the DOM structure with BeautifulSoup | Transforms unstructured web content into machine-readable formats |
| 3️⃣ | **Implemented** | RESTful APIs for scraping, data access, and download | using Flask and Flask-CORS | Facilitates interoperability between frontend systems and backend services |
| 4️⃣ | **Automated** | data storage workflow | with CSV serialization and read/write operations | Provides persistent, portable datasets for offline analysis |
| 5️⃣ | **Designed** | a responsive web interface | with HTML5, CSS3, and vanilla JS | Improves data accessibility and visualization across devices |
| 6️⃣ | **Ensured** | robust error handling | via exception blocks in scraper logic | Increases system reliability and fault tolerance during runtime |
| 7️⃣ | **Structured** | modular project architecture | separating backend, frontend, and data layers | Supports maintainability and scalable codebase expansion |
| 8️⃣ | **Enabled** | automatic browser launching | via Python’s `webbrowser` and threading | Enhances usability and testing convenience |

---

## 🧠 Technologies Used

| Layer | Technology | Purpose |
|-------|-------------|----------|
| **Backend** | Flask (Python), Flask-CORS | REST API, data routing, static serving |
| **Scraping Engine** | BeautifulSoup4, requests | HTML parsing & extraction |
| **Frontend** | HTML5, CSS3, JavaScript | Visualization and interactivity |
| **Data Layer** | CSV (Python `csv` module) | Persistent storage of structured data |
| **Environment** | venv (Virtual Environment) | Dependency isolation |

---

## 📁 Project Structure
WebScraperApp/<br>
├── backend/<br>
│ ├── venv/ ← Python virtual environment<br>
│ ├── init.py<br>
│ ├── app.py ← Flask app (main entry)<br>
│ ├── scraper.py ← Scraper logic (BeautifulSoup)<br>
│ ├── data_handler.py ← CSV read/write handler<br>
│ └── requirements.txt ← Dependencies<br>
│<br>
├── frontend/<br>
│ ├── index.html ← Dashboard UI<br>
│ ├── style.css ← Styling <br>
│ └── script.js ← API & interactivity logic<br>
│<br>
├── data/<br>
│ └── scraped_data.csv ← Generated output file<br>
└── README.md
---

## ⚙️ Setup & Installation

### **1️⃣ Clone the Repository**
- git clone https://github.com/your-username/WebScraperApp.git
- cd WebScraperApp
### **2️⃣ Create Virtual Environment (inside backend/)**
- cd backend
- python -m venv venv
- Activate it:
- - Windows: venv\Scripts\activate
- - macOS/Linux: source venv/bin/activate
### **3️⃣ Install Dependencies**
- pip install -r requirements.txt
### **4️⃣ Run the App**
- python app.py
✅ Browser opens automatically at
👉 http://127.0.0.1:5000
 
---

## 💻 Usage
- Click 🔄 Start Scraping to begin extraction
- Wait until scraping finishes (logs appear in terminal)
- View all books in the table below
- Click 📥 Download CSV to save the dataset locally

---

## 🔍 Understanding How It Works
- 1️⃣ Frontend UI
- → Displays data and user controls using HTML/CSS/JS
- 2️⃣ Flask Backend
- → Handles /api/scrape, /api/data, /api/download routes
- 3️⃣ Scraper Module (scraper.py)
- → Sends HTTP requests and parses the HTML
- → Extracts required fields
- 4️⃣ Data Handler (data_handler.py)
- → Saves extracted results into scraped_data.csv
- → Reads existing CSV data when reloading page

---

## 🧱 Future Enhancements
- Integrate with a database (SQLite / MongoDB)
- Add data visualization (Chart.js or Plotly)
- Enable scheduled scraping (cron jobs)
- Add multiple target sites
- Deploy to cloud (Render / Railway / Vercel)

---

## 🏁 Conclusion

- WebScraperApp encapsulates the essence of data automation, backend engineering, and frontend integration.<br>
- It bridges the gap between raw web content and structured, analyzable data — a core component of modern data intelligence systems.<br>
- This project exemplifies how small-scale automation can have large-scale impact in research, analytics, and digital operations.<br>

---

## 👨‍💻 Author
### [Mayank Singh Negi](https://github.com/MayankSNegi)