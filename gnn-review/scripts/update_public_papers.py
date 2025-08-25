#!/usr/bin/env python3
"""
Script to automatically create a public papers CSV file with all papers from
your private DRACOS_GNN.csv file, showing title, authors, year, citations, and categories.
"""

import csv
import os
import sys
import re
from pathlib import Path

def read_private_csv(private_csv_path):
    """Read the private CSV file and return the data."""
    papers = []
    try:
        with open(private_csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                papers.append(row)
        print(f"Successfully read {len(papers)} papers from {private_csv_path}")
        return papers
    except FileNotFoundError:
        print(f"Error: Could not find {private_csv_path}")
        return []
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []

def extract_citations(paper):
    """Extract citation count from various possible citation fields."""
    # Try different possible citation field names
    citation_fields = [
        'Citations', 'citations', 'Citation Count', 'citation_count',
        'Number of Citations', 'number_of_citations', 'Cited by', 'cited_by',
        'Times Cited', 'times_cited', 'Citation', 'citation'
    ]
    
    for field in citation_fields:
        if field in paper and paper[field]:
            try:
                # Try to convert to integer, handle various formats
                citation_text = str(paper[field]).strip()
                if citation_text.isdigit():
                    return int(citation_text)
                # Handle cases like "150+" or "150 citations"
                citation_text = citation_text.replace('+', '').replace(' citations', '').replace(' citation', '')
                if citation_text.isdigit():
                    return int(citation_text)
            except (ValueError, TypeError):
                continue
    
    # If no citations found, return 0
    return 0

def extract_categories(paper):
    """Extract categories from tags and other fields."""
    categories = []
    
    # Try different possible tag field names
    tag_fields = [
        'Tags', 'tags', 'Tag', 'tag', 'Keywords', 'keywords', 'Keyword', 'keyword'
    ]
    
    for field in tag_fields:
        if field in paper and paper[field]:
            tag_text = str(paper[field]).strip()
            if tag_text:
                # Split tags by common separators
                tags = re.split(r'[,;]|\s+', tag_text)
                for tag in tags:
                    tag = tag.strip()
                    if tag.startswith('#D') and len(tag) > 2:
                        # Extract category name from tag
                        category = tag[2:]  # Remove #D prefix
                        # Convert to readable format
                        category = category.replace('_', ' ').replace('-', ' ')
                        # Capitalize words
                        category = ' '.join(word.capitalize() for word in category.split())
                        if category not in categories:
                            categories.append(category)
    
    # If no categories found, add a default one
    if not categories:
        categories = ['General']
    
    return '; '.join(categories)

def create_public_csv(papers, output_path):
    """Create the public CSV file with all papers, showing selected fields including categories."""
    # Define the fields we want in the public version
    public_fields = ['Title', 'Authors', 'Year', 'Citations', 'Categories']
    
    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=public_fields)
            writer.writeheader()
            
            for paper in papers:
                # Extract title from various possible field names
                title = paper.get('Title', paper.get('title', paper.get('Titel', 'No title')))
                
                # Extract authors from various possible field names
                authors = paper.get('Authors', paper.get('authors', paper.get('Author', 'No authors')))
                
                # Extract year from various possible field names
                year = paper.get('Year', paper.get('year', paper.get('Publication Year', 'No year')))
                
                # Extract citations
                citations = extract_citations(paper)
                
                # Extract categories
                categories = extract_categories(paper)
                
                # Create public paper entry
                public_paper = {
                    'Title': title,
                    'Authors': authors,
                    'Year': year,
                    'Citations': citations,
                    'Categories': categories
                }
                writer.writerow(public_paper)
        
        print(f"\n✓ Successfully created public CSV at {output_path}")
        print(f"  Contains {len(papers)} papers")
        print(f"  Fields included: {', '.join(public_fields)}")
        
    except Exception as e:
        print(f"Error creating public CSV: {e}")

def main():
    """Main function to run the script."""
    print("Public Papers CSV Updater - All Papers with Categories")
    print("="*60)
    
    # Get paths
    script_dir = Path(__file__).parent.parent
    private_csv = script_dir / "DRACOS_GNN.csv"
    public_csv = script_dir / "data" / "public_papers.csv"
    
    # Check if private CSV exists
    if not private_csv.exists():
        print(f"Private CSV not found at: {private_csv}")
        print("Please make sure DRACOS_GNN.csv is in the gnn-review directory")
        return
    
    # Read private CSV
    papers = read_private_csv(private_csv)
    if not papers:
        return
    
    print(f"\nFound {len(papers)} papers. All papers will be included in the public version.")
    print("The following fields will be shown:")
    print("- Title")
    print("- Authors") 
    print("- Year")
    print("- Citations")
    print("- Categories (extracted from tags)")
    
    # Create public CSV with all papers
    create_public_csv(papers, public_csv)
    
    print("\n" + "="*60)
    print("UPDATE COMPLETE!")
    print("="*60)
    print(f"All {len(papers)} papers are now public with categories")
    print("Run 'jekyll serve' to see the changes on your blog")

if __name__ == "__main__":
    main()
