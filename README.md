# ywcc-capstone.github.io

Herein lies the development documentation for the Computing Capstone website.

# TODOs for Student section
* [ ] Student Navbar
    * [ ] Webex
    * [ ] Canvas
    * [x] Discord
    * [x] Github
    * [x] Youtube
* [ ] Homepage with all the info for each of the events, along with pictures from prior years
    * _Should inspire and get people excited for the Capstone_
    * Open House
    * Midterm Demo
    * Final showcase
* [ ] Student Timeline
    * [ ] Sprints / weeks
* [ ] Student Deliverables
    * [ ] Progress reports
    * [ ] Demo video
    * [ ] Final showcase materials
    * [ ] Final report
* [ ] Student Training
    * [ ] PM Training
    * [ ] Gantt Charts
    * [ ] Agile and Scrum
    * [ ] MDDDE
    * [ ] Scope Document
* [ ] Exec board getting started page
    * _See the [eboard-tools][GitHubEboardTools] repository._
    * [ ] Resources from the Fall 2022 eboard
    * [ ] Stretch: resources from Spring 2022 eboard
* [ ] Student handbook
* [ ] Student forms and data retrieval
    * [ ] Project Track commitment
    * [ ] Feedback
* [ ] Migrate the starter email docs here
    * [ ] The email itself?
    * [ ] Project Manager expectations
    * [ ] Executive Team expectations
    * [ ] Sample RWC brochure
    * [ ] CISCO Project of projects
    * [ ] Capstone introduction pptx
    * [x] Capstone Project Options
    * [x] Syllabus
* [x] Upload syllabus
    * [ ] Grading scorecards need to be uploaded
* [x] Central hub for project track info
* [x] Get the sidebar populated
* [x] Publicize this repository and deploy it on the web


# TODOs for Sponsor section
* [ ] Start here
    * [ ] "What is the Computing Capstone at NJIT?"
    * [ ] Why should you sponsor 
    * [ ] Testimonials
    * [ ] Mailing list registry
* [ ] Sponsors (should list past sponsors and their projects)
    * [ ] Join the Capstone
        * Compile info from the homepage, mailing list, about capstone, contact us, capstone agreement
    * [ ] Donate
        * Make a donation or contribution in support of the YWCC Capstone Program at https://njit-connect.njit.edu/pages/capstone, or write a check to “NJIT Foundation / University Advancement” with the attention set to the YWCC Capstone Program Acct. #200094.
    * [ ] Timeline
        * https://ywcccapstone.com/capstone-2020/
    * [ ] Past projects
        * Google Drive and
        * Get company logos and images here
    * [ ] FAQ
        * https://ywcccapstone.com/faq/
    * [ ] Documents
        * Available in footer.
        * [ ] NJIT Capstone Agreement https://ywcccapstone.com/wp-content/uploads/2019/08/Sponsors-Acknowledgment-Agreement-FIN.pdf
        * [ ] NJIT Student NDA https://ywcccapstone.com/wp-content/uploads/2019/08/NDA-Capstone.pdf

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