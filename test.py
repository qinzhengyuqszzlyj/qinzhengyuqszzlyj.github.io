import os


def replace_text_in_files(url_to_replace, new_url):
    for root, dirs, files in os.walk('.'):  # '.' 表示当前目录，可替换为具体路径
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = content.replace(url_to_replace, new_url)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            except UnicodeDecodeError:
                # 如果用utf-8解码失败，尝试用gbk等其他常见编码（可按需添加更多尝试的编码方式）
                try:
                    with open(file_path, 'r', encoding='gbk') as f:
                        content = f.read()
                    content = content.replace(url_to_replace, new_url)
                    with open(file_path, 'w', encoding='gbk') as f:
                        f.write(content)
                except Exception as e:
                    print(f"处理文件 {file_path} 时出现错误: {e}")
            except Exception as e:
                print(f"处理文件 {file_path} 时出现错误: {e}")


if __name__ == "__main__":
    old_url_https = "https://qinzhengyuqszzlyj.github.io/"
    new_url = "https://qinzhengyuqszzlyj.github.io/"
    replace_text_in_files(old_url_https, new_url)
    replace_text_in_files(old_url_http, new_url)
