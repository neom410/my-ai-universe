# AI Universe Explorer - Complete Fixed Version
from flask import Flask, jsonify, render_template_string
import threading
import time
import json
import requests
from datetime import datetime
from collections import defaultdict, deque

# === UNIVERSE EXPLORER CLASS ===
class UniverseDataExplorer:
    """Core AI engine for autonomous universe exploration"""
    
    def __init__(self):
        self.data_universe = defaultdict(dict)
        self.autonomous_insights = []
        self.exploration_history = []
        self.pattern_memory = defaultdict(float)
        self.exploration_state = {
            'total_discoveries': 0,
            'universe_size': 0,
            'last_update': time.time()
        }
        
        print("🌌 Universe Data Explorer initialized")
        self._bootstrap_universe()
    
    def _bootstrap_universe(self):
        """Bootstrap initial universe discovery"""
        print("🚀 Bootstrapping universe discovery...")
        self._discover_crypto_universe()
        self._discover_news_universe()
        self._discover_research_universe()
        print(f"✅ Bootstrap complete: {self.get_total_entities()} entities discovered")
    
    def _discover_crypto_universe(self):
        """Discover cryptocurrency universe"""
        try:
            print("🪙 Discovering crypto universe...")
            url = "https://api.coingecko.com/api/v3/coins/markets"
            crypto_data = {}
            
            for page in range(1, 3):  # Top 500 crypto
                try:
                    params = {
                        'vs_currency': 'usd',
                        'order': 'market_cap_desc',
                        'per_page': 250,
                        'page': page
                    }
                    
                    response = requests.get(url, params=params, timeout=10)
                    if response.status_code == 200:
                        cryptos = response.json()
                        for crypto in cryptos:
                            symbol = crypto['symbol'].upper()
                            crypto_data[f"{symbol}-USD"] = {
                                'name': crypto['name'],
                                'current_price': crypto.get('current_price'),
                                'market_cap': crypto.get('market_cap'),
                                'price_change_24h': crypto.get('price_change_percentage_24h', 0),
                                'discovered_at': datetime.now().isoformat(),
                                'type': 'cryptocurrency'
                            }
                except Exception as e:
                    print(f"Crypto page {page} error: {e}")
                    continue
                
                time.sleep(1)
            
            self.data_universe['financial'] = crypto_data
            print(f"🪙 Discovered {len(crypto_data)} cryptocurrencies")
            
        except Exception as e:
            print(f"Crypto discovery error: {e}")
    
    def _discover_news_universe(self):
        """Discover news sources universe"""
        try:
            print("📰 Discovering news universe...")
            news_data = {
                'TechCrunch': {
                    'url': 'https://feeds.feedburner.com/TechCrunch',
                    'articles_count': 20,
                    'type': 'news_source',
                    'discovered_at': datetime.now().isoformat()
                },
                'Reuters Business': {
                    'url': 'https://feeds.reuters.com/reuters/businessNews',
                    'articles_count': 25,
                    'type': 'news_source',
                    'discovered_at': datetime.now().isoformat()
                }
            }
            
            self.data_universe['news'] = news_data
            print(f"📰 Discovered {len(news_data)} news sources")
            
        except Exception as e:
            print(f"News discovery error: {e}")
    
    def _discover_research_universe(self):
        """Discover research universe"""
        try:
            print("🧬 Discovering research universe...")
            research_categories = ['cs.AI', 'cs.LG', 'cs.CL', 'cs.CV', 'cs.RO']
            research_data = {}
            
            for category in research_categories:
                research_data[category] = {
                    'recent_papers': 10,
                    'category': category,
                    'discovered_at': datetime.now().isoformat(),
                    'type': 'research_category'
                }
            
            self.data_universe['research'] = research_data
            print(f"🧬 Discovered {len(research_data)} research domains")
            
        except Exception as e:
            print(f"Research discovery error: {e}")
    
    def autonomous_universe_exploration(self):
        """Perform autonomous exploration"""
        exploration_results = {
            'new_discoveries': 0,
            'patterns_found': 0,
            'insights_generated': 0,
            'timestamp': datetime.now().isoformat()
        }
        
        self._generate_autonomous_insights()
        self.exploration_state['total_discoveries'] = self.get_total_entities()
        self.exploration_state['last_update'] = time.time()
        exploration_results['insights_generated'] = len(self.autonomous_insights)
        
        return exploration_results
    
