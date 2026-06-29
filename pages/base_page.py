from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)
    
    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)
    
    def wait_element_is_visible(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return True

    def wait_elements_is_visible(self, locator):
        return self.wait.until(expected_conditions.visibility_of_all_elements_located(locator))

    def wait_element_invisible_or_not_present(self, locator, time=20):
        self.wait.until(expected_conditions.invisibility_of_element_located(locator))
        return True
        
    def wait_element_until_invisibility(self, locator, time=20):
        WebDriverWait(self.driver, time).until_not(expected_conditions.text_to_be_present_in_element(locator, '9999'))
        return True

    def get_order_number(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        order_number = self.get_text_from_element(locator)
        return order_number

    def click_to_element(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()
    
    def click_to_element_perform(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        return element
    
    def click_to_element_js(self, locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)
        return self
    
    def wait_text(self, locator, text):
        self.wait.until_not(expected_conditions.text_to_be_present_in_element_value(locator, text))
        return self.driver.find_element(*locator).text

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
    
    def format_locators(self, locator_tuple, **kwargs):
        method, template = locator_tuple
        formatted_xpath = template.format(**kwargs)
        return (method, formatted_xpath)

    def switch_to_another_window(self):
        windows_list = self.driver.window_handles
        self.driver.switch_to.window(windows_list[-1])

    def scroll_to_element(self, locator):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_virt_mouse(self, locator): # виртуальный клик помогает убрать невидимый элемент, который мешает действию
        action = ActionChains(self.driver)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        action.click(on_element=element).perform()

    def drag_and_drop_element(self, locator_from, locator_to):
        self.wait_element_is_visible(locator_from)
        self.wait_element_is_visible(locator_to)
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        self.driver.execute_script("""var source = arguments[0]; var target = arguments[1]; var evt = document.createEvent("DragEvent");
        evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        source.dispatchEvent(evt); evt = document.createEvent("DragEvent");                 
        evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        target.dispatchEvent(evt); evt = document.createEvent("DragEvent");
        evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        target.dispatchEvent(evt); evt = document.createEvent("DragEvent");
        evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        target.dispatchEvent(evt); evt = document.createEvent("DragEvent");
        evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        source.dispatchEvent(evt);
        """, element_from, element_to)
