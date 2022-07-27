import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variable
login_url="https://myappventure.herokuapp.com/login"
register_url="https://myappventure.herokuapp.com/registration"

email="zuhalalimulhadi19@gmail.com"
username="zuhalal"
password="abcabc"
wrong_password="abcdabcd"
wrong_email="saddnsds@gmail.com"

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_success_login(self):
        driver = self.driver
        driver.get(login_url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"email").send_keys(email) # isi email
        time.sleep(0.5)
        driver.find_element(By.NAME,"password").send_keys(password) # isi password
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR,"form button[type=submit]").click()
        time.sleep(8)

        # print(driver.current_url)
        self.assertEqual(driver.current_url, 'https://myappventure.herokuapp.com/home')

    def test_wrong_password(self):
        driver = self.driver
        driver.get(login_url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"email").send_keys(email) # isi email
        time.sleep(0.5)
        driver.find_element(By.NAME,"password").send_keys(wrong_password) # isi password
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR,"form button[type=submit]").click()
        time.sleep(8)

        response_data = driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.flex.items-center.justify-center.text-xs.font-semibold.text-\[\#FF8181\].pb-4 > p").text
        # print(response_data)
        self.assertIn(response_data, 'Kata Sandi Salah')

    def test_wrong_email(self):
        driver = self.driver
        driver.get(login_url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"email").send_keys(wrong_email) # isi email
        time.sleep(0.5)
        driver.find_element(By.NAME,"password").send_keys(wrong_password) # isi password
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR,"form button[type=submit]").click()
        time.sleep(8)

        response_data = driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.flex.items-center.justify-center.text-xs.font-semibold.text-\[\#FF8181\].pb-4 > p").text
        # print(response_data)
        self.assertIn(response_data, 'Alamat email atau kata sandi yang\nanda masukan tidak valid')

    def tearDown(self): 
        self.driver.close()

class TestRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_registered_email(self):
        driver = self.driver
        driver.get(register_url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys('abcdefghij')
        time.sleep(0.5)
        driver.find_element(By.NAME, "email").send_keys(email)
        time.sleep(0.5)
        driver.find_element(By.NAME, "password").send_keys("abcdef")
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR,"form button[type=submit]").click()
        time.sleep(8)
        response_data = driver.find_element(By.CSS_SELECTOR,"form div.flex.text-xs.font-semibold > p").text
        self.assertIn(response_data, 'Email atau username sudah terdaftar')
    
    def test_registered_username(self):
        driver = self.driver
        driver.get(register_url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.NAME, "email").send_keys("abcabcabcabc123123@gmail.com")
        time.sleep(0.5)
        driver.find_element(By.NAME, "password").send_keys("abcdef")
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR,"form button[type=submit]").click()
        time.sleep(8)
        response_data = driver.find_element(By.CSS_SELECTOR,"form div.flex.text-xs.font-semibold > p").text
        self.assertIn(response_data, 'Email atau username sudah terdaftar')

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()