def _generate_autonomous_insights(self):
    """Generate ACTIONABLE insights with concrete data"""
    try:
        # Clear old insights if too many
        if len(self.autonomous_insights) > 15:
            self.autonomous_insights = self.autonomous_insights[-8:]
        
        # Get current data
        financial_data = self.data_universe.get('financial', {})
        domains = list(self.data_universe.keys())
        total_entities = self.get_total_entities()
        
        if financial_data:
            # CONCRETE PRICE ANALYSIS
            gainers = []
            losers = []
            high_volume = []
            cheap_gems = []
            expensive_coins = []
            
            for symbol, data in financial_data.items():
                if isinstance(data, dict):
                    price = data.get('current_price', 0)
                    change = data.get('price_change_24h', 0)
                    market_cap = data.get('market_cap', 0)
                    name = data.get('name', symbol)
                    
                    # Top gainers
                    if change > 10:
                        gainers.append((name, symbol, round(change, 1), price))
                    
                    # Top losers
                    if change < -10:
                        losers.append((name, symbol, round(change, 1), price))
                    
                    # High market cap (valuable)
                    if market_cap and market_cap > 1000000000:  # >1B
                        high_volume.append((name, symbol, price, market_cap))
                    
                    # Cheap potential gems
                    if price and 0.01 <= price <= 1.0 and change > 5:
                        cheap_gems.append((name, symbol, price, round(change, 1)))
                    
                    # Expensive coins
                    if price and price > 100:
                        expensive_coins.append((name, symbol, price, round(change, 1)))
            
            # Sort lists
            gainers.sort(key=lambda x: x[2], reverse=True)  # By % change
            losers.sort(key=lambda x: x[2])  # By % change (most negative first)
            high_volume.sort(key=lambda x: x[3], reverse=True)  # By market cap
            cheap_gems.sort(key=lambda x: x[3], reverse=True)  # By % change
            expensive_coins.sort(key=lambda x: x[2], reverse=True)  # By price
            
            # ACTIONABLE INSIGHTS
            
            # 1. TOP GAINERS
            if gainers:
                top_gainers = gainers[:5]
                insight_text = f"🚀 TOP GAINERS: "
                for name, symbol, change, price in top_gainers:
                    clean_symbol = symbol.replace('-USD', '')
                    insight_text += f"{clean_symbol} +{change}% (${price:.4f}), "
                insight_text = insight_text.rstrip(', ')
                
                self.autonomous_insights.append({
                    'type': 'top_gainers',
                    'description': insight_text,
                    'actionable': f"Consider research on {len(top_gainers)} high-momentum coins",
                    'data': top_gainers,
                    'timestamp': datetime.now().isoformat()
                })
            
            # 2. TOP LOSERS (POTENTIAL OPPORTUNITIES)
            if losers:
                top_losers = losers[:3]
                insight_text = f"📉 POTENTIAL OPPORTUNITIES (Big Drops): "
                for name, symbol, change, price in top_losers:
                    clean_symbol = symbol.replace('-USD', '')
                    insight_text += f"{clean_symbol} {change}% (${price:.4f}), "
                insight_text = insight_text.rstrip(', ')
                
                self.autonomous_insights.append({
                    'type': 'potential_opportunities',
                    'description': insight_text,
                    'actionable': "Research if drops are temporary or fundamental issues",
                    'data': top_losers,
                    'timestamp': datetime.now().isoformat()
                })
            
            # 3. CHEAP GEMS ANALYSIS
            if cheap_gems:
                gems = cheap_gems[:3]
                insight_text = f"💎 CHEAP GEMS (Rising & Under $1): "
                for name, symbol, price, change in gems:
                    clean_symbol = symbol.replace('-USD', '')
                    insight_text += f"{clean_symbol} ${price:.4f} (+{change}%), "
                insight_text = insight_text.rstrip(', ')
                
                self.autonomous_insights.append({
                    'type': 'cheap_gems',
                    'description': insight_text,
                    'actionable': f"Low-price coins with upward momentum - research fundamentals",
                    'data': gems,
                    'timestamp': datetime.now().isoformat()
                })
            
            # 4. BLUE CHIP ANALYSIS
            if high_volume:
                blue_chips = high_volume[:5]
                insight_text = f"🏦 BLUE CHIP STATUS: "
                for name, symbol, price, mcap in blue_chips:
                    clean_symbol = symbol.replace('-USD', '')
                    mcap_b = mcap / 1000000000  # Convert to billions
                    insight_text += f"{clean_symbol} ${price:.2f} (${mcap_b:.1f}B mcap), "
                insight_text = insight_text.rstrip(', ')
                
                self.autonomous_insights.append({
                    'type': 'blue_chip_analysis',
                    'description': insight_text,
                    'actionable': "Stable large-cap coins for conservative portfolio allocation",
                    'data': blue_chips,
                    'timestamp': datetime.now().isoformat()
                })
            
            # 5. EXPENSIVE COINS WATCH
            if expensive_coins:
                expensive = expensive_coins[:3]
                insight_text = f"💰 HIGH-VALUE COINS: "
                for name, symbol, price, change in expensive:
                    clean_symbol = symbol.replace('-USD', '')
                    insight_text += f"{clean_symbol} ${price:.0f} ({change:+.1f}%), "
                insight_text = insight_text.rstrip(', ')
                
                self.autonomous_insights.append({
                    'type': 'high_value_watch',
                    'description': insight_text,
                    'actionable': "Premium coins - track for institutional adoption signals",
                    'data': expensive,
                    'timestamp': datetime.now().isoformat()
                })
            
            # 6. MARKET TEMPERATURE
            total_positive = len([x for x in financial_data.values() 
                                if isinstance(x, dict) and x.get('price_change_24h', 0) > 0])
            total_negative = len([x for x in financial_data.values() 
                                if isinstance(x, dict) and x.get('price_change_24h', 0) < 0])
            
            if total_positive > total_negative:
                market_sentiment = "BULLISH"
                emoji = "🟢"
            else:
                market_sentiment = "BEARISH" 
                emoji = "🔴"
            
            percentage_up = (total_positive / len(financial_data)) * 100
            
            self.autonomous_insights.append({
                'type': 'market_sentiment',
                'description': f"{emoji} MARKET SENTIMENT: {market_sentiment} - {percentage_up:.0f}% of coins are green ({total_positive} up, {total_negative} down)",
                'actionable': f"Market is {market_sentiment.lower()} - adjust strategy accordingly",
                'sentiment': market_sentiment,
                'timestamp': datetime.now().isoformat()
            })
            
            # 7. VOLATILITY ALERT
            high_volatility = []
            for symbol, data in financial_data.items():
                if isinstance(data, dict):
                    change = abs(data.get('price_change_24h', 0))
                    if change > 20:  # Very volatile
                        name = data.get('name', symbol)
                        price = data.get('current_price', 0)
                        high_volatility.append((name, symbol, change, price))
            
            if high_volatility:
                vol_coins = sorted(high_volatility, key=lambda x: x[2], reverse=True)[:3]
                insight_text = f"⚡ HIGH VOLATILITY ALERT: "
                for name, symbol, change, price in vol_coins:
                    clean_symbol = symbol.replace('-USD', '')
                    insight_text += f"{clean_symbol} ±{change:.0f}% (${price:.4f}), "
                insight_text = insight_text.rstrip(', ')
                
                self.autonomous_insights.append({
                    'type': 'volatility_alert',
                    'description': insight_text,
                    'actionable': "Extreme volatility detected - high risk/reward potential",
                    'data': vol_coins,
                    'timestamp': datetime.now().isoformat()
                })
        
        # 8. SYSTEM STATUS WITH CONCRETE DATA
        self.autonomous_insights.append({
            'type': 'discovery_summary',
            'description': f"📊 ACTIVE MONITORING: {len(financial_data)} cryptocurrencies, {len(self.data_universe.get('news', {}))} news sources, {len(self.data_universe.get('research', {}))} research domains",
            'actionable': f"Real-time data on {len(financial_data)} digital assets available for analysis",
            'timestamp': datetime.now().isoformat()
        })
        
        print(f"💡 Generated {len(self.autonomous_insights)} actionable insights")
        
    except Exception as e:
        print(f"Insight generation error: {e}")
        # Fallback insight
        self.autonomous_insights.append({
            'type': 'system_status',
            'description': f"🔍 AI actively exploring universe - {self.get_total_entities()} entities tracked",
            'actionable': "Data collection in progress - check back for detailed analysis",
            'timestamp': datetime.now().isoformat()
        })
    
    def _universal_search(self, search_term):
        """Search across entire universe"""
        search_results = {
            'search_term': search_term,
            'results_by_domain': {},
            'total_matches': 0,
            'timestamp': datetime.now().isoformat()
        }
        
        search_lower = search_term.lower()
        
        for domain, data in self.data_universe.items():
            domain_matches = []
            
            for entity, details in data.items():
                if search_lower in entity.lower():
                    domain_matches.append({
                        'entity': entity,
                        'match_type': 'name',
                        'details': details
                    })
                elif isinstance(details, dict):
                    for key, value in details.items():
                        if isinstance(value, str) and search_lower in value.lower():
                            domain_matches.append({
                                'entity': entity,
                                'match_type': key,
                                'match_value': value
                            })
                            break
            
            if domain_matches:
                search_results['results_by_domain'][domain] = domain_matches
                search_results['total_matches'] += len(domain_matches)
        
        return search_results
    
    def get_universe_status(self):
        """Get current universe status"""
        universe_stats = {}
        
        for domain, data in self.data_universe.items():
            universe_stats[domain] = {
                'total_entities': len(data),
                'sample_entities': list(data.keys())[:3]
            }
        
        return {
            'universe_statistics': universe_stats,
            'total_discoveries': self.get_total_entities(),
            'autonomous_insights': len(self.autonomous_insights),
            'exploration_state': self.exploration_state,
            'timestamp': datetime.now().isoformat()
        }
    
    def get_recent_insights(self, limit=10):
        """Get recent insights"""
        recent_insights = []
        
        for insight in self.autonomous_insights[-limit:]:
            recent_insights.append({
                'category': insight.get('type', 'general'),
                'description': insight.get('description', ''),
                'timestamp': insight.get('timestamp', ''),
                'details': insight.get('details', {})
            })
        
        return recent_insights
    
    def get_total_entities(self):
        """Get total entities discovered"""
        return sum(len(domain_data) for domain_data in self.data_universe.values())

