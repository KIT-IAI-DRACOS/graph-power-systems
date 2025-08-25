require 'csv'

module Jekyll
  class PapersGenerator < Generator
    safe true
    priority :normal

    def generate(site)
      # Read the public CSV file
      csv_file = File.join(site.source, 'data', 'public_papers.csv')
      
      if File.exist?(csv_file)
        papers = CSV.read(csv_file, headers: true)
        
        # Convert to array of hashes for easier use in templates
        papers_data = papers.map do |row|
          {
            'title' => row['Title'],
            'authors' => row['Authors'],
            'year' => row['Year'],
            'citations' => row['Citations'],
            'categories' => row['Categories']
          }
        end
        
        # Make papers data available to all pages
        site.data['papers'] = papers_data
        
        # Sort papers by year (newest first) and then by citations (highest first)
        sorted_papers = papers_data.sort_by { |paper| [-paper['year'].to_i, -paper['citations'].to_i] }
        site.data['papers_sorted'] = sorted_papers
        
        # Group papers by year
        papers_by_year = sorted_papers.group_by { |paper| paper['year'] }
        site.data['papers_by_year'] = papers_by_year
        
        # Extract all unique categories and group papers by category
        all_categories = []
        papers_by_category = {}
        
        papers_data.each do |paper|
          if paper['categories']
            # Split categories by semicolon and clean them
            paper_categories = paper['categories'].split(';').map(&:strip)
            paper_categories.each do |category|
              if category && !category.empty?
                all_categories << category
                papers_by_category[category] ||= []
                papers_by_category[category] << paper
              end
            end
          end
        end
        
        # Remove duplicates and sort categories
        site.data['all_categories'] = all_categories.uniq.sort
        site.data['papers_by_category'] = papers_by_category
        
        # Create a mapping of papers to their categories for filtering
        papers_with_categories = papers_data.map do |paper|
          if paper['categories']
            paper_categories = paper['categories'].split(';').map(&:strip)
            paper['category_list'] = paper_categories
          else
            paper['category_list'] = ['General']
          end
          paper
        end
        site.data['papers_with_categories'] = papers_with_categories
      end
    end
  end
end
