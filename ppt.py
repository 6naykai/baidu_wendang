import os.path
from lxml.html import etree
import requests


# 创建目录方法
def create_file(path):
    if not os.path.exists(path):
        os.makedirs(path)


url = "https://wenku.baidu.com/view/f46c328a03768e9951e79b89680203d8cf2f6a0b.html?fr=income1-doc-search&_wkts_" \
      "=1671180998784&wkQuery=%E8%AF%BE%E4%BB%B6 "
content = "测试"

resp = requests.get(url)

print(resp.text)
text = resp.text

html = etree.HTML(text)

img_list = html.xpath('//div[@class="mod flow-ppt-mod"]/div/div/img')

# 计数
cnt = 1

# 文件保存路径
file_path = './wendang_ppt/{}/'.format(content)
create_file(file_path)

# 获取图片
for i in img_list:
    try:
        img_url = i.xpath('./@src')[0]
    except:
        img_url = i.xpath('./@data-src')[0]

    # 文件名称
    file_name = f'{file_path}page_{cnt}.jpg'
    print(file_name, img_url)
    # 下载保存路径
    resp = requests.get(img_url)
    with open(file_name, 'wb') as f:
        f.write(resp.content)

    cnt += 1
