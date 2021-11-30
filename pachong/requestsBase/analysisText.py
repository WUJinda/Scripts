import json

from lxml import etree

if __name__ == '__main__':

    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse('HAL-Inria.html', parser=parser)
    res_list = tree.xpath('//div[@class="media-body"]/a/@href')
    article_name_list = tree.xpath('//div[@class="media-body"]//strong/a/text()')

    print(res_list)
    print(article_name_list)

    site_list = []
    for str in res_list:
        if str[0] == '/':
            str = 'https://hal.archives-ouvertes.fr' + str
            site_list.append(str)
        else:
            site_list.append(str)

    print(site_list)

    article_name_site = dict(map(lambda x, y: [x, y], article_name_list, site_list))

    print(article_name_site)

    with open('articles.json', 'w') as f:
        json.dump(article_name_site, f)  # 会在目录下生成一个1.json的文件，文件内容是dict数据转成的json数据
