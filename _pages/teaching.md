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
check our [open thesis proposals](/thesis).

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