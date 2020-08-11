from selenium import webdriver


def get_dam_data():
    url = 'https://www.napocor.gov.ph/index.php/services/dmd/dams-status/'
    driver = webdriver.Firefox()
    driver.get(url)

    with open('dams.csv', 'w') as fp:
        fp.write('DAM NAME,CURRENT,PREVIOUS\n')
        for num in range(8):
            dam1 = driver.find_element_by_xpath(f"//table/tbody/tr[{2+(num*5)}]")
            name = dam1.find_element_by_xpath("./td[1]").text.split('\n')[0]
            current = dam1.find_element_by_xpath("./td[4]").text
            previous = dam1.find_element_by_xpath("./td[5]").text
            fp.write(f'{name},{current},{previous}\n')
    driver.close()


if __name__ == "__main__":
    get_dam_data()
