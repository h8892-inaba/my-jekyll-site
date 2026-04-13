---

layout: page
title: "Manual_md"
permalink: /manual_md3/ 

---

## 表組み(html)
<table class="table-alt">
  <tr>
    <th>配置</th>
    <th>LEFT:100</th>
    <th>CENTER:200</th>
    <th>RIGHT:500</th>
  </tr>
  <tr>
    <td>セルの結合</td>
    <td>></td>
    <td>></td>
    <td>CENTER:表キャプション</td>
  </tr>
  <tr>
    <td>セルに背景色を付ける</td>
    <td>`ヘッダ1ヘッダ1</td>
    <td>~ヘッダ2ヘッダ2</td>
    <td>~ヘッダ3ヘッダ3</td>
    <td>`</td>
  </tr>
  <tr>
    <td>セル内で開業する</td>
    <td>></td>
    <td>></td>
    <td>セルの中で<br>改行してみる。</td>
  </tr>
  <tr>
    <td>セルの結合と配置</td>
    <td>></td>
    <td>></td>
    <td>RIGHT:右寄せ+3セル結合</td>
  </tr>
  <tr>
    <td>セルの結合と配置</td>
    <td>></td>
    <td>></td>
    <td>CENTER:中央+3セル結合</td>
  </tr>
  <tr>
    <td>セルの結合と配置</td>
    <td>></td>
    <td>></td>
    <td>LEFT:左寄せ+3セル結合</td>
  </tr>
</table>


<table class="table-alt">
  <tr>
    <th>配置</th>
    <th>LEFT:100</th>
    <th>CENTER:200</th>
    <th>RIGHT:500</th>
  </tr>
  <tr>
    <td>セルの結合</td>
    <td>></td>
    <td>></td>
    <td>CENTER:表キャプション</td>
  </tr>
  <tr>
    <td>セルに背景色を付ける</td>
    <td>`ヘッダ1ヘッダ1</td>
    <td>~ヘッダ2ヘッダ2</td>
    <td>~ヘッダ3ヘッダ3</td>
    <td>`</td>
  </tr>
  <tr>
    <td>セル内で開業する</td>
    <td>></td>
    <td>></td>
    <td>セルの中で<br>改行してみる。</td>
  </tr>
  <tr>
    <td>セルの結合と配置</td>
    <td>></td>
    <td>></td>
    <td>RIGHT:右寄せ+3セル結合</td>
  </tr>
  <tr>
    <td>セルの結合と配置</td>
    <td>></td>
    <td>></td>
    <td>CENTER:中央+3セル結合</td>
  </tr>
  <tr>
    <td>セルの結合と配置</td>
    <td>></td>
    <td>></td>
    <td>LEFT:左寄せ+3セル結合</td>
  </tr>
</table>

<br>


## 表（markdown）

横方向にセルを結合する場合は、何も設定しないか>を設定。(未対応)

```
 |header1|header2|header3|
 |:------|:-----:|------:|
 |hoge   |fuga   |piyo   |
 |hoge   |       |piyo   |
 |>      |fuga   |piyo   |
 |hoge   |fuga   |       |
 |hoge   |>      |piyo   |
 |hoge   |       |       |
 |>      |fuga   |       |
 |>      |>      |piyo   |
```

|header1|header2|header3|
|:------|:-----:|------:|
|hoge   |fuga   |piyo   |
|hoge   |       |piyo   |
|>      |fuga   |piyo   |
|hoge   |fuga   |       |
|hoge   |>      |piyo   |
|hoge   |       |       |
|>      |fuga   |       |
|>      |>      |piyo   |


縦方向にセルを結合する場合は、^を設定。(未対応)


```
 |header1|header2|header3|
 |:------|:-----:|------:|
 |hoge   |fuga   |piyo   |
 |hoge   |^      |^      |
 |hoge   |fuga   |^      |
```

|header1|header2|header3|
|:------|:-----:|------:|
|hoge   |fuga   |piyo   |
|hoge   |^      |^      |
|hoge   |fuga   |^      |


