一、编程题
https://iftp.chinamoney.com.cn/english/bdInfo/
1. 从链接页面获取公开数据
2. 需要获取数据的条件: Bond Type=Treasury Bond, Issue Year=2023
3. 解析返回表格数据，列名包括ISIN, Bond Code, Issuer, Bond Type, Issue Date, Latest Rating
3. 保存成有效csv文件，
二、编程题：
一个代码列表长度500，要求以80个为一个批次，拆分成多个数组打印输出，测试数据来源：https://edidata.oss-cn-beijing.aliyuncs.com/fyx_chinamoney.csv
可以下载到本地用做测试数据

# Question1 是第一个编程题的解决方案，因为该网站的表格并不是通过POST请求来渲染，所以我使用了浏览器驱动Selenium来模拟浏览器行为，选择获取数据的条件，然后点击Search按钮。但因选择元素处ID出了莫名的问题，没有进行到最后一步。

# Question2 是第二个编程题的解决方案，通过简单遍历进行了解决。

# 到岗时间: 随时可以到岗            
# 测试时间: 14：55——16：35
