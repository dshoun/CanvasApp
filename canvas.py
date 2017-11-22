from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def open_safari():
    # Opens Safari and goes to Canvas.
    driver = webdriver.Safari()  # Change "Safari" to your preferred browser.
    driver.set_window_size(1440, 815)  # Set to preferred window size.
    driver.set_window_position(0, 0)  # Set to preferred window position.
    driver.get("https://usflearn.instructure.com")
    return driver


def login(driver, username, password):
        username_field = driver.find_element_by_id("username")
        username_field.send_keys(username)
        password_field = driver.find_element_by_id("password")
        password_field.send_keys(password)
        login_button = driver.find_element_by_id("btn-submit")
        login_button.click()
        try:
            element = WebDriverWait(driver, 1000).until(
                EC.title_is("User Dashboard")
            )
        finally:
            print("Login successful.")


def find_course(driver):
    print("Enter a Course ID:")
    course_name = input()

    # Goes to the search result page for the desired course.
    driver.get("https://usflearn.instructure.com/accounts/86643/courses?utf8=✓&focus=course_name&course%5Bname%5D=" + course_name)

    # Waits for the search result page to load.
    try:
        element = WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.LINK_TEXT, course_name))
        )
    finally:
        print("Search results loaded.")

    # Finds and clicks on the desired course.
    desired_course = driver.find_element_by_link_text(course_name)
    desired_course.click()
    print("Course found.")


def make_self_teacher(driver, username):
    driver.get(driver.current_url + "/users")
    print("changed url")
    try:
        element = WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.ID, "addUsers"))
        )
    finally:
        print("Users page loaded.")
    add_users_button = driver.find_elements_by_class_name("icon-plus")
    driver.execute_script("$(arguments[0]).click();", add_users_button[1])
    try:
        element = WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.ID, "peoplesearch_radio_unique_id"))
        )
    finally:
        print("Add Users dialog box opened.")
    search_by_id_button = driver.find_element_by_id("peoplesearch_radio_unique_id")
    search_by_id_button.click()
    text_box = driver.find_element_by_class_name("_2ykbfrP b0-oiV6")
    text_box.send_keys("rzimmerman")
    role_choice_list = driver.find_element_by_class_name("_3_H4N-b")
   # role_choice_list = Select(driver.find_element_by_class_name("_3_H4N-b"))
   # role_choice_list.select_by_index(2)
   # driver.execute_script("document.getElementById(" + role_choice_list.get_attribute("id") + ").value = " + "1208")
    driver.execute_script(
        "var select = arguments[0]; for(var i = 0; i < select.options.length; i++){ if(select.options[i].text == arguments[1]){ select.options[i].selected = true; } }",
        role_choice_list, "Teacher");
    time.sleep(60)
    next_button = driver.find_element_by_id("addpeople_next")
    next_button.click()
    time.sleep(3)
    next_button = driver.find_element_by_id("addpeople_next")
    driver.execute_script("$(arguments[0]).click();", next_button)


def find_person(driver):
    print("Enter a name, NetID, or U-Number:")
    person_id = input()
    driver.get("https://usflearn.instructure.com/accounts/86643/users?utf8=✓&focus=user_name&user%5Bname%5D=" + person_id)
    # Waits for the search result page to load.
    try:
        element = WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.CLASS_NAME, "user"))
        )
    finally:
        print("Search results loaded.")

    users_on_page = driver.find_elements_by_class_name("user")
    for user in users_on_page:
        clickable_link = user.find_element_by_tag_name("A")
        clickable_link.click()
        try:
            element = WebDriverWait(driver, 1000).until(
                EC.presence_of_element_located((By.CLASS_NAME, "name"))
            )
        finally:
            print("User page loaded.")
        found_name = driver.find_element_by_class_name("name")
        found_netid = driver.find_element_by_class_name("unique_id")
        found_unumber = driver.find_element_by_class_name("sis_user_id")

        if found_name.text == person_id or found_netid.text == person_id or found_unumber.text == person_id:
            print("User found.")
            break
        else:
            driver.back()
            try:
                element = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "user"))
                )
            finally:
                print("Search results loaded.")
            reloaded_users = driver.find_elements_by_class_name("user")
            users_on_page[users_on_page.index(user) + 1] = reloaded_users[users_on_page.index(user) + 1]
