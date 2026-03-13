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

<!--script>
  if (!window.__sidebarSearchInitialized) {
    window.__sidebarSearchInitialized = true;

    const input = document.getElementById('sidebar-search-input');
    const results = document.getElementById('sidebar-results');

    SimpleJekyllSearch({
      searchInput: input,
      resultsContainer: results,
      json: '{{ "/search.json" | relative_url }}',
      searchResultTemplate: '<li><a href="{url}">{title}</a></li>',
      noResultsText: '<li class="no-results">見つかりませんでした</li>',
      limit: 10
    });

    // 入力に応じて表示/非表示を切り替え
    const toggle = () => {
      const has = results.children.length > 0 && input.value.trim().length > 0;
      results.classList.toggle('has-results', has);
      if (!has) results.classList.remove('has-results');
    };

    input.addEventListener('input', () => setTimeout(toggle, 0));
    input.addEventListener('focus', () => setTimeout(toggle, 0));

    // 外をクリックしたら閉じる
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.nav-search')) results.classList.remove('has-results');
    });

    // Escで閉じる
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') results.classList.remove('has-results');
    });
  }
</script-->

hogehoge---0011


### [how to code]({{ site.baseurl }}/howto_code)
### [manual_md1]({{ site.baseurl }}/manual_md1)


# News...

<ul>
  {% for post in site.posts %}
<hr>
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <small>{{ post.date | date: "%Y-%m-%d" }}</small>
    </li>
  {% endfor %}
<hr>
</ul>


<hr>
{% for post in site.posts limit: 3 %}
  <article>
    <li>
      <!--a href="{{ post.url }}"-->
      <a href="{{ post.url }}">
        <img src="{{post.image}}" alt="hogee" height="50" />
        <br>{{ post.title }} ({{post.date | date: "%B %-d, %Y"}})
      </a>
      <a>
        test_news0301
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
