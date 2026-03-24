---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

#assets/rtm_images/rtm_logo.png

layout: home

permalink: /

title: "OpenRTM-aist"
excerpt: "OpenRTM-aist | The power to connect"

feature_rows:
  - title: "OpenRTM-aistとは？"
    excerpt: "ロボットシステムをコンポーネント思考開発するためのソフトウェアプラットフォームです。"
    url: "/ja/doc/aboutopenrtm/rtmiddleware/"
    img_path: "feature_rows/contest2025_news.png"
    img_alt: "What's OpenRTM-aist?"
  - title: "OpenRTM-aist 2.0.2 RELEASE"
    excerpt: "OpenRTM-aist 2.0.2 をリリースしました"
    url: "/ja/download/"
    img_path: "feature_rows/202release_news.png"
    img_alt: "RELEASE"
  - title: "10分で始めよう！"
    excerpt: "インストール、サンプルの起動・接続、RTSystemEditor・rtshellを使った基本的動作確認の入門ガイド"
    url: "/ja/doc/installation/lets_start"
    img_alt: "Only 10 min !?"
    img_path: "feature_rows/10min_test.png"

---



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
