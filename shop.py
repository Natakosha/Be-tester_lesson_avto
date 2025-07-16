import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

popUp =  WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[aria-label="Do not consent"]')))
if popUp:
    popUp[0].click()
else:
    pass
Acc = driver.find_element_by_css_selector('#menu-item-50')
Acc.click()
email = driver.find_element_by_css_selector('#username')
email.send_keys("email@milo.com")
passw = driver.find_element_by_css_selector('#password')
passw.send_keys("5I89Ytrew32!Jo")
time.sleep(5)
login = driver.find_element_by_css_selector('[name="login"]')
login.click()
time.sleep(2)

shop = driver.find_element_by_css_selector('#menu-item-40')
shop.click()
book = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/product/html5-forms/"]')
book.click()

element = driver.find_element_by_css_selector('.product_title.entry-title')
element_get_text = element.text
assert element_get_text == "HTML5 Forms"
print('Проверка первого блока.')
print('   Заголовок книги называеться:',element_get_text)
time.sleep(5)
driver.close()

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

popUp =  WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[aria-label="Do not consent"]')))
if popUp:
    popUp[0].click()
else:
    pass

Acc = driver.find_element_by_css_selector('#menu-item-50')
Acc.click()
email = driver.find_element_by_css_selector('#username')
email.send_keys("email@milo.com")
passw = driver.find_element_by_css_selector('#password')
passw.send_keys("5I89Ytrew32!Jo")
time.sleep(5)
login = driver.find_element_by_css_selector('[name="login"]')
login.click()
time.sleep(2)

shop = driver.find_element_by_css_selector('#menu-item-40')
shop.click()
html = driver.find_element_by_css_selector('.product-categories > li:nth-child(2)>a')
html.click()

basket = driver.find_elements_by_css_selector('[rel=nofollow]')
assert len(basket) == 3
print('Проверка второго блока.')
print('   На странице отображаеться:',len(basket),'элемента')
time.sleep(5)
driver.close()

from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

popUp =  WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[aria-label="Do not consent"]')))
if popUp:
    popUp[0].click()
else:
    pass

driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
# Login
Acc = driver.find_element_by_id('menu-item-50')
Acc.click()
email = driver.find_element_by_id('username')
email.send_keys("email@milo.com")
passw = driver.find_element_by_id('password')
passw.send_keys("5I89Ytrew32!Jo")
time.sleep(2)
login = driver.find_element_by_css_selector('[name="login"]')
login.click()
time.sleep(1)

shop = driver.find_element_by_id('menu-item-40')
shop.click()

element = driver.find_element_by_tag_name("select")
select = Select(element)
so = select.first_selected_option
assert "Default sorting" in so.text
print('Проверки третьего блока.')
print('   В списке выбран вариант =',so.text)

element = driver.find_element_by_tag_name("select")
select = Select(element)
select.select_by_value("price-desc")

element = driver.find_element_by_tag_name("select")
select = Select(element)
sp = select.first_selected_option
assert "Sort by price: high to low" in sp.text
print('   В списке выбран вариант =',sp.text)
time.sleep(2)
driver.close()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

popUp =  WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[aria-label="Do not consent"]')))
if popUp:
    popUp[0].click()
else:
    pass

Acc = driver.find_element_by_id('menu-item-50')
Acc.click()
email = driver.find_element_by_id('username')
email.send_keys("email@milo.com")
passw = driver.find_element_by_id('password')
passw.send_keys("5I89Ytrew32!Jo")
time.sleep(2)
login = driver.find_element_by_css_selector('[name="login"]')
login.click()
time.sleep(1)

shop = driver.find_element_by_id('menu-item-40')
shop.click()
android = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/product/android-quick-start-guide/"]')
android.click()

prises = driver.find_elements_by_css_selector('.woocommerce-Price-amount.amount')
prises_0 = prises[0].text
prises_1 = prises[1].text
print('Проверки четвертого блока.')
print('   Старая цена = ',prises_0)
print('   Новая цена =', prises_1)
assert prises_0 == "₹600.00"
assert prises_1 == "₹450.00"

time.sleep(2)
Img_open = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'woocommerce-main-image.zoom')))
Img_open.click()
time.sleep(2)
Img_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
Img_close.click()
time.sleep(2)
driver.close()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(1)

driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

popUp =  WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[aria-label="Do not consent"]')))
if popUp:
    popUp[0].click()
else:
    pass

shop = driver.find_element_by_id('menu-item-40')
shop.click()
add_card = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]')
add_card.click()

time.sleep(1)
card_item = driver.find_element_by_css_selector('#wpmenucartli > a> span.cartcontents')
card_item_text = card_item.text
print('Проверки пятого блока.')
print('   Кол-во товара в корзине:',card_item_text)
assert card_item_text == "1 Item"

