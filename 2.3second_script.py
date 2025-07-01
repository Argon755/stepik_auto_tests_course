from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
    button1.click()

    Redirect_page = browser.window_handles[1]
    browser.switch_to.window(Redirect_page)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Ваш код, который заполняет обязательные поля 
    input1 = browser.find_element(By.CLASS_NAME, "form-control")
    input1.send_keys(y)


    # Отправляем заполненную форму
    button2 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button2.click()




    # ждем загрузки страницы
    time.sleep(3)

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()