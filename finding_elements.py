from selenium import webdriver

class FindByID():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementbyID = driver.find_element_by_id("name")
        if elementbyID is not None:
            print("Found")

if __name__ == "__main__":
    find = FindByID()
    find.test()