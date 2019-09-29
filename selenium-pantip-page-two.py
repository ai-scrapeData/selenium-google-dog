import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

import json
# import bson

import pymongo
from pymongo import MongoClient
uri = "mongodb://heroku_3lsf2k6l:acj9qbdfmvd8j2ub1ek7nc8ac1@ds023523.mlab.com:23523/heroku_3lsf2k6l"
# from time import time, mktime
# timeStart = time()
client = MongoClient(uri)
db = client["heroku_3lsf2k6l"]
collections = db['comment']


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        # 38168956
        driver.get("https://pantip.com/topic/38168956")
        count_seemore = driver.find_elements_by_class_name("reply.see-more")
        for i in range(len(count_seemore)):
            element = driver.find_element_by_class_name('reply.see-more')
            driver.execute_script("arguments[0].click();", element)
        header = driver.find_elements_by_class_name("display-post-title")[0].text
        print('header',header)
        hash_tags = driver.find_elements_by_class_name("tag-item.cs-tag_topic_title")
        list_hash_tag = [hash_tag.text for hash_tag in hash_tags]
        comment = driver.find_elements_by_class_name("display-post-story")
        like_score = driver.find_elements_by_class_name("like-score")
        emoji_score = driver.find_elements_by_class_name("emotion-score")
        date_time = driver.find_elements_by_class_name("timeago")
        number_comment = driver.find_elements_by_class_name("display-post-number")
        edit_time = driver.find_elements_by_class_name("display-post-timestamp.timeago")

        list_edit_time = [edit_time[i].text for i in range(len(edit_time))]

        list_date_time = [date_time[i].text for i in range(len(date_time)) if date_time[i].text not in list_edit_time]

        list_number_comment = ['ความคิดเห็นที่ 0']
        for i in range(len(number_comment)):
            list_number_comment.append(number_comment[i].text)

        for i in range(len(like_score)):
            print('--------------------------------------------')
            number_comment_text = list_number_comment[i]
            description_comment = " ".join(comment[i].text.split())
            like_comment = like_score[i].text
            emoji_comment = emoji_score[i].text
            date_time_comment_normal = list_date_time[i].split(' น.')[0]

            day = date_time_comment_normal.split(' ')[0]
            month = date_time_comment_normal.split(' ')[1]
            dict_month = {
                "มกราคม": "01",
                "กุมภาพันธ์":"02",
                "มีนาคม":"03",
                "เมษายน":"04",
                "พฤษภาคม":"05",
                "มิถุนายน":"06",
                "กรกฎาคม":"07",
                "สิงหาคม":"08",
                "กันยายน":"09",
                "ตุลาคม":"10",
                "พฤศจิกายน":"11",
                "ธันวาคม":"12"
            }
            year = str(int(date_time_comment_normal.split(' ')[2]) - 543)
            hour = date_time_comment_normal.split(' ')[4].split(':')[0]
            minute = date_time_comment_normal.split(' ')[4].split(':')[1]
            date_time_comment_string = f'{minute}/{hour}/{day}/{dict_month[f"{month}"]}/{year}'
            date_time_comment_timestamp = time.mktime(datetime.datetime.strptime(date_time_comment_string, "%M/%H/%d/%m/%Y").timetuple())

            print('minute',minute)
            print('hour',hour)
            print('day',day)
            print('month',dict_month[f'{month}'])
            print('year',year)
            print('date_time_comment_string',date_time_comment_string)
            print('date_time_comment_timestamp',date_time_comment_timestamp)
            print('--------------------------------------------')
        

            dict_comment = {
                'header':header,
                'list_hash_tag':list_hash_tag,
                'number_comment_text':number_comment_text,
                'description_comment':description_comment,
                'like_comment':like_comment,
                'emoji_comment':emoji_comment,
                'minute':minute,
                'hour':hour,
                'day':day,
                'month':dict_month[f"{month}"],
                'year':year,
                'date_time_comment_string':date_time_comment_string,
                'date_time_comment_timestamp':date_time_comment_timestamp
            }
            # try:
            allData = {'MacthID':date_time_comment_timestamp,'api': dict_comment}
            query = {"MacthID":date_time_comment_timestamp}
            result = collections.find(query, {'_id': False})
            print('result_count:', result.count())
            if result.count() == 0:
                print('Not found. inserting')
                print('All Data', allData)
                collections.insert_one(allData)
            else:
                collections.replace_one(query, allData)
                print('Updated completed!')
            # except:
            #     print('error try catch')
if __name__ == "__main__":
    unittest.main()
    # [i].get_property("href")