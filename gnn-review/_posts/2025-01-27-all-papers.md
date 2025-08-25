---
layout: post
title: "All Papers - DRACOS GNN Review"
date: 2025-01-27 12:00:00 +0100
categories: papers review gnn
---

# All Papers - DRACOS GNN Review

<div class="construction-banner">
  <p><strong>🚧 Companion Web Page Under Construction</strong></p>
  <p>This page is being developed to accompany our research review. Features and content may be updated as development continues.</p>
  <p><em>Note: Papers data will be displayed once the CSV file is properly loaded.</em></p>
</div>

This page contains all papers from our DRACOS GNN study, focusing on Graph Neural Networks applications in power systems. The papers are presented with their titles, authors, publication year, and citation counts.

<div class="papers-container">
  <div class="sidebar">
    <h3>Filter by Year</h3>
    <div class="year-filters">
      <label><input type="checkbox" class="year-filter" value="all" checked> All Years</label>
      {% if site.data.papers_by_year and site.data.papers_by_year.keys.size > 0 %}
        {% for year in site.data.papers_by_year %}
        <label><input type="checkbox" class="year-filter" value="{{ year[0] }}" checked> {{ year[0] }}</label>
        {% endfor %}
      {% endif %}
    </div>
    
    <h3>Filter by Category</h3>
    <div class="category-filters">
      <label><input type="checkbox" class="category-filter" value="all" checked> All Categories</label>
      {% if site.data.all_categories and site.data.all_categories.size > 0 %}
        {% for category in site.data.all_categories %}
        <label><input type="checkbox" class="category-filter" value="{{ category }}" checked> {{ category }}</label>
        {% endfor %}
      {% endif %}
    </div>
    
    <h3>Quick Stats</h3>
    <div class="stats">
      <p><strong>Total Papers:</strong> {{ site.data.papers.size | default: 0 }}</p>
      <p><strong>Years Covered:</strong> 
        {% if site.data.papers_by_year and site.data.papers_by_year.keys.size > 0 %}
          {{ site.data.papers_by_year.keys.min }} - {{ site.data.papers_by_year.keys.max }}
        {% else %}
          N/A
        {% endif %}
      </p>
      <p><strong>Categories:</strong> {{ site.data.all_categories.size | default: 0 }}</p>
      <p><strong>Total Citations:</strong> 
        {% if site.data.papers and site.data.papers.size > 0 %}
          {{ site.data.papers | map: 'citations' | map: 'to_i' | sum }}
        {% else %}
          0
        {% endif %}
      </p>
      <p><strong>Avg Citations:</strong> 
        {% if site.data.papers and site.data.papers.size > 0 %}
          {{ site.data.papers | map: 'citations' | map: 'to_i' | sum | divided_by: site.data.papers.size | round: 1 }}
        {% else %}
          0
        {% endif %}
      </p>
    </div>
  </div>

  <div class="main-content">
    <h2>Papers Overview</h2>
    
    <div class="search-container">
      <input type="text" id="searchInput" placeholder="Search papers by title or authors..." class="search-input">
      <div class="search-stats">
        <span id="visibleCount">{{ site.data.papers.size | default: 0 }}</span> of {{ site.data.papers.size | default: 0 }} papers shown
      </div>
    </div>
    
    <div class="papers-table-container">
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
          {% if site.data.papers_with_categories and site.data.papers_with_categories.size > 0 %}
            {% for paper in site.data.papers_with_categories %}
            <tr class="paper-row" data-year="{{ paper.year }}" data-title="{{ paper.title | downcase }}" data-authors="{{ paper.authors | downcase }}" data-categories="{{ paper.category_list | join: ' ' | downcase }}">
              <td>{{ paper.title }}</td>
              <td>{{ paper.authors }}</td>
              <td>{{ paper.year }}</td>
              <td>{{ paper.citations }}</td>
              <td>
                {% for category in paper.category_list %}
                <span class="category-tag">{{ category }}</span>
                {% endfor %}
              </td>
            </tr>
            {% endfor %}
          {% else %}
            <tr>
              <td colspan="5" style="text-align: center; padding: 2rem; color: #6c757d;">
                <em>Papers data is being loaded...</em>
              </td>
            </tr>
          {% endif %}
        </tbody>
      </table>
    </div>

    <h2>Papers by Category</h2>
    {% if site.data.all_categories and site.data.all_categories.size > 0 %}
      {% for category in site.data.all_categories %}
      <div class="category-section" data-category="{{ category }}">
        <h3>{{ category }}</h3>
        <p class="category-stats">{{ site.data.papers_by_category[category].size }} papers</p>
        {% for paper in site.data.papers_by_category[category] %}
        <div class="paper-item">
          <h4>{{ paper.title }}</h4>
          <p><strong>Authors:</strong> {{ paper.authors }}</p>
          <p><strong>Year:</strong> {{ paper.year }}</p>
          <p><strong>Citations:</strong> {{ paper.citations }}</p>
          <p><strong>Categories:</strong> 
            {% for cat in paper.category_list %}
            <span class="category-tag">{{ cat }}</span>
            {% endfor %}
          </p>
        </div>
        {% endfor %}
      </div>
      {% endfor %}
    {% else %}
      <div class="category-section">
        <h3>Categories</h3>
        <p class="category-stats">Categories are being loaded...</p>
      </div>
    {% endif %}

    <h2>Interactive Visualizations</h2>
    <div class="charts-container">
      <div class="chart-row">
        <div class="chart-card">
          <h3>Papers by Category</h3>
          <canvas id="categoryChart" width="400" height="300"></canvas>
        </div>
        <div class="chart-card">
          <h3>Papers by Year</h3>
          <canvas id="yearChart" width="400" height="300"></canvas>
        </div>
      </div>
      <div class="chart-row">
        <div class="chart-card">
          <h3>Citations by Category</h3>
          <canvas id="citationsChart" width="400" height="300"></canvas>
        </div>
        <div class="chart-card">
          <h3>Citations Over Time</h3>
          <canvas id="citationsOverTimeChart" width="400" height="300"></canvas>
        </div>
      </div>
    </div>

    <h2>Papers by Year</h2>
    {% if site.data.papers_by_year and site.data.papers_by_year.keys.size > 0 %}
      {% for year in site.data.papers_by_year %}
      <div class="year-section" data-year="{{ year[0] }}">
        <h3>{{ year[0] }}</h3>
        {% for paper in year[1] %}
        <div class="paper-item">
          <h4>{{ paper.title }}</h4>
          <p><strong>Authors:</strong> {{ paper.authors }}</p>
          <p><strong>Citations:</strong> {{ paper.citations }}</p>
          <p><strong>Categories:</strong> 
            {% for cat in paper.category_list %}
            <span class="category-tag">{{ cat }}</span>
            {% endfor %}
          </p>
        </div>
        {% endfor %}
      </div>
      {% endfor %}
    {% else %}
      <div class="year-section">
        <h3>Years</h3>
        <p>Papers by year are being loaded...</p>
      </div>
    {% endif %}
  </div>
