---
title: "BIG - Thesis"
layout: textlay
excerpt: "BIG -- Thesis"
sitemap: false
permalink: /thesis/
---

# Thesis

The BIG research group offers many thesis opportunities, usually (but not exclusively) aimed at Master students in Computer Science and Engineering and related to research projects and/or collaborations with companies.

If you are looking for thesis opportunities with internship in a company, <a href="">click here</a> to see our availabilities.

Check below the open proposals or contact us if you are looking for a thesis on Information Systems, Big Data, or Data Mining.

## Open research thesis

<div id="thesis">

{% for thesis in site.data.thesis %}
{% if thesis.status == "Open" and thesis.location == "BIG" %}

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

## Open thesis within companies

<div id="thesis">

{% for thesis in site.data.thesis %}
{% if thesis.status == "Open" and thesis.location == "company" %}

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

## Completed thesis

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
