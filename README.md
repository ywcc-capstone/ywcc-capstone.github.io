# ywcc-capstone.github.io

Herein lies the development documentation for the Computing Capstone website.

# TODOs
* [ ] Homepage with intro, useful links (discord, webex, surveys)
* [ ] Central page with all the info for each of the events, along with pictures from prior years
    * Open House
    * Midterm Demo
    * Final showcase
* [ ] Exec board getting started page
    * _See the [eboard-tools][GitHubEboardTools] repository._
    * [ ] Resources from the Fall 2022 eboard
    * [ ] Stretch: resources from Spring 2022 eboard
* [ ] Student handbook
* [ ] Forms and data retrieval
* [x] Central hub for project track info
* [x] Upload syllabus
* [x] Get the sidebar populated
* [x] Publicize this repository and deploy it on the web

# Local Development
This site is deployed using GitHub Pages and Jekyll, a freely available tools to
generate and deploy static webpages.

1. [Install Ruby and Jekyll](https://jekyllrb.com/docs/installation/) for your system.
2. Clone this repository to your local machine
```
$ git clone https://github.com/ywcc-capstone/ywcc-capstone.github.io.git
```
3. Install the dependencies and serve it to localhost
```
$ bundle install
$ bundle exec jekyll serve
```
4. Create your own development branch with your changes, tagged with your UCID.
```
$ git checkout -b ucid123/dev
```
5. Make your changes, and open a pull request to the branch `gh-pages`. This
branch is public-facing, thus all changes must be reviewed prior to merging.

[GitHubEboardTools]: https://github.com/ywcc-capstone/eboard-tools