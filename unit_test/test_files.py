import os
import time
import tempfile
import unittest

import http.client as httplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

upload_url = 'https://the-internet.herokuapp.com/upload'
download_url = 'http://the-internet.herokuapp.com/download'
br_url_down = 'https://www.browserstack.com/test-on-the-right-mobile-devices'
plagiarism_checker = 'https://smallseotools.com/plagiarism-checker/'

# test file uploading and downloading
# problem that dialog box is out of reach fo Selenium
# TODO - add test from browserStack upload and download
# TODO - add check file's hash ?
# TODO - something else for file manipulation? (check sweord?)


class TestFilesManipulation(unittest.TestCase):
    def setUp(self) -> None:
        # initialisation
        # print('SetUp test')
        #service = Service(ChromeDriverManager().install())
        #self.driver = webdriver.Chrome(service=service)
        #self.driver.set_window_size(1024, 768)

        options = Options()
        # prefs = {"download.default_directory" : "<directory_path>
        prefs = {"download.default_directory": "/Users/okamene/src/QA_python_camp/files"}
        options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1024, 768)

        #self.download_dir = tempfile.mkdtemp()

    def test_file_downloading1(self):
        """
            simple way to download file
        :return:
        """
        browser = self.driver
        url = download_url
        browser.get(url)

        download_link = browser.find_element(By.CSS_SELECTOR, '.example a')
        download_link.click()
        time.sleep(2)

        self.download_dir = "/Users/okamene/src/QA_python_camp/files"
        files = os.listdir(self.download_dir)
        files = [os.path.join(self.download_dir, f)
                 for f in files]
        assert len(files) > 0, "no files were downloaded"
        assert os.path.getsize(files[0]) > 0, "downloaded file was empty"

    def test_file_downloading2(self):
        """
            Check header for content type and length
        :return:
        """
        browser = self.driver
        url = download_url
        browser.get(url)

        download_link = browser.find_element(By.CSS_SELECTOR, '.example a').get_attribute('href')

        connection = httplib.HTTPConnection('the-internet.herokuapp.com')
        connection.request('HEAD', download_link)
        response = connection.getresponse()
        content_type = response.getheader('Content-type')
        content_length = response.getheader('Content-length')
        time.sleep(1)
        # assert content_type == 'application/octet-stream'
        assert content_type == 'image/jpeg'
        assert int(content_length) > 0

    def test_file_downloading3(self):
        """
            another way to test from browserStack
        :return:
        """
        browser = self.driver
        url = br_url_down

        try:
            browser.get(url)
            gotit = browser.find_element(By.ID, 'accept-cookie-notification')
            gotit.click()
            downloadcsv = browser.find_element(By.CSS_SELECTOR, '.icon-csv')
            #downloadcsv = browser.find_element(By.CSS_SELECTOR, '.icon-pdf')
            downloadcsv.click()
            time.sleep(5)
            browser.close()
        except:
            print("Invalid URL")

    def test_file_uploading1(self):
        """
            A work-around for this problem is to side-step the system dialog box
             entirely. Selenium inserts the full path of the file we want to upload
              (as text) into the form and then submit the form.
        :return:
        """
        browser = self.driver
        url = upload_url
        browser.get(url)

        file_root = '/Users/okamene/src/QA_python_camp/files'
        filename = 'some-file.txt'
        filepath = f"{file_root}/{filename}"
        #file = os.path.join(os.getcwd(), filepath)

        browser.find_element(By.ID, 'file-upload').send_keys(filepath)
        browser.find_element(By.ID, 'file-submit').click()
        time.sleep(2)

        uploaded_file = browser.find_element(By.ID, 'uploaded-files').text
        assert uploaded_file == filename, "uploaded file should be %s" % filename

    def test_file_uploading2(self):
        """
        this test killing my PC. Don't run it anymore.
        :return:
        """
        browser = self.driver
        url = plagiarism_checker
        browser.get(url)

        file_root = '/Users/okamene/src/QA_python_camp/files'
        filename = 'some-file.txt'
        filepath = f"{file_root}/{filename}"
        file = os.path.join(os.getcwd(), filepath)
        # accept cookie notification
        #gotit = browser.find_element(By.XPATH, '//a[@class="cb-enable" and text()="Accept"]')
        gotit = browser.find_element(By.CLASS_NAME, 'cb-enable')
        gotit.click()
        time.sleep(1)

        #browser.find_element(By.linkText("Upload a Document:( .tex, .txt, .doc, .docx, .odt, .pdf, .rtf )")).send_keys(file)
        browser.find_element(By.ID, 'fileUpload').send_keys(file)
        browser.find_element(By.ID, 'file-submit').click()
        time.sleep(2)

        textarea = browser.find_element(By.ID, 'textbox').text
        assert textarea == filename, "uploaded file should be %s" % filename

    def tearDown(self) -> None:
        # destroy driver instance
        print('Destroy driver')
        self.driver.quit()