</div>

<style>
.papers-container {
  display: flex;
  gap: 2rem;
  margin-top: 2rem;
}

.construction-banner {
  background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
  border: 2px solid #ffc107;
  border-radius: 8px;
  padding: 1.5rem;
  margin: 1.5rem 0;
  text-align: center;
  box-shadow: 0 2px 8px rgba(255, 193, 7, 0.2);
}

.construction-banner p {
  margin: 0.5rem 0;
  color: #856404;
}

.construction-banner p:first-child {
  font-size: 1.1rem;
  font-weight: 600;
}

.construction-banner p:last-child {
  font-size: 0.9rem;
  opacity: 0.8;
}

.sidebar {
  flex: 0 0 300px;
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  height: fit-content;
  position: sticky;
  top: 2rem;
}

.main-content {
  flex: 1;
}

.year-filters label {
  display: block;
  margin: 0.5rem 0;
  cursor: pointer;
}

.year-filters input[type="checkbox"] {
  margin-right: 0.5rem;
}

.category-filters {
  max-height: 200px;
  overflow-y: auto;
  border: 1px solid #dee2e6;
  border-radius: 4px;
  padding: 0.5rem;
  background: white;
}

.category-filters label {
  display: block;
  margin: 0.5rem 0;
  cursor: pointer;
  font-size: 0.9rem;
}

.category-filters input[type="checkbox"] {
  margin-right: 0.5rem;
}

.category-filters::-webkit-scrollbar {
  width: 6px;
}

.category-filters::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 3px;
}

.category-filters::-webkit-scrollbar-thumb {
  background: #c1c1c1;
  border-radius: 3px;
}

.category-filters::-webkit-scrollbar-thumb:hover {
  background: #a8a8a8;
}

.stats p {
  margin: 0.5rem 0;
  font-size: 0.9rem;
}

.search-container {
  margin-bottom: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

.search-input {
  flex: 1;
  min-width: 300px;
  padding: 0.75rem;
  border: 1px solid #dee2e6;
  border-radius: 4px;
  font-size: 1rem;
}

.search-stats {
  font-size: 0.9rem;
  color: #6c757d;
  white-space: nowrap;
}

.papers-table-container {
  overflow-x: auto;
  margin-bottom: 2rem;
}

.papers-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1rem;
}

.papers-table th,
.papers-table td {
  padding: 0.75rem;
  text-align: left;
  border-bottom: 1px solid #dee2e6;
}

.papers-table th {
  background-color: #f8f9fa;
  font-weight: 600;
}

.paper-row.hidden {
  display: none;
}

.category-tag {
  display: inline-block;
  background-color: #e9ecef;
  color: #495057;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.8rem;
  margin-right: 0.5rem;
  margin-bottom: 0.5rem;
}

.category-section {
  margin-bottom: 2rem;
  padding: 1rem;
  border: 1px solid #dee2e6;
  border-radius: 8px;
}

