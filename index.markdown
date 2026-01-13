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
    url: "/ja/community/event/ROBOMECH2025/"
    img_path: "feature_rows/contest2025_news.png"
    img_alt: "ROBOMECH2025"
  - title: "OpenRTM-aist 2.0.2 RELEASE"
    excerpt: "OpenRTM-aist 2.0.2 をリリースしました"
    url: "/ja/download/"
    img_path: "feature_rows/contest2025_news_.png"
    img_alt: "RELEASE"
  - title: "OpenRTM-aistを10分で始めよう！"
    excerpt: "Let's start openrtm-aist!"
    url: "/ja/doc/installation/lets_start"
    img_alt: "Only 10 min !?"
    img_path: "feature_rows/10min-startup_ja.png"

---

<script>
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
</script>



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
