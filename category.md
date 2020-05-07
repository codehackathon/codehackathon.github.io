---
layout: page
title: Categories
clickbait: All of our categories, in one place.
---

{% for category in site.categories %}
  <h4>{{ category[0] | upcase}}</h4>
  <ul>
    {% for post in category[1] %}
      <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}
