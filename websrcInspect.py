from bs4 import BeautifulSoup
import re

class WebStructureAnalyzer:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')
        self.findings = {
            'name': [],
            'price': [],
            'rating': [],
            'reviews': []
        }
        
    def analyze(self):
        self._detect_names()
        self._detect_prices()
        self._detect_ratings()
        self._detect_reviews()
        return self.findings
    
    def _detect_names(self):
        candidates = []
        for tag in self.soup.find_all(['h1', 'h2', 'h3', 'div', 'span', 'meta']):
            text = self._get_element_text(tag)
            attributes = tag.attrs
            
            score = 0
            if tag.name in ['h1', 'h2', 'h3']:
                score += 2
            if 'itemprop' in attributes and 'name' in attributes['itemprop']:
                score += 3
            if 'class' in attributes and any(re.search(r'title|name|heading', c, re.I) for c in attributes['class']):
                score += 2
            if 10 < len(text) < 120:
                score += 1
                
            if score > 3:
                candidates.append(self._create_candidate(tag, text, score))
        
        self.findings['name'] = sorted(candidates, key=lambda x: x['confidence'], reverse=True)

    def _detect_prices(self):
        price_pattern = re.compile(r'\$?\d{1,3}(?:,\d{3})*(?:\.\d{2})?')
        candidates = []
        
        for tag in self.soup.find_all(['span', 'div', 'meta', 'p', 'b']):
            text = self._get_element_text(tag)
            attributes = tag.attrs
            
            score = 0
            if price_pattern.search(text):
                score += 3
            if 'itemprop' in attributes and 'price' in attributes['itemprop']:
                score += 3
            if 'class' in attributes and any(re.search(r'price|cost|amount', c, re.I) for c in attributes['class']):
                score += 2
                
            if score > 2:
                candidates.append(self._create_candidate(tag, text, score))
        
        self.findings['price'] = sorted(candidates, key=lambda x: x['confidence'], reverse=True)

    def _detect_ratings(self):
        rating_pattern = re.compile(r'\d\.?\d? out of \d|[\d.]+/[\d.]+')
        candidates = []
        
        for tag in self.soup.find_all(['div', 'span', 'meta', 'section']):
            text = self._get_element_text(tag)
            attributes = tag.attrs
            
            score = 0
            if rating_pattern.search(text):
                score += 3
            if 'itemprop' in attributes and 'ratingValue' in attributes['itemprop']:
                score += 3
            if 'class' in attributes and any(re.search(r'rating|star|review', c, re.I) for c in attributes['class']):
                score += 2
                
            if score > 2:
                candidates.append(self._create_candidate(tag, text, score))
        
        self.findings['rating'] = sorted(candidates, key=lambda x: x['confidence'], reverse=True)

    def _detect_reviews(self):
        review_pattern = re.compile(r'\d+ (?:reviews|ratings)')
        candidates = []
        
        for tag in self.soup.find_all(['div', 'span', 'a', 'section']):
            text = self._get_element_text(tag)
            attributes = tag.attrs
            
            score = 0
            if review_pattern.search(text):
                score += 3
            if 'itemprop' in attributes and 'reviewCount' in attributes['itemprop']:
                score += 3
            if 'class' in attributes and any(re.search(r'review|comment|feedback', c, re.I) for c in attributes['class']):
                score += 2
                
            if score > 2:
                candidates.append(self._create_candidate(tag, text, score))
        
        self.findings['reviews'] = sorted(candidates, key=lambda x: x['confidence'], reverse=True)

    def _create_candidate(self, tag, text, score):
        return {
            'element': tag.name,
            'attrs': tag.attrs,
            'text': text,
            'selector': self._generate_selector(tag),
            'confidence': min(score, 5)
        }

    def _generate_selector(self, tag):
        if tag.get('id'):
            return f"{tag.name}#{tag['id']}"
        classes = tag.get('class', [])
        if classes:
            return f"{tag.name}.{'.'.join(classes)}"
        return tag.name

    def _get_element_text(self, tag):
        if tag.name == 'meta':
            return tag.get('content', '')
        return tag.get_text(strip=True)

def analyze_website(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            analyzer = WebStructureAnalyzer(f.read())
            return analyzer.analyze()
    except Exception as e:
        print(f"Error analyzing website: {str(e)}")
        return None

def print_recommendations(results):
    for category, candidates in results.items():
        print(f"\n=== {category.upper()} CANDIDATES ===")
        if not candidates:
            print("No candidates found")
            continue
            
        for candidate in candidates:
            print(f"Tag: {candidate['element'].upper()}")
            print(f"Selector: {candidate['selector']}")
            print(f"Sample: {candidate['text'][:50]}{'...' if len(candidate['text']) >50 else ''}")
            print(f"Confidence: {'★' * candidate['confidence']}")
            print("-" * 60)

# Usage
if __name__ == "__main__":
    file_path = r'F:\DS\web scraping\demo.html'  # Update with your file path
    analysis = analyze_website(file_path)
    
    if analysis:
        print_recommendations(analysis)
    else:
        print("Failed to analyze the website structure")