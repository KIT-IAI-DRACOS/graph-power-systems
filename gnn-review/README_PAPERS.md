# Papers Management System

This system automatically creates a public version of your research database, showing all papers but only the essential fields (title, authors, year, citations) for privacy protection.

## File Structure

- **`DRACOS_GNN.csv`** - Your private Zotero library export (keep this local, never commit to git)
- **`data/public_papers.csv`** - Public version with all papers but limited fields
- **`_plugins/csv_reader.rb`** - Jekyll plugin that reads the public CSV
- **`scripts/update_public_papers.py`** - Script to automatically create public CSV

## How It Works

1. **Private Data**: Your full `DRACOS_GNN.csv` stays local and private
2. **Automatic Processing**: Script reads all papers and extracts only safe fields
3. **Public Data**: All papers appear in `public_papers.csv` with limited information
4. **Blog Display**: Jekyll automatically reads the public CSV and displays papers

## Fields Displayed Publicly

- ✅ **Title** - Paper title
- ✅ **Authors** - Author names
- ✅ **Year** - Publication year
- ✅ **Citations** - Number of citations

## Fields Kept Private

- ❌ **Abstract** - Detailed paper summary
- ❌ **Keywords** - Research keywords
- ❌ **Notes** - Personal research notes
- ❌ **Tags** - Zotero tags
- ❌ **URLs** - Links to papers
- ❌ **DOI** - Digital object identifiers
- ❌ **File attachments** - PDFs and other files

## Setting Up

1. **Place your private CSV**: Put `DRACOS_GNN.csv` in the `gnn-review/` directory
2. **Run the update script**: 
   ```bash
   cd gnn-review
   python scripts/update_public_papers.py
   ```
3. **Automatic processing**: The script will process all papers automatically
4. **Review output**: Check the generated `data/public_papers.csv`

## Updating Papers

### Automatic Update (Recommended)
```bash
python scripts/update_public_papers.py
```

The script will:
- Read all papers from your private CSV
- Extract only the safe fields (title, authors, year, citations)
- Handle various citation field formats automatically
- Create a clean public CSV file

### Manual Edit (If Needed)
Edit `data/public_papers.csv` directly. The format is:
```csv
Title,Authors,Year,Citations
"Paper Title","Author 1, Author 2",2024,150
```

## Privacy Features

- ✅ **All papers public** - Complete transparency of your research scope
- ✅ **Limited fields** - Only essential metadata is shared
- ✅ **Automatic processing** - No manual selection needed
- ✅ **Citation extraction** - Automatically finds and formats citation counts
- ✅ **Field mapping** - Handles various CSV column names from Zotero

## Blog Integration

The blog automatically:
- Reads from `public_papers.csv`
- Displays all papers in organized tables
- Groups papers by year
- Shows citation statistics
- Updates when you regenerate the public CSV

## Security Notes

- **Never commit** `DRACOS_GNN.csv` to git
- **Keep** `DRACOS_GNN.csv` in your local directory only
- **Use** `.gitignore` to ensure private files stay private
- **Review** `public_papers.csv` before committing (though it's safe by design)

## Troubleshooting

### Script won't run
- Make sure Python 3 is installed
- Check that `DRACOS_GNN.csv` is in the right location
- Verify file permissions

### Blog not showing papers
- Check that `public_papers.csv` exists in `data/` folder
- Ensure the CSV format is correct
- Run `jekyll serve` to see changes

### Citation counts are 0
- The script tries multiple field names for citations
- Check your CSV column headers
- Common names: "Citations", "Citation Count", "Cited by", etc.

## Example Workflow

1. Export your Zotero library to `DRACOS_GNN.csv`
2. Run `python scripts/update_public_papers.py`
3. Script automatically processes all papers
4. Review the generated `public_papers.csv`
5. Commit and push your blog changes
6. Your blog shows all papers with only safe fields

## Citation Field Detection

The script automatically detects citation information from various field names:
- `Citations`, `citations`
- `Citation Count`, `citation_count`
- `Number of Citations`, `number_of_citations`
- `Cited by`, `cited_by`
- `Times Cited`, `times_cited`
- And many more variations

This ensures that citation data is properly extracted regardless of your Zotero export format.
