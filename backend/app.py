from flask import Flask, jsonify, send_file, send_from_directory
from flask_cors import CORS
from scraper import BookScraper
from data_handler import DataHandler
import os
import threading
import webbrowser
import sys

# Get absolute path to frontend directory
FRONTEND_PATH = os.path.join(os.path.dirname(__file__), '..', 'frontend')

# Flask app configuration
app = Flask(__name__,
            static_folder=FRONTEND_PATH,
            static_url_path='',
            template_folder=FRONTEND_PATH)

# ✅ Ensure proper Unicode (UTF-8) output for JSON
app.config['JSON_AS_ASCII'] = False

CORS(app)

# Serve frontend files
@app.route('/')
def serve_index():
    """Serve index.html"""
    return send_from_directory(FRONTEND_PATH, 'index.html')


@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static frontend files"""
    return send_from_directory(FRONTEND_PATH, filename)


# -------------------------
#        API ROUTES
# -------------------------

@app.route('/api/scrape', methods=['GET'])
def scrape():
    """Trigger scraping and return JSON result"""
    try:
        print("📚 Starting scrape...")
        books = BookScraper.scrape_books(max_pages=5)

        if books:
            success = DataHandler.save_to_csv(books)
            print(f"✅ Scraped {len(books)} books")
            return jsonify({
                'status': 'success' if success else 'error',
                'message': f'Scraped {len(books)} books successfully!' if success else 'Failed to save data',
                'count': len(books),
                'data': books
            }), 200 if success else 500
        else:
            print("❌ No books scraped")
            return jsonify({
                'status': 'error',
                'message': 'Failed to scrape books'
            }), 400

    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/data', methods=['GET'])
def get_data():
    """Return existing scraped data"""
    try:
        books = DataHandler.read_from_csv()
        return jsonify({
            'status': 'success',
            'count': len(books),
            'data': books
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/download', methods=['GET'])
def download_csv():
    """Download CSV file"""
    try:
        csv_path = DataHandler.CSV_FILE
        if not os.path.exists(csv_path):
            return jsonify({'status': 'error', 'message': 'No data file found. Scrape data first!'}), 404

        # ✅ Explicitly set correct encoding for CSV download
        return send_file(
            csv_path,
            mimetype='text/csv; charset=utf-8',
            as_attachment=True,
            download_name='scraped_data.csv'
        )

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'Backend is running'}), 200


# -------------------------
#       AUTO-LAUNCH
# -------------------------
def open_browser():
    """Automatically open browser"""
    import time
    time.sleep(2)
    try:
        webbrowser.open('http://127.0.0.1:5000')
        print("🌐 Browser opened!")
    except Exception as e:
        print(f"Could not open browser: {e}")


if __name__ == '__main__':
    if not os.path.exists(FRONTEND_PATH):
        print(f"❌ ERROR: Frontend folder not found at {FRONTEND_PATH}")
        sys.exit(1)

    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()

    print("\n" + "=" * 60)
    print("🚀 WebScraperApp Starting...")
    print("=" * 60)
    print(f"📱 Frontend: http://127.0.0.1:5000")
    print(f"🔌 API: http://127.0.0.1:5000/api")
    print(f"📂 Frontend Path: {FRONTEND_PATH}")
    print("=" * 60 + "\n")

    app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)
