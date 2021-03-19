import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WechatMoment():
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'

        desired_caps['deviceName'] = '7aaab36a'

        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = '.ui.LauncherUI'

        desired_caps['noReset'] = 'True'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.wait = WebDriverWait(self.driver, 30)

        print('启动微信...')

    def findUserMoments(self, user_id):
        search_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/f8y')))
        time.sleep(1)
        search_button.click()
        print('点击搜索框...')

        search_edit_text = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/bhn')))
        search_edit_text.send_keys(user_id)
        print('搜索用户...', user_id)

        user_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/tm')))
        user_button.click()
        print('点击用户头像...')
        
        chat_content_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/cj')))
        chat_content_button.click()
        print('进入聊天详情页...')

        user_profile_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/f3y')))
        user_profile_button.click()
        print('点击头像...')

        moment_entry = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/ja')))
        moment_entry.click()
        print('进入朋友圈...')

    def catch_moments(self):
        items = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'com.tencent.mm:id/fol')))
        print('swiping')
        self.driver.swipe(300,800,300,300,15000)
        print('swipe end')
        print(len(items))
        print(items)
        for item in items:
            print(item)
            moment_text=item.find_element_by_id('com.tencent.mm:id/b_l').text
            print(moment_text)

def main():
    moment = WechatMoment()
    moment.findUserMoments('wondermomo001')
    moment.catch_moments()


if __name__ == '__main__':
  main()