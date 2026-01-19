---
layout: page
title: 
---

init
<!-- #ref(dl_logo_wrob.jpg,60%,right,margin=10,around,url=http://biz.nikkan.co.jp/eve/s-robot/index.html) -->
<div align="right"><a href="http://biz.nikkan.co.jp/eve/s-robot/index.html"><img src="DSC_0025.png" width="50%; margin:10px;" align="right"></a></div>


#contents(4)

<!-- ** 開催案内 -->
## 開催報告

2017年11月7日(火)～11月8日(水)の日程で、高度ポリテクセンターの能力開発セミナーの一環として、「RTミドルウェアによるロボットプログラミング技術」講習会を開催いたしました。

- コース案内(2016年版): http://www.apc.jeed.or.jp/seminar/course/16semiE077.html

## 日時・場所

- **日時**: 2017年11月7日(火)8日(水), 10時00分～16時30分
- **場所**: [高度ポリテクセンター](http://www.apc.jeed.or.jp/index.html)
  - [交通アクセス](http://www.apc.jeed.or.jp/04_apc/04_02.html)
- **主催**: 高度ポリテクセンター
<!-- -''参加者''：6名 -->
- **参加費**: 20,000円

## プログラム

<table class="table-alt">
  <tr>
    <th>CENTER:100</th>
    <th>LEFT:500</th>
    <th>c</th>
  </tr>
  <tr>
    <td>></td>
    <td>CENTER: **11月7日（火）**</td>
  </tr>
  <tr>
    <td>10:00 -11:00</td>
    <td>**１．コース概要**<br>　（１）ロボットシステムプログラミングの現状 <br>　（２）ロボットOS・ミドルウェア <br>　（３）RTミドルウェア(RTM)を用いたロボット開発 <br> **資料:** <div align="center"><a href="171107-01.pdf"><img src="171107-01.pdf" width="100;"></a></div>;</td>
  </tr>
  <tr>
    <td>11:00 -12:00 <br> 13:00-14:00</td>
    <td>**２．プログラミングの基礎** <br>　（１）プログラミングの基礎 <br>　（２）Linuxでのプログラミング <br>　（３）Windowsでのプログラミング <br> <br> **サンプルコード:** <div align="center"><a href="arm2dof_ver001.zip"><img src="arm2dof_ver001.zip" width="100;"></a></div>; <br> **資料:** <div align="center"><a href="171107-02.pdf"><img src="171107-02.pdf" width="100;"></a></div>;</td>
  </tr>
  <tr>
    <td>12:00 -13:00</td>
    <td>昼食</td>
  </tr>
  <tr>
    <td>14:00 -16:30</td>
    <td>**３．RTMによるプログラミング** <br> （１）RTコンポーネントの設計 <br> （２）RTコンポーネントの実装 <br> （３）テスト	<br> <a href="/ja/node/6057">チュートリアル（画像処理コンポーネントの作成 Windows編）</a> <br> <a href="/ja/node/6058">チュートリアル（画像処理コンポーネントの作成 Linux編）</a> <br> **資料:** <div align="center"><a href="171107-03.pdf"><img src="171107-03.pdf" width="100;"></a></div>;</td>
  </tr>
</table>

<table class="table-alt">
  <tr>
    <th>CENTER:100</th>
    <th>LEFT:500</th>
    <th>c</th>
  </tr>
  <tr>
    <td>></td>
    <td>CENTER: **11月8日（水）**</td>
  </tr>
  <tr>
    <td>10:00 -12:00</td>
    <td>**４．ロボットの運動学と制御の基礎** <br>　（１）ロボットと運動学 <br>　（２）ロボットと制御 <br> **資料:** <div align="center"><a href="171108-04.pdf"><img src="171108-04.pdf" width="100;"></a></div>; <br> **プログラム1:** <div align="center"><a href="arm2dof.zip"><img src="arm2dof.zip" width="100;"></a></div>; <br> **プログラム2:** <div align="center"><a href="joystick.zip"><img src="joystick.zip" width="100;"></a></div>; <br>  **解答:' <div align="center"><a href="171108-06.pdf"><img src="171108-06.pdf" width="100;"></a></div>; <br> **プログラム1(解答):** <div align="center"><a href="arm2dof.ans_.zip"><img src="arm2dof.ans_.zip" width="100;"></a></div>; <br> **プログラム2(解答):'' <div align="center"><a href="joystick.ans_.zip"><img src="joystick.ans_.zip" width="100;"></a></div>;</td>
  </tr>
  <tr>
    <td>12:00 -13:00</td>
    <td>昼食</td>
  </tr>
  <tr>
    <td>13:00 -16:30</td>
    <td>**５．総合演習** <br>　（１）ロボットシステムの設計 <br> 　（２）ロボット制御プログラムの作成 <br> <a href="/ja/node/6310">チュートリアル（Raspberry Pi Mouseシミュレータ、Windows編）</a>  <br> <a href="/ja/node/6042">チュートリアル（RaspberryPiマウス）</a> <br> **資料:** <div align="center"><a href="171108-05.pdf"><img src="171108-05.pdf" width="100;"></a></div>;</td>
  </tr>
</table>

<br>

<span style="color:red;">小型ロボットを使って実習を行います。</span>;

### RaspberryPiマウス
RaspberryPiマウスは、株式会社アールティから発売されているメインボードにRaspberry Piを使った左右独立二輪方式の小型移動プラットフォームロボットです。
RaspberryPiを利用しているので、実機上で開発したり、容易に拡張したりすることが可能です。今回は、あらかじめマウス制御用コンポーネントがインストールされている状態で、これを制御するRTコンポーネントを作成していただきます。


<div align="center"><a href="http://www.rt-net.jp/wp-content/uploads/2015/08/DSC_0025.png"><img src="http://www.rt-net.jp/wp-content/uploads/2015/08/DSC_0025.png" width="20%; margin:10px;"></a></div>

- [Raspberry Pi Mouse 活用事例](http://openrtm.org/openrtm/ja/content/raspberry_pi_mouse)


### インストールするソフトウエア

あらかじめインストールしておくべきソフトウエアは以下のとおりです。以下のリンクをクリックし、ファイルをダウンロード・インストールしてください。<br>
一部のリンクはダウンロードページへ飛びますので、飛んだ先のページ内で適切なファイルをそれぞれダウンロードしてください。


#### Visual Studio 

- Visual Studio 2013推奨：[こちらのページ](https://www.visualstudio.com/ja-jp/downloads/download-visual-studio-vs#DownloadFamilies_2) から無償版をダウンロードできます。
  - ポリテクセンターのPCにはインストール済みです。

#### Python

- [Python2.7.10](https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi)
  - <span style="color:red;">Python2.7.11もすでにリリースされていますが非推奨です。</span>;
  - <span style="color:red;">OpenRTM-aistやPyYAMLをインストールする前にインストールしてください</span>;

#### OpenRTM-aist 1.1.2-RELEASE版 (C++版、Python版）

- インストーラには 32bit/64bit の区別がありますが今回は32bit版を使用します。
  - [Windows用インストーラ(32bit)](/ja/content/openrtm-aist-c-112-release#toc2)


#### その他

以下のソフトウェアも必須です。忘れずにインストールしてください。

- [PyYAML](http://pyyaml.org/download/pyyaml/PyYAML-3.11.win32-py2.7.exe)
- [CMake](https://cmake.org/files/v3.5/cmake-3.5.2-win32-x86.msi)
- [Doxygen](http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.11-setup.exe)
- [TeraTerm](https://ja.osdn.net/projects/ttssh2/)
- 使い慣れたエディタ: EclipseやPythonに付属のエディタでも構いませんが、使い慣れたエディタが入っていた方が良いでしょう
  - [Vim](https://www.kaoriya.net/software/vim/)
  - [sublime text3](https://www.sublimetext.com/3)
    - [日本語化の方法](http://webkaru.net/dev/sublime-text-3-japanize/)
  - [atom](https://atom.io/)


## 資料

### １．コース概要

<!-- Invalid YouTube URL: http://www.slideshare.net/68436966 -->

### ２．プログラミングの基礎 

<!-- Invalid YouTube URL: http://www.slideshare.net/68437439 -->


### ３．RTMによるプログラミング

<!-- Invalid YouTube URL: http://www.slideshare.net/68437448 -->

### ４．ロボットの運動学と制御の基礎

<!-- Invalid YouTube URL: http://www.slideshare.net/68437436 -->

<!-- Invalid YouTube URL: http://www.slideshare.net/68610156 -->


### ５．総合演習

<!-- Invalid YouTube URL: http://www.slideshare.net/68437454 -->


<!-- ** コースの様子 -->
<!-- #ref(161110-00.jpg,center,nolink) -->
<br>

<!-- #ref(161110-01.jpg,center,nolink) -->
<br>

<!-- #ref(161019-03.jpg,center,nolink) -->
<br>

<!-- #ref(161019-04.jpg,center,nolink) -->
<br>


<!-- #ref(161019-05.jpg,center,nolink) -->



