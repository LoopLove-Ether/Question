from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd

# 创建一个新的浏览器实例
driver = webdriver.Firefox()

# 打开给定的URL
driver.get('https://iftp.chinamoney.com.cn/english/bdInfo/')

#TODO:抱歉，find_element_by_id 因莫名原因找不到元素对象，无法进行到最后一步

# 找到Bond Type的下拉菜单，并选择"Treasury Bond"
bond_type = Select(driver.find_element_by_id('Bond_Type_select'))
bond_type.select_by_visible_text('Treasury Bond')

# 找到Issue Year的下拉菜单，并选择"2023"
issue_year = Select(driver.find_element_by_id('Issue_Year_select'))
issue_year.select_by_visible_text('2023')

# 点击"Search"按钮
search_button = driver.find('a', attrs={'onclick': "searchData()"})
search_button.click()

# 等待页面加载完毕
driver.implicitly_wait(3)

# 解析表格数据
table = driver.find('table', attrs={'class': 'san-sheet-alternating'})
rows = table.find_elements_by_tag_name('tr')

data = []
for row in rows:
    cols = row.find_elements_by_tag_name('td')
    cols = [ele.text for ele in cols]
    data.append([ele for ele in cols if ele])

# 转换数据为dataframe并保存为csv文件
df = pd.DataFrame(data, columns=['ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating'])
df.to_csv('bond_data.csv', index=False)

# 关闭浏览器实例
driver.quit()