# === FLASK APP ===
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
            time.sleep(600)

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
            .insight-item { border-bottom: 1px solid #333; padding: 10px 0; }
            .insight-category { color: #00ff88; font-weight: bold; }
            .insight-description { margin: 5px 0; }
            .insight-timestamp { color: #888; font-size: 0.8em; }
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
                <input type="text" id="searchInput" placeholder="Search anything in the universe..." style="width: 70%; padding: 10px; margin-right: 10px; background: #333; color: #fff; border: 1px solid #555;">
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
            setInterval(updateDashboard, 30000);
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
                        container.innerHTML = insights.slice(0, 8).map(insight => 
                            `<div class="insight-item">
                                <div class="insight-category">${insight.category}</div>
                                <div class="insight-description">${insight.description}</div>
                                <div class="insight-timestamp">${insight.timestamp}</div>
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
                updateDashboard();
            }
            
            async function exploreMore() {
                try {
                    const response = await fetch('/explore');
                    const result = await response.json();
                    alert('🚀 New exploration triggered! ' + result.result.insights_generated + ' insights generated');
                    setTimeout(() => {
                        updateDashboard();
                        loadInsights();
                    }, 2000);
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
    return jsonify(explorer.get_universe_status())

@app.route('/insights')
def insights():
    return jsonify(explorer.get_recent_insights())

@app.route('/search/<term>')
def search(term):
    return jsonify(explorer._universal_search(term))

@app.route('/explore')
def trigger_exploration():
    try:
        result = explorer.autonomous_universe_exploration()
        return jsonify({"success": True, "result": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
