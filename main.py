from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import canvas
import interface

driver = canvas.open_safari()

username = interface.get_username()
password = interface.get_password(username)
canvas.login(driver, username, password)

primary_input = 0
while primary_input != 666:
    primary_input = interface.main_menu()

    if primary_input == "1":
        canvas.find_course(driver)
        secondary_input = interface.course_sub_menu()
        if secondary_input == "1":
            canvas.make_self_teacher(driver, username)
        if secondary_input == 666:
            primary_input = interface.main_menu()
    if primary_input == "2":
        canvas.find_person(driver)
        #secondary_input = interface.person_sub_menu()


driver.find