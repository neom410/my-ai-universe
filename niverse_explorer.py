# AI Universe Explorer - Core Engine
import requests
import json
import time
import random
from datetime import datetime
from collections import defaultdict, deque

class UniverseDataExplorer:
    """
    Core AI engine for autonomous universe exploration
    """
    
    def __init__(self):
        # Discovery systems
        self.data_universe = defaultdict(dict)
        self.autonomous_insights = []
        self.exploration_history = []
        self.pattern_memory = defaultdict(float)
        self.world_pattern_memory = defaultdict(float)
        
        # Exploration state
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
        
        # Auto-discover crypto universe
        self._discover_crypto_universe()
        
        # Auto-discover news sources
        self._discover_news_universe()
        
        # Auto-discover research domains
        self._discover_research_universe()
        
        print(f"✅ Bootstrap complete: {self.get_total_entities()} entities discovered")
    
    def _discover_crypto_universe(self):
        """Discover cryptocurrency universe"""
        try:
            print("🪙 Discovering crypto universe...")
            
            url = "https://api.coingecko.com/api/v3/coins/markets"
            crypto_data = {}
            
            for page in range(1, 4):  # Top 750 crypto
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
                
                time.sleep(1)  # Rate limiting
            
            self.data_universe['financial'] = crypto_data
            print(f"🪙 Discovered {len(crypto_data)} cryptocurrencies")
            
        except Exception as e:
            print(f"Crypto discovery error: {e}")
    
    def _discover_news_universe(self):
        """Discover news sources universe"""
        try:
            print("📰 Discovering news universe...")
            
            news_sources = [
                'https://feeds.feedburner.com/TechCrunch',
                'https://www.wired.com/feed/rss',
                'https://feeds.reuters.com/reuters/businessNews'
            ]
            
            news_data = {}
            
            for source_url in news_sources:
                try:
                    import feedparser
                    feed = feedparser.parse(source_url)
                    
                    if feed.entries:
                        source_name = feed.feed.get('title', source_url)
                        news_data[source_name] = {
                            'url': source_url,
                            'articles_count': len(feed.entries),
                            'latest_article': feed.entries[0].get('title', '') if feed.entries else '',
                            'discovered_at': datetime.now().isoformat(),
                            'type': 'news_source'
                        }
                except Exception as e:
                    print(f"News source error: {e}")
                    continue
            
            self.data_universe['news'] = news_data
            print(f"📰 Discovered {len(news_data)} news sources")
            
        except Exception as e:
            print(f"News discovery error: {e}")
    
    def _discover_research_universe(self):
        """Discover research universe"""
        try:
            print("🧬 Discovering research universe...")
            
            research_categories = [
                'cs.AI', 'cs.LG', 'cs.CL', 'cs.CV', 'cs.RO',
                'physics.gen-ph', 'math.NA', 'stat.ML', 'q-bio.BM'
            ]
            
            research_data = {}
            
            for category in research_categories:
                try:
                    url = f"http://export.arxiv.org/api/query?search_query=cat:{category}&start=0&max_results=10&sortBy=submittedDate&sortOrder=descending"
                    
                    response = requests.get(url, timeout=10)
                    if response.status_code == 200:
                        paper_count = response.text.count('<entry>')
                        research_data[category] = {
                            'recent_papers': paper_count,
                            'category': category,
                            'discovered_at': datetime.now().isoformat(),
                            'type': 'research_category'
                        }
                except Exception as e:
                    print(f"Research category {category} error: {e}")
                    continue
                
                time.sleep(1)  # Rate limiting
            
            self.data_universe['research'] = research_data
            print(f"🧬 Discovered {len(research_data)} research domains")
            
        except Exception as e:
            print(f"Research discovery error: {e}")
    
    def autonomous_universe_exploration(self):
        """Perform autonomous exploration"""
        print("🔍 Starting autonomous exploration...")
        
        exploration_results = {
            'new_discoveries': 0,
            'patterns_found': 0,
            'insights_generated': 0,
            'timestamp': datetime.now().isoformat()
        }
        
        # Generate insights from current data
        self._generate_autonomous_insights()
        
        # Update exploration state
        self.exploration_state['total_discoveries'] = self.get_total_entities()
        self.exploration_state['last_update'] = time.time()
        
        exploration_results['insights_generated'] = len(self.autonomous_insights)
        
        return exploration_results
    
    def _generate_autonomous_insights(self):
        """Generate insights autonomously"""
        try:
            # Financial insights
            financial_data = self.data_universe.get('financial', {})
            if financial_data:
                # Find big price movers
                big_movers = []
                for symbol, data in financial_data.items():
                    if isinstance(data, dict):
                        change = data.get('price_change_24h', 0)
                        if abs(change) > 10:  # >10% change
                            big_movers.append((symbol, change))
                
                if big_movers:
                    self.autonomous_insights.append({
                        'type': 'market_movement',
                        'description': f"Detected {len(big_movers)} cryptocurrencies with >10% price movement",
                        'details': big_movers[:5],  # Top 5
                        'timestamp': datetime.now().isoformat()
                    })
            
            # Cross-domain insights
            domains = list(self.data_universe.keys())
            if len(domains) > 1:
                self.autonomous_insights.append({
                    'type': 'cross_domain_analysis',
                    'description': f"Universe spans {len(domains)} domains: {', '.join(domains)}",
                    'entity_count': self.get_total_entities(),
                    'timestamp': datetime.now().isoformat()
                })
        
        except Exception as e:
            print(f"Insight generation error: {e}")
    
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
                # Search in entity name
                if search_lower in entity.lower():
                    domain_matches.append({
                        'entity': entity,
                        'match_type': 'name',
                        'details': details
                    })
                # Search in entity details
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

# Initialize explorer when module is imported
if __name__ == "__main__":
    explorer = UniverseDataExplorer()
    print(f"🌌 Universe initialized with {explorer.get_total_entities()} entities")
