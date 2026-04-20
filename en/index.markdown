---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

#assets/rtm_images/rtm_logo.png

layout: home

lang: en
title: "Home"
excerpt: "OpenRTM-aist | The power to connect"

swiper_images:
  - src: /assets/images/swiper/10min-startup_ja.png
    link: /ja/doc/installation/lets_start
  - src: /assets/images/swiper/202release.png
    link: /ja/download
  - src: /assets/images/swiper/contest2025_2.png
    link: /ja/content/content/rtmcontest2025/
  - src: /assets/images/swiper/what_is_openrtm_ja2.jpg
    link: /ja/doc/aboutopenrtm/rtmiddleware
---

{%- assign current_lang = site.default_lang | default: 'ja' -%}

{%- if page.url contains '/ja/' -%}
  {%- assign current_lang = 'ja' -%}
{%- elsif page.url contains '/en/' -%}
  {%- assign current_lang = 'en' -%}
{%- endif -%}


<hr>
{% include top-swiper.html %}


<script src="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function () {
  new Swiper('.top-swiper', {
    loop: true,
    autoplay: {
      delay: 4000,
      disableOnInteraction: false
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev'
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true
    }
  });
});
</script>
<hr>


### [how to code]({{ site.baseurl }}/howto_code)
### [manual_md1]({{ site.baseurl }}/manual_md1)

# News

<div class="news-grid">
  {% for post in site.posts limit: 6 %}
    <article class="news-item">
      <a href="{{ post.url | relative_url }}">
        {% if post.image %}
          <div class="news-thumb">
          <img src="{{ post.image | relative_url }}" alt="">
          </div>
        {% endif %}
      </a>
     <span class="news-date-wrap">
     <span class="news-date-day">{{ post.date | date: "%-d" }}</span>
     <span class="news-date">{{ post.date | date: " %b , %Y" }}</span>
     </span>
     <h4 class="news-title">
     <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
     </h4>
     <p class="top-news__excerpt">
              {{ post.excerpt | strip_html | truncate: 100 }}
     </p>
     <div class="news-more-wrap">
      <a class="news-more" href="{{ post.url | relative_url }}">続きを読む</a>
    </div>
    </article>
  {% endfor %}
</div>
<br>
<div class="news-more-wrap">
  <a class="news-more" href="{{ site.baseurl }}/ja/news/">その他のnews</a>
</div>
<hr>
<!-- /section -->
