---
title: "BIG - Teaching"
layout: textlay
excerpt: "BIG -- Teaching"
sitemap: false
permalink: /teaching/
---

# Teaching

The BIG research group is teaching several courses, 
both at the [University of Bologna](#university)
and at [Master courses](#master).

If you are interested in doing your Master/Bachelor thesis with us,
check our [open thesis proposals](#thesis).

## University

<div id="university">

{% for c in site.data.courses-university %}
<strong>[{{ c.title }}]({{ c.link }})</strong><br>
<i>{{ c.venue }}</i><br>
<ul>
{% for course in c.courses %}
<li>
{% if course.homelink %}
<a href="{{ site.url }}{{ site.baseurl }}/{{ course.homelink }}">{{ course.title }}</a> ({{ course.language }})<br> 
{% else %}
<a href="{{ course.link }}">{{ course.title }}</a> ({{ course.language }})<br> 
{% endif %}
<!--[{{ course.title }}]({{ course.link }}) ({{ course.language }})<br>-->
{% if course.teachers %}Teacher: {{ course.teachers }}{% endif %}
</li>
{% endfor %}
</ul>
{% endfor %}

</div>

## Master

<div id="master">

{% for course in site.data.courses-master %}
<strong>[{{ course.title }}]({{ course.link }})</strong> ({{ course.language }})<br>
<i>{{ course.venue }}; {{ course.master }}</i><br>
{% if course.teachers %}Teachers: {{ course.teachers }}{% endif %}
{% endfor %}

</div>

## Thesis

<div id="thesis">

{% for thesis in site.data.thesis %}
{% if thesis.status == "Open" %}

<strong>{{ thesis.title }}</strong><br>
{{ thesis.level }} - {{ thesis.type }}<br>
Field: {{ thesis.field }}<br>
Status: <span class="thesis-status-{{ thesis.status }}">{{ thesis.status }}</span><br>
Abstract: {{ thesis.abstract }}<br>
Contact: {{ thesis.contact }}

{% endif %}
{% endfor %}

{% for thesis in site.data.thesis %}
{% if thesis.status == "Taken" %}

<strong>{{ thesis.title }}</strong><br>
{{ thesis.level }} - {{ thesis.type }}<br>
Field: {{ thesis.field }}<br>
Status: <span class="thesis-status-{{ thesis.status }}">{{ thesis.status }}</span><br>
Abstract: {{ thesis.abstract }}<br>
Contact: {{ thesis.contact }}

{% endif %}
{% endfor %}

</div>

### Completed thesis

<div id="completed-thesis">

{% for thesis in site.data.thesis %}
{% if thesis.status == "Closed" %}

<strong>{% if thesis.link %}<a href="{{ thesis.link }}">{% endif %}{{ thesis.title }}{% if thesis.link %}</a>{% endif %}</strong>, {{ thesis.student }}, {{ thesis.year }}<br>
Supervisor: {{ thesis.supervisor }}<br>
{% if thesis.co-supervisor %} Co-supervisors: {{ thesis.co-supervisor }}<br>{% endif %}
{% if thesis.slides %} Slides: {{ thesis.slides }} {% endif %}


{% endif %}
{% endfor %}

</div>
