# [The Computing Capstone @ NJIT](/home)
_Unofficial Website_

<!-- Clickable icons -->
<a href="http://github.com/ywcc-capstone"><i class="fab fa-github"></i></a>
<a href="https://njit.gg/capstone"><i class="fab fa-discord"></i></a>
<a href="https://www.youtube.com/@ywcc.capstone.fall22"><i class="fab fa-youtube"></i></a>

<hr />

## Students
{% assign student-pages = site.students | sort: 'order' %}
{% for page in student-pages %}
    {% if page.published %}
* [{{ page.title }}]({{ page.url }})
    {% endif %}
{% endfor %}

<hr /> 

## [Sponsors]() 
Herein lies information for **sponsors** wanting to understand the purpose of
this course and how to partner with NJIT.


[Students]: /students/
[StartHere]: /students/start_here
[OpenHouse]: /students/open_house
[ProjectTracks]: /students/project_tracks
[MidtermDemo]: /students/midterm_demo
[FinalShowcase]: /students/final_showcase