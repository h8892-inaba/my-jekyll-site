import os
import requests
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited_urls = set()

def is_excluded(url_path, exclude_dirs):
    return any(url_path.startswith(exclude) for exclude in exclude_dirs)

def sanitize_path(url_path):
    path = url_path.split("?")[0].rstrip("/")
    return path if path else "index"


def download_image_for_page(base_url, img_src, page_path, exclude_dirs, output_root):
    full_url = urljoin(base_url, img_src)
    parsed_img_url = urlparse(full_url)
    img_filename = os.path.basename(parsed_img_url.path)

    if is_excluded(parsed_img_url.path, exclude_dirs):
        print(f"Skipping excluded image: {parsed_img_url.path}")
        return

    # 保存先をカレントディレクトリに変更
    save_path = os.path.join(os.getcwd(), img_filename)

    if os.path.exists(save_path):
        print(f"Already exists: {save_path}, skipping.")
        return

    try:
        response = requests.get(full_url, stream=True, timeout=10)
        if response.status_code == 200:
            with open(save_path, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Saved: {save_path}")
        else:
            print(f"Failed to fetch image: {full_url} (status {response.status_code})")
    except Exception as e:
        print(f"Error downloading {full_url}: {e}")


#def process_page(url, base_domain, path_prefix_filter, exclude_dirs, output_root):
#    if url in visited_urls:
#        return
#    visited_urls.add(url)

#    try:
#        response = requests.get(url, timeout=10)
#        soup = BeautifulSoup(response.content, "html.parser")
#        body = soup.body
#        page_path = urlparse(url).path

#        if body:
#            images = body.find_all("img", src=True)
#            for img in images:
#                img_src = img["src"]
#                download_image_for_page(url, img_src, page_path, exclude_dirs, output_root)

#        for link in soup.find_all("a", href=True):
#            href = link["href"]
#            joined_url = urljoin(url, href)
#            parsed = urlparse(joined_url)

#            if parsed.netloc == base_domain and parsed.path.startswith(path_prefix_filter):
#                process_page(joined_url, base_domain, path_prefix_filter, exclude_dirs, output_root)

#    except Exception as e:
#        print(f"Failed to process page {url}: {e}")

def process_page(url, exclude_dirs):
    downloaded_urls = set()

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        body = soup.body

        if body:
            images = body.find_all("img", src=True)
            for img in images:
                img_src = img["src"]
                full_url = urljoin(url, img_src)

                if full_url in downloaded_urls:
                    continue  # 同じ画像はスキップ
                downloaded_urls.add(full_url)

                download_image_for_page(url, img_src, exclude_dirs)

    except Exception as e:
        print(f"Failed to process page {url}: {e}")



def crawl_images(start_urls, path_prefixes, exclude_dirs, output_root):
    for i, start_url in enumerate(start_urls):
        parsed_start = urlparse(start_url)
        base_domain = parsed_start.netloc

        # path_prefix は複数与えられた場合は対応するものを使う、足りない場合は最後を繰り返し使用
        if i < len(path_prefixes):
            path_prefix_filter = path_prefixes[i]
        else:
            path_prefix_filter = path_prefixes[-1] if path_prefixes else "/"

        print(f"\n=== Processing: {start_url} with prefix filter: {path_prefix_filter} ===\n")
        process_page(start_url, base_domain, path_prefix_filter, exclude_dirs, output_root)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OpenRTM 画像クロールスクリプト（複数URL対応）")
    parser.add_argument("--start_url", required=True, nargs="+", help="クロール開始URL（複数可）")
    parser.add_argument("--start_url_file", type=str, help="URLを列挙したファイルパス（1行1URL）")
    parser.add_argument("--path_prefix", required=False, nargs="+", default=[], help="対象パスのフィルタ（start_urlと順に対応）")
    parser.add_argument("--output_root", default="downloaded_images", help="保存先ルートディレクトリ")
    parser.add_argument("--exclude", nargs="*", default=[], help="除外する画像ディレクトリパス（複数可）")

    args = parser.parse_args()

    # URL読み込み処理の置き換え
    if args.start_url_file:
        # ファイルからURLを読み込む
        with open(args.start_url_file, "r", encoding="utf-8") as f:
            start_urls = [line.strip() for line in f if line.strip()]
    else:
        start_urls = args.start_url

    # 通常通り crawl_images 呼び出し
    crawl_images(
        start_urls=start_urls,
        path_prefixes=args.path_prefix,
        exclude_dirs=args.exclude,
        output_root=args.output_root
    )

