NAME_TAG = '//span[@class = "name"]/text()'
GENRES_TAG = '//p[@class = "elementList"]/span[@class = "elem_genre "]/a[@class = "element-link"]/text()'
AUTHOR_TAG = '//div[@class = "subject-meta col-sm-7"]/p[@class = "elementList"]/span[@class = "elem_author "] \
            /a[@class = "person-link"]/text()'
YEAR_TAG = '//div[@class = "subject-meta col-sm-7"]/p[@class = "elementList"]/span[@class = "elem_year "] \
            /a[@class = "element-link"]/text()'
TRANSLATORS_TAG = '//div[@class = "subject-meta col-sm-7"]/p[@class = "elementList"]/span[@class = "elem_translator "] \
            /a[@class = "person-link"]/text()'
DESCRIPTION_TAG = '//div[@class = "manga-description"]//text()'
DESCRIPTION_ALT_TAG = '//div[@class = "manga-description"]/p/text()'
IMAGE_TAG = '//div[@class = "flex-row"]//img/@src'
CHAPTERS_TAG = '//table[@class = "table table-hover"]//a/@href|//table[@class = "table table-hover"]//a/text()'
