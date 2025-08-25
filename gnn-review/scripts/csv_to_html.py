#!/usr/bin/env python3
"""
Script to convert the public_papers.csv file directly to HTML
This eliminates the need for Jekyll plugins and works reliably on GitHub Pages
"""

import csv
import os
from pathlib import Path

def csv_to_html(csv_file, output_file):
    """Convert CSV to HTML table with proper styling."""
    
    # Read CSV data
    papers = []
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            papers.append(row)
    
    # Generate HTML
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Papers - DRACOS GNN Review</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f8f9fa;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 0.5rem;
            margin-bottom: 2rem;
        }}
        .construction-banner {{
            background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
            border: 2px solid #ffc107;
            border-radius: 8px;
            padding: 1.5rem;
            margin: 2rem 0;
            text-align: center;
            box-shadow: 0 2px 8px rgba(255, 193, 7, 0.2);
        }}
        .construction-banner p {{
            margin: 0.5rem 0;
            color: #856404;
        }}
        .construction-banner p:first-child {{
            font-size: 1.1rem;
            font-weight: 600;
        }}
        .stats {{
            background: #e9ecef;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }}
        .stats p {{
            margin: 0.5rem 0;
            font-weight: 500;
        }}
        .papers-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 2rem 0;
            background: white;
        }}
        .papers-table th {{
            background: #f8f9fa;
            padding: 12px;
            text-align: left;
            border-bottom: 2px solid #dee2e6;
            font-weight: 600;
            color: #495057;
        }}
        .papers-table td {{
            padding: 12px;
            border-bottom: 1px solid #dee2e6;
            vertical-align: top;
        }}
        .papers-table tr:hover {{
            background-color: #f8f9fa;
        }}
        .category-tag {{
            display: inline-block;
            background: #e9ecef;
            color: #495057;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.8rem;
            margin: 2px;
        }}
        .search-container {{
            margin: 1rem 0;
        }}
        .search-input {{
            width: 100%;
            padding: 12px;
            border: 1px solid #dee2e6;
            border-radius: 4px;
            font-size: 1rem;
            margin-bottom: 1rem;
        }}
        .filter-container {{
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
            flex-wrap: wrap;
        }}
        .filter-group {{
            flex: 1;
            min-width: 200px;
        }}
        .filter-group label {{
            display: block;
            margin: 0.5rem 0;
            cursor: pointer;
        }}
        .filter-group input[type="checkbox"] {{
            margin-right: 0.5rem;
        }}
        @media (max-width: 768px) {{
            .container {{
                padding: 1rem;
            }}
            .papers-table {{
                font-size: 0.9rem;
            }}
            .papers-table th,
            .papers-table td {{
                padding: 8px 4px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>All Papers - DRACOS GNN Review</h1>
        
        <div class="construction-banner">
            <p><strong>🚧 Companion Web Page Under Construction</strong></p>
            <p>This page is being developed to accompany our research review. Features and content may be updated as development continues.</p>
        </div>
        
        <p>This page contains all papers from our DRACOS GNN study, focusing on Graph Neural Networks applications in power systems. The papers are presented with their titles, authors, publication year, and citation counts.</p>
        
        <div class="stats">
            <p><strong>Total Papers:</strong> {len(papers)}</p>
            <p><strong>Years Covered:</strong> {min(int(p['Year']) for p in papers if p['Year'].isdigit()) if papers else 'N/A'} - {max(int(p['Year']) for p in papers if p['Year'].isdigit()) if papers else 'N/A'}</p>
            <p><strong>Total Citations:</strong> {sum(int(p['Citations']) for p in papers if p['Citations'].isdigit()) if papers else 0}</p>
        </div>
        
        <div class="search-container">
            <input type="text" id="searchInput" class="search-input" placeholder="Search papers by title or authors...">
        </div>
        
        <div class="filter-container">
            <div class="filter-group">
                <h4>Filter by Year</h4>
                <label><input type="checkbox" class="year-filter" value="all" checked> All Years</label>
                {chr(10).join(f'<label><input type="checkbox" class="year-filter" value="{year}" checked> {year}</label>' for year in sorted(set(p['Year'] for p in papers if p['Year'].isdigit()), reverse=True))}
            </div>
            <div class="filter-group">
                <h4>Filter by Category</h4>
                <label><input type="checkbox" class="category-filter" value="all" checked> All Categories</label>
                {chr(10).join(f'<label><input type="checkbox" class="category-filter" value="{category}" checked> {category}</label>' for category in sorted(set(cat.strip() for p in papers for cat in p['Categories'].split(';') if cat.strip())))}
            </div>
        </div>
        
        <table class="papers-table" id="papersTable">
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Authors</th>
                    <th>Year</th>
                    <th>Citations</th>
                    <th>Categories</th>
                </tr>
            </thead>
            <tbody>
"""
    
    # Add table rows
    for paper in papers:
        categories_html = ''.join(f'<span class="category-tag">{cat.strip()}</span>' for cat in paper['Categories'].split(';') if cat.strip())
        html_content += f"""                <tr class="paper-row" data-year="{paper['Year']}" data-title="{paper['Title'].lower()}" data-authors="{paper['Authors'].lower()}" data-categories="{paper['Categories'].lower()}">
                    <td>{paper['Title']}</td>
                    <td>{paper['Authors']}</td>
                    <td>{paper['Year']}</td>
                    <td>{paper['Citations']}</td>
                    <td>{categories_html}</td>
                </tr>
"""
    
    # Close HTML
    html_content += """            </tbody>
        </table>
        
        <div class="stats">
            <p><em>Showing {len(papers)} papers from our comprehensive review. Use the search and filters above to find specific research areas.</em></p>
        </div>
    </div>
    
    <script>
        // Search and filtering functionality
        document.addEventListener('DOMContentLoaded', function() {
            const searchInput = document.getElementById('searchInput');
            const yearFilters = document.querySelectorAll('.year-filter');
            const categoryFilters = document.querySelectorAll('.category-filter');
            const paperRows = document.querySelectorAll('.paper-row');
            
            function updateVisibility() {
                const searchTerm = searchInput.value.toLowerCase();
                const selectedYears = Array.from(yearFilters).filter(f => f.checked).map(f => f.value);
                const selectedCategories = Array.from(categoryFilters).filter(f => f.checked).map(f => f.value);
                
                let visibleCount = 0;
                
                paperRows.forEach(row => {
                    const year = row.dataset.year;
                    const title = row.dataset.title;
                    const authors = row.dataset.authors;
                    const categories = row.dataset.categories;
                    
                    const matchesYear = selectedYears.includes('all') || selectedYears.includes(year);
                    const matchesCategory = selectedCategories.includes('all') || 
                                         selectedCategories.some(cat => categories.includes(cat.toLowerCase()));
                    const matchesSearch = searchTerm === '' || 
                                        title.includes(searchTerm) || 
                                        authors.includes(searchTerm);
                    
                    if (matchesYear && matchesCategory && matchesSearch) {
                        row.style.display = '';
                        visibleCount++;
                    } else {
                        row.style.display = 'none';
                    }
                });
                
                // Update stats
                const statsDiv = document.querySelector('.stats p:last-child');
                if (statsDiv) {
                    statsDiv.innerHTML = `<em>Showing ${visibleCount} of ${paperRows.length} papers. Use the search and filters above to find specific research areas.</em>`;
                }
            }
            
            // Event listeners
            searchInput.addEventListener('input', updateVisibility);
            yearFilters.forEach(filter => filter.addEventListener('change', updateVisibility));
            categoryFilters.forEach(filter => filter.addEventListener('change', updateVisibility));
            
            // Initialize
            updateVisibility();
        });
    </script>
</body>
</html>"""
    
    # Write HTML file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)
    
    print(f"✓ Successfully converted CSV to HTML: {output_file}")
    print(f"  Contains {len(papers)} papers")
    return len(papers)

def main():
    """Main function."""
    script_dir = Path(__file__).parent.parent
    csv_file = script_dir / "data" / "public_papers.csv"
    html_file = script_dir / "all-papers.html"
    
    if not csv_file.exists():
        print(f"Error: CSV file not found at {csv_file}")
        print("Please run the update_public_papers.py script first to generate the CSV file.")
        return
    
    print("Converting CSV to HTML...")
    paper_count = csv_to_html(csv_file, html_file)
    
    print(f"\n✓ Conversion complete!")
    print(f"  HTML file: {html_file}")
    print(f"  Papers included: {paper_count}")
    print(f"  Features: Search, Year filtering, Category filtering")
    print(f"  No Jekyll plugins required - works directly on GitHub Pages!")

if __name__ == "__main__":
    main()
