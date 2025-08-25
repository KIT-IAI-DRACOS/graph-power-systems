# Graph Neural Networks in Power Systems - Research Blog

This is a Jekyll-based research blog that serves as a companion to our comprehensive review paper on Graph Neural Networks in Power Systems.

## Overview

The blog provides:
- **Research Updates**: Latest developments in GNN applications for power systems
- **Technical Deep Dives**: Detailed explanations of key concepts and methodologies
- **Case Studies**: Real-world applications and success stories
- **Future Directions**: Emerging trends and open research questions

## Getting Started

### Prerequisites

- Ruby (version 2.4.0 or higher)
- RubyGems
- GCC and Make

### Installation

1. **Install Jekyll and Bundler**:
   ```bash
   gem install jekyll bundler
   ```

2. **Install dependencies**:
   ```bash
   bundle install
   ```

3. **Serve the blog locally**:
   ```bash
   bundle exec jekyll serve
   ```

4. **View your blog**: Open [http://localhost:4000](http://localhost:4000) in your browser

## Blog Structure

```
gnn-review/
├── _config.yml          # Jekyll configuration
├── _posts/              # Blog posts (markdown files)
├── _layouts/            # HTML layouts (inherited from minima theme)
├── _includes/           # Reusable HTML components
├── assets/              # CSS, JavaScript, images
├── index.markdown       # Home page
├── about.markdown       # About page
└── README.md            # This file
```

## Creating New Blog Posts

### Post Format

Create new posts in the `_posts/` directory with the naming convention:
```
YYYY-MM-DD-title.markdown
```

### Post Front Matter

Each post should include front matter at the top:

```markdown
---
layout: post
title: "Your Post Title"
date: YYYY-MM-DD HH:MM:SS +0000
categories: category1 category2
---

# Your Post Content

Your markdown content goes here...
```

### Post Categories

Use relevant categories for your posts:
- `gnn` - General GNN topics
- `power-systems` - Power system applications
- `power-flow` - Power flow analysis
- `fault-detection` - Fault detection and security
- `optimization` - Grid optimization
- `renewables` - Renewable energy integration
- `research` - Research updates and papers
- `tutorial` - How-to guides and code examples

## Customization

### Theme

The blog uses the `minima` theme. You can customize it by:

1. **Overriding theme files**: Create files in `_layouts/`, `_includes/`, or `assets/`
2. **Modifying CSS**: Add custom styles in `assets/css/`
3. **Custom layouts**: Create new layout files in `_layouts/`

### Configuration

Edit `_config.yml` to customize:
- Site title and description
- Author information
- Social media links
- Build settings
- Plugins

### Adding Features

Common additions include:
- **Comments**: Disqus, Giscus, or custom solution
- **Analytics**: Google Analytics, Plausible, etc.
- **Search**: Algolia, Lunr.js, or custom search
- **Newsletter**: Mailchimp, ConvertKit, etc.

## Deployment

### GitHub Pages

1. Push your blog to a GitHub repository
2. Enable GitHub Pages in repository settings
3. Set source to main branch or gh-pages branch

### Netlify

1. Connect your GitHub repository to Netlify
2. Build command: `bundle exec jekyll build`
3. Publish directory: `_site`

### Vercel

1. Import your GitHub repository to Vercel
2. Build command: `bundle exec jekyll build`
3. Output directory: `_site`

## Content Guidelines

### Writing Style

- **Clear and concise**: Explain complex concepts simply
- **Technical depth**: Provide sufficient detail for researchers
- **Code examples**: Include practical implementations
- **Visuals**: Use diagrams, charts, and code snippets
- **Citations**: Reference relevant papers and sources

### Post Types

1. **Research Updates**: New papers, breakthroughs, conferences
2. **Technical Deep Dives**: Detailed methodology explanations
3. **Case Studies**: Real-world applications and results
4. **Tutorials**: Step-by-step guides and code walkthroughs
5. **Future Perspectives**: Emerging trends and open questions

### Code Examples

- Use syntax highlighting for code blocks
- Include complete, runnable examples
- Explain key concepts in comments
- Link to full implementations when possible

## Maintenance

### Regular Tasks

- **Update dependencies**: Run `bundle update` periodically
- **Review content**: Ensure posts remain accurate and relevant
- **Monitor performance**: Check site speed and analytics
- **Backup**: Keep backups of your content and configuration

### Content Updates

- **Add new posts**: Regular posting schedule (weekly/bi-weekly)
- **Update existing posts**: Fix errors, add new information
- **Archive old content**: Organize and categorize posts
- **Cross-linking**: Connect related posts and topics

## Support

### Jekyll Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Jekyll Themes](https://jekyllthemes.io/)
- [Jekyll Talk](https://talk.jekyllrb.com/)

### Markdown Resources

- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Markdown](https://docs.github.com/en/github/writing-on-github)

### Power Systems Resources

- [IEEE Power & Energy Society](https://www.ieee-pes.org/)
- [CIGRE](https://www.cigre.org/)
- [Power Systems Research Journals](https://www.ieee-pes.org/publications)

## Contributing

We welcome contributions to improve the blog:

1. **Content suggestions**: New topics and post ideas
2. **Technical improvements**: Code examples and implementations
3. **Design enhancements**: UI/UX improvements
4. **Documentation**: Better guides and tutorials

## License

[Add your license information here]

---

*This blog accompanies our academic review paper on Graph Neural Networks in Power Systems. For detailed technical content and comprehensive literature review, please refer to the published paper.*
