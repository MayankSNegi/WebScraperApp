const API_BASE_URL = '/api';

const scrapeBtn = document.getElementById('scrapeBtn');
const downloadBtn = document.getElementById('downloadBtn');
const statusDiv = document.getElementById('status');
const loadingSpinner = document.getElementById('loadingSpinner');
const tableBody = document.getElementById('tableBody');
const totalBooksEl = document.getElementById('totalBooks');
const lastUpdatedEl = document.getElementById('lastUpdated');

// Event Listeners
scrapeBtn.addEventListener('click', handleScrape);
downloadBtn.addEventListener('click', handleDownload);

// Load data on page load
document.addEventListener('DOMContentLoaded', loadData);

/**
 * Handle scraping action
 */
async function handleScrape() {
    scrapeBtn.disabled = true;
    showLoading(true);
    showStatus('Scraping in progress...', 'loading');
    
    try {
        const response = await fetch(`${API_BASE_URL}/scrape`);
        const data = await response.json();
        
        if (data.status === 'success') {
            showStatus(`✅ ${data.message}`, 'success');
            displayBooks(data.data);
            updateStats(data.data);
            downloadBtn.disabled = false;
        } else {
            showStatus(`❌ ${data.message}`, 'error');
        }
    } catch (error) {
        console.error('Scrape error:', error);
        showStatus('❌ Error connecting to backend. Ensure the server is running!', 'error');
    } finally {
        scrapeBtn.disabled = false;
        showLoading(false);
    }
}

/**
 * Handle CSV download
 */
async function handleDownload() {
    try {
        const response = await fetch(`${API_BASE_URL}/download`);
        
        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'scraped_data.csv';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
            showStatus('✅ CSV downloaded successfully!', 'success');
        } else {
            showStatus('❌ Failed to download file', 'error');
        }
    } catch (error) {
        console.error('Download error:', error);
        showStatus('❌ Error downloading file', 'error');
    }
}

/**
 * Load existing data from backend
 */
async function loadData() {
    try {
        const response = await fetch(`${API_BASE_URL}/data`);
        const data = await response.json();
        
        if (data.data && data.data.length > 0) {
            displayBooks(data.data);
            updateStats(data.data);
            downloadBtn.disabled = false;
        }
    } catch (error) {
        console.error('Load data error:', error);
    }
}

/**
 * Display books in table
 */
function displayBooks(books) {
    if (books.length === 0) {
        tableBody.innerHTML = `
            <tr class="empty-row">
                <td colspan="5">No data available.</td>
            </tr>
        `;
        return;
    }
    
    tableBody.innerHTML = books.map((book, index) => `
        <tr>
            <td>${index + 1}</td>
            <td title="${book.title}">${book.title}</td>
            <td>${book.price}</td>
            <td>${book.availability}</td>
            <td><span class="rating">${book.rating}</span></td>
        </tr>
    `).join('');
}

/**
 * Update statistics
 */
function updateStats(books) {
    totalBooksEl.textContent = books.length;
    lastUpdatedEl.textContent = new Date().toLocaleString();
}

/**
 * Show status message
 */
function showStatus(message, type) {
    statusDiv.textContent = message;
    statusDiv.className = `status-message ${type}`;
    
    // Auto-clear after 5 seconds if success
    if (type === 'success') {
        setTimeout(() => {
            statusDiv.textContent = '';
            statusDiv.className = 'status-message';
        }, 5000);
    }
}

/**
 * Toggle loading spinner
 */
function showLoading(show) {
    loadingSpinner.classList.toggle('hidden', !show);
}