.category-section h3 {
  margin-top: 0;
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

.category-stats {
  margin-bottom: 1rem;
  font-size: 0.9rem;
  color: #6c757d;
  font-style: italic;
}

.year-section {
  margin-bottom: 2rem;
  padding: 1rem;
  border: 1px solid #dee2e6;
  border-radius: 8px;
}

.charts-container {
  margin: 2rem 0;
}

.chart-row {
  display: flex;
  gap: 2rem;
  margin-bottom: 2rem;
}

.chart-card {
  flex: 1;
  background: white;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.chart-card h3 {
  margin-top: 0;
  margin-bottom: 1rem;
  color: #2c3e50;
  text-align: center;
  font-size: 1.1rem;
}

.chart-card canvas {
  max-width: 100%;
  height: auto;
}

.paper-item {
  margin-bottom: 1rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 4px;
}

.paper-item h4 {
  margin: 0 0 0.5rem 0;
  color: #2c3e50;
}

.paper-item p {
  margin: 0.25rem 0;
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .papers-container {
    flex-direction: column;
  }
  
  .sidebar {
    position: static;
    flex: none;
  }

  .chart-row {
    flex-direction: column;
  }
  
  .chart-card {
    margin-bottom: 1rem;
  }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const yearFilters = document.querySelectorAll('.year-filter');
  const categoryFilters = document.querySelectorAll('.category-filter');
  const paperRows = document.querySelectorAll('.paper-row');
  const categorySections = document.querySelectorAll('.category-section');
  const yearSections = document.querySelectorAll('.year-section');
  const searchInput = document.getElementById('searchInput');
  const visibleCountSpan = document.getElementById('visibleCount');
  
  function updateVisibility() {
    const selectedYears = Array.from(yearFilters)
      .filter(filter => filter.checked)
      .map(filter => filter.value);
    
    const selectedCategories = Array.from(categoryFilters)
      .filter(filter => filter.checked)
      .map(filter => filter.value);

    // Show/hide table rows
    paperRows.forEach(row => {
      const year = row.dataset.year;
      const title = row.dataset.title;
      const authors = row.dataset.authors;
      const categories = row.dataset.categories;

      const matchesYear = selectedYears.includes('all') || selectedYears.includes(year);
      const matchesCategory = selectedCategories.includes('all') || 
                             selectedCategories.some(cat => categories.includes(cat.toLowerCase()));
      const matchesSearch = searchInput.value === '' ||
                            title.includes(searchInput.value.toLowerCase()) ||
                            authors.includes(searchInput.value.toLowerCase());

      if (matchesYear && matchesCategory && matchesSearch) {
        row.classList.remove('hidden');
      } else {
        row.classList.add('hidden');
      }
    });
    
    // Show/hide category sections
    categorySections.forEach(section => {
      const category = section.dataset.category;
      const matchesCategory = selectedCategories.includes('all') || selectedCategories.includes(category);
      const matchesSearch = searchInput.value === '' ||
                            section.querySelector('h3').textContent.toLowerCase().includes(searchInput.value.toLowerCase());

      if (matchesCategory && matchesSearch) {
        section.style.display = 'block';
      } else {
        section.style.display = 'none';
      }
    });

    // Show/hide year sections
    yearSections.forEach(section => {
      const year = section.dataset.year;
      const matchesYear = selectedYears.includes('all') || selectedYears.includes(year);
      const matchesSearch = searchInput.value === '' ||
                            section.querySelector('h3').textContent.toLowerCase().includes(searchInput.value.toLowerCase());

      if (matchesYear && matchesSearch) {
        section.style.display = 'block';
      } else {
        section.style.display = 'none';
      }
    });

    visibleCountSpan.textContent = document.querySelectorAll('.paper-row:not(.hidden)').length;
  }
  
  // Add event listeners to checkboxes
  yearFilters.forEach(filter => {
    filter.addEventListener('change', updateVisibility);
  });

  categoryFilters.forEach(filter => {
    filter.addEventListener('change', updateVisibility);
  });

  // Add event listener for search input
  searchInput.addEventListener('input', updateVisibility);
  
  // Initialize visibility
  updateVisibility();
});
</script>

## Research Areas Covered

Our review encompasses various applications of GNNs in power systems, including:

- **Power Flow Analysis** - Computational efficiency and accuracy improvements
- **Fault Detection and Diagnosis** - Pattern recognition in distribution networks
- **Grid Stability Assessment** - Reliability and stability analysis
- **Load Forecasting** - Temporal and spatial demand prediction
- **Network Optimization** - Grid efficiency and loss reduction
- **Security and Anomaly Detection** - Threat identification and response
- **Renewable Energy Integration** - Smart grid and sustainability applications

## Methodology Notes

- **Citation Counts**: Based on Google Scholar and Web of Science data as of January 2025
- **Coverage**: Comprehensive review of peer-reviewed publications
- **Focus**: Graph Neural Networks specifically applied to power systems
- **Data Source**: Curated selection from our research database

## Data Privacy

This page presents all papers from our comprehensive review with publicly available information. Only the essential metadata (title, authors, year, citations) is displayed to maintain academic transparency while protecting detailed research notes and analysis.

---

*Last updated: January 2025*

*Note: This page automatically reads from the public_papers.csv file. All papers from your research database are included with only the specified fields displayed.*