time.sleep(1)
card_price = driver.find_element_by_css_selector('#wpmenucartli > a> span.amount')
card_price_text = card_price.text
print('   Цена:',card_price_text)
assert card_price_text == "₹180.00"

go_card = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/basket/"]')
go_card.click()

price_v = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal"), "₹180.00"))
price_t = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total"), "₹183.60"))
time.sleep(2)
driver.close()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(1)

driver.maximize_window()
driver.get("https://practice.automationtesting.in/")


popUp =  WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[aria-label="Do not consent"]')))
if popUp:
    popUp[0].click()
else:
    pass

shop = driver.find_element_by_id('menu-item-40')
shop.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 300);")
add_card_0 = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]')
add_card_0.click()
time.sleep(2)
add_card_1= driver.find_element_by_css_selector('[href="/shop/?add-to-cart=180"]')
add_card_1.click()
time.sleep(2)

go_card = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/basket/"]')
go_card.click()
time.sleep(5)
del_book = driver.find_element_by_css_selector('#page-34 > div > div >form > table >tbody >tr:nth-child(1) >td >a.remove')
del_book.click()
time.sleep(2)
undo = driver.find_element_by_link_text('Undo?')
undo.click()

quantity = driver.find_elements_by_css_selector('tbody >tr.cart_item >td:nth-child(5) >div.quantity > input.input-text.qty.text')
quantity[0].clear()
quantity[0].send_keys("3")

time.sleep(2)
Update_b = driver.find_element_by_css_selector('[name=update_cart]')
Update_b.click()
value_item = quantity[0].get_attribute('value')
print('Проверки шестого блока.')
print('   Value элемента quantity для "JS Data Structures and Algorithm"=',value_item)
assert value_item == '3'
time.sleep(2)
Cupon = driver.find_element_by_css_selector('[name="apply_coupon"]')
Cupon.click()
time.sleep(2)

Cupon_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "ul.woocommerce-error"), "Please enter a coupon code."))
if Cupon_check:
    print('   Надпись "Please enter a coupon code." появилась.')
else:
    print('   Надписи "Please enter a coupon code." НЕТ.')

time.sleep(2)
driver.close()

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(1)

driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

popUp =  WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[aria-label="Do not consent"]')))
if popUp:
    popUp[0].click()
else:
    pass

shop = driver.find_element_by_id('menu-item-40')
shop.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 300);")
add_card_1 = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]')
add_card_1.click()
time.sleep(2)

go_card = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/basket/"]')
go_card.click()
time.sleep(3)

checkout = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'checkout-button.button.alt.wc-forward')))
checkout.click()
time.sleep(3)

billing_first_name = WebDriverWait(driver, 5).until_not(EC.invisibility_of_element_located((By.ID, "billing_first_name")))
billing_first_name = driver.find_element_by_id('billing_first_name')
billing_first_name.send_keys("Natali")

billing_last_name = driver.find_element_by_id('billing_last_name')
billing_last_name.send_keys("Pupkovna")

billing_email = driver.find_element_by_id('billing_email')
billing_email.send_keys("email@milo.com")

billing_phone = driver.find_element_by_id('billing_phone')
billing_phone.send_keys("+789631410")

time.sleep(2)
contry_pole = driver.find_element_by_id('s2id_billing_country')
contry_pole.click()
contry_vvod = driver.find_element_by_id('s2id_autogen1_search')
contry_vvod.send_keys('Russia')
time.sleep(1)
contry_vvod.send_keys(Keys.RETURN)
time.sleep(2)

adress = driver.find_element_by_id('billing_address_1')
adress.send_keys("Ul. Talsinskaja")
sity = driver.find_element_by_id('billing_city')
sity.send_keys("Moscow")
oblast = driver.find_element_by_id('billing_state')
oblast.send_keys("Moscow region")
zip = driver.find_element_by_id('billing_postcode')
zip.send_keys("141100")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 600);")
check = driver.find_element_by_id('payment_method_cheque')
check.click()
place_order = driver.find_element_by_id('place_order')
place_order.click()

TY = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
CP = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "table.shop_table.order_details > tfoot >tr:nth-child(3) > td"), "Check Payments"))
ty = driver.find_element_by_css_selector("p.woocommerce-thankyou-order-received")
cp = driver.find_element_by_css_selector("table.shop_table.order_details > tfoot >tr:nth-child(3) > td")
ty_text = ty.text
cp_text = cp.text
print('Проверки седьмого блока.')
print(f'   Должна отображается надпись "Thank you. Your order has been received." Отображается= "{ty_text}"')
print(f'   Должна отображается надпись "Check Payments." Отображается= "{cp_text}"')
print('')
print('Конец скрипта.')

driver.execute_script("alert('Скрипт выполнен успешно! Домашнее задание 4-го урока выполнено!!');")
driver.quit()













