import scrapy
import jmespath
import json
import js2xml


class FreepicSpider(scrapy.Spider):
    name = "freepic"
    # allowed_domains = ["mydomain.com"]
    # start_urls = ["file:///home/anselmo/Estudo/Candidato/LuizaMario/scrapy/projects/qrcode2.html"]
    start_urls = ["https://www.freepik.com/free-photos-vectors/qrcode/2"]

    def parse(self, response):
        # se não sei em qual script está a estrutura
        # all_urls = []
        # scripts = response.xpath("//script//text()").getall()
        # print('len scripts', len(scripts))
        # for i, script in enumerate(scripts):
        #     print('script', i)
        #     data = None
        #     try:
        #         print('try js2xml')
        #         jstree = js2xml.parse(script)
        #         # print(js2xml.pretty_print(jstree))
        #         data = js2xml.jsonlike.getall(jstree)
        #     except:
        #         print('js2xml error')
        #         try:
        #             print('try json')
        #             data = json.loads(script)
        #         except:
        #             print('json error')
        #             pass
        #     if data:
        #         print('tem dados')
        #         urls = jmespath.search(
        #             'props.pageProps.items[*].preview.url', data)
        #         if urls:
        #             print('achou urls')
        #             all_urls.extend(urls)
        # print(len(urls))

        # se sei exatamente qual script está a estrutura
        script = response.xpath(
            "//script[@type='application/json']//text()").get()
        data = json.loads(script)
        urls = jmespath.search(
            'props.pageProps.items[*].preview.url', data)
        print(len(urls))

