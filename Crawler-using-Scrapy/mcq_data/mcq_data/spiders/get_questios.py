from collections import OrderedDict
import re
import scrapy

from mcq_data.items import McqDataItem, link_ref


class QuotesSpider(scrapy.Spider):
    name = "get_questions"

    start_urls = [
        # 'https://www.firstnaukri.com/career-guidance/65-logical-reasoning-questions-and-answers-for-freshers',
        # 'https://www.goeduhub.com/4946/data-structures-mcqs-questions-set-1',
        'https://www.math-only-math.com/math-quiz.html'
        # 'https://www.math-only-math.com/math-quiz-a.html',
        # 'https://www.math-only-math.com/math-quiz-b.html',
        # 'https://www.examveda.com/computer-fundamentals/practice-mcq-question-on-computer-fundamental-miscellaneous/'
    ]


    def parse(self, response):
        
        item = McqDataItem()

        if response.url == link_ref[1]:
            para = response.xpath("//p")[3:124]

            for qstn in para:
                item['question'] = qstn.xpath("./strong/text()").getall()
                temp_data = qstn.xpath("./text()").getall()
                if not temp_data:
                    continue
                item['options'] = temp_data[:4]
                item['answer'] = temp_data[-1]
                item['age_group'] = "16-18"
                yield item

        elif response.url == link_ref[2]:
            para = response.xpath("//div[@itemprop='text']//p/span/strong/text()")
            questions = response.xpath("//div[@itemprop='text']//p/span/text()").getall()
            questions.pop(10)
            options = response.xpath("//div[@itemprop='text']//ol/li/span/text()").getall()
            answers = response.xpath("//div[@itemprop='text']//p/span/strong/text()").getall()

            s, e = 0, 4
            counter = 1
            for q in questions:
                item['question'] = q
                item['options'] = options[s:e]
                item['answer'] = answers[counter].replace("Answer:- ", "")
                item['age_group'] = "13-15"
                s += 4
                e += 4
                counter += 2
                yield item

        elif response.url in link_ref[3]:
            questions = response.xpath("//td//b/text()").getall()
            options_data = response.xpath("//td//form/text()").getall()
            options = []
            for option in options_data:
                if option != "\n \n" or option != "":
                    options.append(option.replace("\n", ""))
            answers_data = response.xpath("//td//form/@onsubmit").getall()
            answers = []
            for answer in answers_data:
                answer.replace("return checkAnswer(this,", "").replace(
                    ");", "").replace("'", "")
            s, e = 0, 4
            for q, ans in zip(questions, answers):
                item['question'] = q
                item['options'] = options[s:e]
                item['answer'] = ans
                item['age_group'] = "06-08"
                s += 4
                e += 4
                yield item


        elif 'examveda' in response.url:
            questions = response.xpath("//div[@class='question-main']/text()").getall()
            options_data = response.xpath(
                "//div[@class='question-inner']//p/label/text()").getall()
            answers = response.xpath(
                "//div[@class='row answer_container']/div/div/div[2]/strong/text()").getall()

            options = []
            s, e = 0, 1
            for i in range(len(options_data)):
                # if e == 49:
                #     break
                options.append(options_data[s] + " " + options_data[e])
                s += 2
                e += 2

            s, e = 0, 4
            for q, ans in zip(questions, answers):
                item['question'] = q
                item['options'] = options[s:e]
                item['answer'] = ans
                item['age_group'] = "06-08"
                s += 4
                e += 4
                yield item