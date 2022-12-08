# [The Computing Capstone at NJIT](/home)

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