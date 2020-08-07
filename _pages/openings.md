---
title: "BIG - Openings"
layout: textlay
excerpt: "Openings available at the BIG"
sitemap: false
permalink: /openings/
---

# Open positions

{% assign psize = site.data.openings | size %}
{% if psize == 0 %} 
  <p>Unfortunately, there are no available openings at this time. However, feel free to contact any of the [team members]({{ site.url }}{{ site.baseurl }}/team/#staff) for all kinds of information and check the available [thesis proposals]({{ site.url }}{{ site.baseurl }}/teaching/#thesis).</p>
{% endif %}