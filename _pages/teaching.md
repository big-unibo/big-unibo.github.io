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

{% for course in site.data.courses-university %}
<strong>[{{ course.title }}]({{ course.link }})</strong> ({{ course.language }})<br>
<i>{{ course.venue }}; {{ course.course }}</i><br>
{% if course.teachers %}Teachers: {{ course.teachers }}{% endif %}
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

<strong>{{ thesis.title }}</strong>, {{ thesis.student }}, {{ thesis.year }}<br>
Supervisor: {{ thesis.supervisor }}
{% if thesis.co-supervisor %}
Co-supervisors: {{ thesis.co-supervisor }}
{% endif %}
{% if thesis.slides %}
Slides: {{ thesis.slides }}
{% endif %}
<br>

{% endif %}
{% endfor %}

</div>
