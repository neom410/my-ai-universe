# Copia questo codice e salvalo come "app.py"
from flask import Flask, jsonify, render_template_string
import threading
import time
import json
from datetime import datetime
from universe_explorer import UniverseDataExplorer

app = Flask(__name__)

# Initialize AI Universe Explorer
explorer = UniverseDataExplorer()
exploration_active = True

# Background exploration thread
def continuous_exploration():
    global exploration_active
    while exploration_active:
        try:
            result = explorer.autonomous_universe_exploration()
            print(f"🔍 Auto-discovery: {result}")
            time.sleep(300)  # Every 5 minutes
        except Exception as e:
            print(f"Exploration error: {e}")
            time.sleep(600)  # Wait 10 min on error

# Start background exploration
exploration_thread = threading.Thread(target=continuous_exploration)
exploration_thread.daemon = True
exploration_thread.start()

@app.route('/')
def dashboard():
    """Main dashboard"""
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🌌 AI Universe Explorer</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background: #0a0a0a; color: #fff; }
            .container { max-width: 800px; margin: 0 auto; }
            .card { background: #1a1a1a; padding: 20px; margin: 10px 0; border-radius: 10px; border-left: 4px solid #00ff88; }
            .status { display: flex; justify-content: space-between; flex-wrap: wrap; }
            .metric { text-align: center; margin: 10px; }
            .metric h3 { margin: 0; color: #00ff88; font-size: 2em; }
            .metric p { margin: 5px 0; color: #888; }
            button { background: #00ff88; color: black; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; margin: 5px; }
            button:hover { background: #00cc70; }
            .insights { max-height: 300px; overflow-y: auto; }
            @media (max-width: 600px) { .status { flex-direction: column; } }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌌 AI Universe Explorer</h1>
            <p>Autonomous AI exploring the entire data universe 24/7</p>
            
            <div class="card">
                <h2>📊 Universe Status</h2>
                <div class="status" id="status">
                    <div class="metric">
                        <h3 id="entities">Loading...</h3>
                        <p>Total Entities</p>
                    </div>
                    <div class="metric">
                        <h3 id="insights">Loading...</h3>
                        <p>AI Insights</p>
                    </div>
                    <div class="metric">
                        <h3 id="domains">Loading...</h3>
                        <p>Data Domains</p>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <h2>🔍 Search Universe</h2>
                <input type="text" id="searchInput" placeholder="Search anything in the universe..." style="width: 70%; padding: 10px; margin-right: 10px;">
                <button onclick="searchUniverse()">Search</button>
                <div id="searchResults"></div>
            </div>
            
            <div class="card">
                <h2>💡 Latest AI Insights</h2>
                <div id="insights-list" class="insights">Loading insights...</div>
                <button onclick="refreshInsights()">Refresh Insights</button>
            </div>
            
            <div class="card">
                <h2>🌍 Quick Actions</h2>
                <button onclick="window.location.href='/status'">Full Status JSON</button>
                <button onclick="window.location.href='/insights'">All Insights JSON</button>
                <button onclick="exploreMore()">Trigger New Exploration</button>
            </div>
        </div>
        
        <script>
            // Auto-refresh every 30 seconds
            setInterval(updateDashboard, 30000);
            
            // Initial load
            updateDashboard();
            loadInsights();
            
            async function updateDashboard() {
                try {
                    const response = await fetch('/status');
                    const data = await response.json();
                    
                    document.getElementById('entities').textContent = data.total_discoveries || '0';
                    document.getElementById('insights').textContent = data.autonomous_insights || '0';
                    document.getElementById('domains').textContent = Object.keys(data.universe_statistics || {}).length;
                } catch (e) {
                    console.error('Error updating dashboard:', e);
                }
            }
            
            async function loadInsights() {
                try {
                    const response = await fetch('/insights');
                    const insights = await response.json();
                    
                    const container = document.getElementById('insights-list');
                    if (insights.length > 0) {
                        container.innerHTML = insights.slice(0, 5).map(insight => 
                            `<div style="border-bottom: 1px solid #333; padding: 10px 0;">
                                <strong>${insight.category}</strong><br>
                                <small>${insight.timestamp}</small>
                            </div>`
                        ).join('');
                    } else {
                        container.innerHTML = '<p>🤖 AI is exploring... insights coming soon!</p>';
                    }
                } catch (e) {
                    console.error('Error loading insights:', e);
                }
            }
            
            async function searchUniverse() {
                const query = document.getElementById('searchInput').value;
                if (!query) return;
                
                const resultsDiv = document.getElementById('searchResults');
                resultsDiv.innerHTML = '<p>🔍 Searching universe...</p>';
                
                try {
                    const response = await fetch(`/search/${encodeURIComponent(query)}`);
                    const results = await response.json();
                    
                    if (results.total_matches > 0) {
                        resultsDiv.innerHTML = `
                            <h4>Found ${results.total_matches} matches:</h4>
                            ${Object.entries(results.results_by_domain).map(([domain, matches]) => 
                                `<p><strong>${domain}:</strong> ${matches.length} matches</p>`
                            ).join('')}
                        `;
                    } else {
                        resultsDiv.innerHTML = '<p>❌ No matches found in current universe</p>';
                    }
                } catch (e) {
                    resultsDiv.innerHTML = '<p>⚠️ Search error occurred</p>';
                }
            }
            
            function refreshInsights() {
                loadInsights();
            }
            
            async function exploreMore() {
                try {
                    const response = await fetch('/explore');
                    alert('🚀 New exploration triggered!');
                    setTimeout(updateDashboard, 2000);
                } catch (e) {
                    alert('⚠️ Exploration trigger failed');
                }
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html_template)

@app.route('/status')
def status():
    """Get universe status"""
    return jsonify(explorer.get_universe_status())

@app.route('/insights')
def insights():
    """Get recent insights"""
    return jsonify(explorer.get_recent_insights())

@app.route('/search/<term>')
def search(term):
    """Search universe"""
    return jsonify(explorer._universal_search(term))

@app.route('/explore')
def trigger_exploration():
    """Trigger new exploration"""
    try:
        result = explorer.autonomous_universe_exploration()
        return jsonify({"success": True, "result": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
