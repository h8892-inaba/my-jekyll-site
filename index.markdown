---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

#assets/rtm_images/rtm_logo.png

layout: home

permalink: /

title: "OpenRTM-aist"
excerpt: "OpenRTM-aist | The power to connect"

feature_rows:
  - title: "ROBOMECH2025"
    excerpt: "ROBOMECH2025申し込み開始しました"
    url: "/community/event/ROBOMECH2025/"
    img_path: "feature_rows/nedo-06.png"
    img_alt: "ROBOMECH2025"
  - title: "OpenRTM-aist 2.0.2 RELEASE"
    excerpt: "OpenRTM-aist 2.0.2 をリリースしました"
    url: "/download/"
    img_path: "feature_rows/rosnews.png"
    img_alt: "RELEASE"
  - title: "OpenRTM-aistを10分で始めよう！"
    excerpt: "Let's start openrtm-aist!"
    url: "/doc/installation/lets_start"
    img_alt: "Only 10 min !?"

---


<a href="/howto_code">howto_code</a>
<a href="/manual_md1">manual_md1</a>

# News...

<hr>
{% for post in site.posts limit: 3 %}
  <article>
    <li>
      <a href="{{ post.url }}">
        <img src="{{post.image}}" alt="hogee" height="50" />
        <br>{{ post.title }} ({{post.date | date: "%B %-d, %Y"}})
      </a>
      <a>
        <br>{{ post.excerpt }}
      </a>
    </li>
  </article>
<hr>
{% endfor %}


# News...

inaba-test show list for post  auther=sharathdt

{% assign sorted-posts = site.posts | where: "author","sharathdt" %}
{% for post in sorted-posts limit: 5 %}
  <li>
    <a href="{{ post.url }}">
        {{post.title}}
    </a>
  </li>
{% endfor %}
