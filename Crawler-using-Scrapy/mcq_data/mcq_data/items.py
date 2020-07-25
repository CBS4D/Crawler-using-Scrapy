# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


link_ref = {
	1: "https://www.firstnaukri.com/career-guidance/65-logical-reasoning-questions-and-answers-for-freshers",
	2: "https://www.goeduhub.com/4946/data-structures-mcqs-questions-set-1",
	3: ["https://www.math-only-math.com/math-quiz.html",
        "https://www.math-only-math.com/math-quiz-a.html",
        "https://www.math-only-math.com/math-quiz-b.html"]
}

class McqDataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    question = scrapy.Field()
    options = scrapy.Field()
    answer = scrapy.Field()
    age_group = scrapy.Field()