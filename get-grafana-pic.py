#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
from configparser import ConfigParser
import time


def capture(url_list):
    x = 20
    y = 60
    right = 980
    bottom = 570
    browser = webdriver.Chrome()
    browser.set_window_size(1000, 1800)
    browser.get("https://log.example.com/grafana/login")
    browser.find_element_by_name("username").send_keys("****")
    browser.find_element_by_name("password").send_keys("****")
    browser.find_element_by_xpath(
        "/html/body/grafana-app/div[2]/div/div/div[2]/form/div[3]/button").click()
    browser.execute_script("""
      (function () {
          var y = 0;
          var step = 100;
          window.scroll(0, 0);

          function f() {
              if (y < document.body.scrollHeight) {
                  y += step;
                  window.scroll(0, y);
                  setTimeout(f, 50);
              } else {
                  window.scroll(0, 0);
                  document.title += "scroll-done";
              }
          }

          setTimeout(f, 1000);
      })();
  """)

    for url in list(url_list):
        browser.get(url)
        state = browser.execute_script(
            "return document.readyState") == "complete"
        while not state:
            time.sleep(1)
            state = browser.execute_script(
                "return document.readyState") == "complete"

        time.sleep(2)
        save_fliename = '{0}{1}'.format(url_list.index(url), ".png")
        browser.save_screenshot(save_fliename)
        im = Image.open(save_fliename)
        im = im.crop((x, y, right, bottom))
        im.save(save_fliename)
    browser.close()


if __name__ == "__main__":

    url_list = ["https://log.example.com/grafana/dashboard/db/zhou-bao?panelId=10&fullscreen",
                "https://log.example.com/grafana/dashboard/db/zhou-bao?panelId=3&fullscreen",
                "https://log.example.com/grafana/dashboard/db/zhou-bao?panelId=11&fullscreen",
                "https://log.example.com/grafana/dashboard/db/zhou-bao?panelId=8&fullscreen",
                "https://log.example.com/grafana/dashboard/db/zhou-bao?panelId=7&fullscreen",
                "https://log.example.com/grafana/dashboard/db/zhou-bao?panelId=12&fullscreen",
                "https://log.example.com/grafana/dashboard/db/zhou-bao?panelId=1&fullscreen",
                "https://log.example.com/grafana/dashboard/db/zhou-bao?panelId=9&fullscreen",
                "https://log.example.com/grafana/dashboard/db/zhou-bao?panelId=2&fullscreen",
                "https://log.example.com/grafana/dashboard/db/zhou-bao?panelId=15&fullscreen",
                "https://log.example.com/grafana/dashboard/db/zhou-bao?panelId=16&fullscreen"]

    capture(url_list)
