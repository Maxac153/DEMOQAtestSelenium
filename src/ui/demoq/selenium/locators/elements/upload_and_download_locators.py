from selenium.webdriver.common.by import By


class UploadAndDownloadLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_RESULT = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')

    DOWNLOAD_FILE = (By.CSS_SELECTOR, 'a[id="downloadButton"]')