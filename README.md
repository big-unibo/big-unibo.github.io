# BIG Website

[![build](https://github.com/big-unibo/big-website/actions/workflows/build.yml/badge.svg)](https://github.com/big-unibo/big-website/actions/workflows/build.yml)

This is the website of our academic research group at the University of Bologna.

This website is powered by Jekyll and some Bootstrap, Bootwatch; it is inspired  by the [Allan Lab's website](https://www.allanlab.org/). 

## Installation

Main instructions are [here](https://jekyllrb.com/docs/installation/).

- Install Ruby
- Install Jekyll via ```gem install jekyll bundler```
- Either create a new website via ```jekyll new mywebsite``` or clone/fork it from someone else, e.g., ```git clone https://github.com/mpa139/allanlab.git```.
- ```cd``` to the new folder
- Run Jekyll via ```bundle exec jekyll serve --incremental```
  - ```bundle exec``` is needed only the first time
  - ```--incremental``` is for development, to regenerate the website after each edit
- The website is now available at [http://localhost:4000/]
- If you just need to build the website for production, run ```bundle exec jekyll build```
- The static pages are generated in the _site folder; thus, just copy/paste the content of the _site folder 
to the webserver
  - To deploy, the site must be *built*, not *served*!
  - CI is implemented through Travis to automatically build the website (takes 1-2 minutes)
  - On the webserver, the latest release must be pulled: just go to ```/var/www/html/big``` ang  ```git pull```

## Biblio plugin

Getting the Bibtex:

- Export Bibtexs from Scopus [see tutorial](https://libguides.usask.ca/c.php?g=218034&p=1445629#:~:text=Download%20BibTex%20format%20from%20Scopus,Select%20BibTex%2C%20and%20click%20Export.).
- Import in Mendeley and export to get rid of duplicates.
- Put the Bibtex file in the *_biblio* folder.

Installing the Bibtex manager:

- Instructions [here](https://github.com/inukshuk/jekyll-scholar)
- Add the following lines ```gem 'jekyll-scholar', group: :jekyll_plugins to *Gemfile*
```
group :jekyll_plugins do
  gem "jekyll-scholar"
end
```
- Add the following lines to *_config.yml*
```
plugins: ['jekyll/scholar']
scholar:
  style: modern-language-association
  source: _biblio
  bibliography: BIG.bib
  sort_by: year
  order: descending
  bibliography_template: bibliography
```
- Update Jekyll via ```bundle update```

To customize the visualization of the biblio:
- Download from [here](https://github.com/citation-style-language/styles) the style of your choice (e.g., apa.csl, renamed as my-apa.csl)
- Put it in the main folder
- Reference it in the *scholar* options plugin *_config.yml*
```
plugins: ['jekyll/scholar']
scholar:
  style: my-apa
```
- Change the style (see edits marked as ```<!-- ENR -->``` in my-apa.csl)

## Maintenance

The *_layout* folder contains pages' templates.

The *_pages* folder contains one entry for each page; a page is generated from a template (i.e., layout).

The *_data* folder contains the data to be maintained (team members, publications, news, etc.); these data 
are access by the pages.

The *_includes* folder contains headers and footers.

## Troubleshooting

- If the page is not regenerated, verify that it contains ```regenerate: true``` in the header.

## Copyright

Copyright BIG. Code released under the MIT License.
