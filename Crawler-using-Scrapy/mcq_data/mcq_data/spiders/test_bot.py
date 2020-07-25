from collections import OrderedDict
import re
import scrapy

from mcq_data.items import McqDataItem, link_ref



class TestBotSpider(scrapy.Spider):
    name = 'test_bot'
    start_urls = [
        'https://www.examveda.com/computer-fundamentals/practice-mcq-question-on-computer-fundamental-miscellaneous/',
        'https://www.examveda.com/c-program/practice-mcq-question-on-c-fundamentals/',
        'https://www.examveda.com/competitive-english/practice-mcq-question-on-ordering-of-sentences/',
        'https://www.examveda.com/arithmetic-ability/practice-mcq-question-on-algebra/',
        'https://www.examveda.com/html/practice-mcq-question-on-basic-html/',
        'https://www.examveda.com/competitive-reasoning/practice-mcq-question-on-number-series-completion/',
        'https://www.examveda.com/competitive-reasoning/practice-mcq-question-on-puzzle/',
        'https://www.examveda.com/competitive-reasoning/practice-mcq-question-on-coding-and-decoding/',
        'https://www.examveda.com/competitive-reasoning/practice-mcq-question-on-classification/',
        'https://www.goeduhub.com/4946/data-structures-mcqs-questions-set-1'
    ]


    def parse(self, response):
        
        item = McqDataItem()

        if 'examveda' in response.url:
            questions = response.xpath("//div[@class='question-main']/text()").getall()
            options_data = response.xpath(
                "//div[@class='question-inner']//p/label/text()").getall()
            answers = response.xpath(
                "//div[@class='row answer_container']/div/div/div[2]/strong/text()").getall()
            solutions_data = response.xpath(
                "//div[@class='row answer_container']/div/div/div[3]/text()").getall()

            solutions = []
            options = []
            s, e = 0, 1
            for i in range(len(options_data)):
                if e == len(options_data) - 1:
                    break

                options.append(options_data[s] + " " + options_data[e])
                s += 2
                e += 2

            for solution in solutions_data:
                if '\n\t' not in solution:
                    if isinstance(i, str):
                        solutions.append(i.strip())
                    else:
                        solutions.append(i)

            s, e = 0, 4
            for q, ans , sol in zip(questions, answers, solutions):
                if "algebra" in response.url:
                    item['age_group'] = "09-10"
                elif any(word in response.url \
                    for word in ['basic-html', 'series', 'classification']):
                    item['age_group'] = "11-12"
                elif any(word in response.url \
                    for word in ['and-decoding', 'puzzle', 'sentences']):
                    item['age_group'] = "13-15"
                elif any(word in response.url for word in ['fundamental']):
                    item['age_group'] = "16-18"
                item['answer'] = ans
                item['options'] = options[s:e]
                item['question'] = q
                s += 4
                e += 4
                yield item

            next_page = response.xpath("//div[@class='pagination']//a/@href").getall()
            if next_page:
                next_page = next_page[-1]
                # next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
            else:
                next_page = 'https://www.goeduhub.com/4946/data-structures-mcqs-questions-set-1'
                yield scrapy.Request(next_page, callback=self.parse)