# Selenium WebDriver

> Source: http://docs.seleniumhq.org/docs/

> Aliases: seleniumhq, selenium-webdriver, seleniumhq-python, python-selenium, selenium-python, selenium-webdriver-python

$ Installing Selenium WebDriver
    `pip install -U selenium       {{Install or upgrade the Python bindings for Selenium WebDriver}} 

$ Open a browser go to a specified URL
    `from selenium import webdriver 

 browser = webdriver.Firefox() 
 browser.get('http://seleniumhq.org/')
>                                  {{Open a new Firefox browser and load the page at the given URL}} 

$ Navigating
    `driver.switch_to_window('windowName')
>                                  {{Selenium WebDriver supports moving between named windows using the “switch_to_window” method}} 
    `driver.switch_to_frame('frameName')
>                                  {{You can also swing from frame to frame (or into iframes)}} 
    `driver.switch_to_default_content()
>                                  {{Once we are done with working on frames, we will have to come back to the parent frame}} 
    `alert = driver.switch_to_alert()
>                                  {{This will return the currently open alert object. With this object you can now accept, dismiss, read its contents or even type into a prompt}} 
    `driver.get('http://www.example.com') 

driver.forward() 
 driver.back()
>                                  {{To move backwards and forwards in your browser’s history}} 

$ Waits
    `try:
element = WebDriverWait(driver, 10).until(
EC.presence_of_element_by_id('Form')
)
finally:
driver.quit()
>                                  {{An explicit wait is code you define to wait for a certain condition to occur before proceeding further in the code}} 
    `driver.implicitly_wait(10) # seconds
>                                  {{An implicit wait is to tell WebDriver to poll the DOM for a certain amount of time when trying to find an element or elements if they are not immediately available}} 

$ Locating Elements
    `driver.getTitle()             {{Get page title in Selenium WebDriver}} 
    `driver.getCurrentUrl()        {{Get Current Page URL In Selenium WebDriver}} 
    `form = driver.find_element_by_id('Form')
>                                  {{Use this when you know id attribute of an element. With this strategy, the first element with the id attribute value matching the location will be returned}} 
    `email = driver.find_element_by_name('email')
>                                  {{Use this when you know name attribute of an element. With this strategy, the first element with the name attribute value matching the location will be returned}} 
    `form = driver.find_element_by_xpath('//form[1]')
>                                  {{XPath is the language used for locating nodes in an XML document. One of the main reasons for using XPath is when you don’t have a suitable id or name attribute for the element you wish to locate}} 
    `link = driver.find_element_by_link_text('Continue')
>                                  {{Use this when you know link text used within an anchor tag. With this strategy, the first element with the link text value matching the location will be returned}} 
    `heading = driver.find_element_by_tag_name('h1')
>                                  {{Use this when you want to locate an element by tag name. With this strategy, the first element with the given tag name will be returned}} 
    `content = driver.find_element_by_css_selector('p.content')
>                                  {{Use this when you want to locate an element by CSS selector syntax. With this strategy, the first element with the matching CSS selector will be returned}} 

$ Element's operation
    `driver.find_element_by_id('submitButton').click()
>                                  {{Clicking on any element or button of webpage}} 
    `dropdown = driver.find_element_by_tag_name('select').getText()
>                                  {{Store text of targeted element in variable}} 
    `driver.find_element_by_name('fname').sendKeys('My First Name')
>                                  {{Typing text in text box or text area}} 
    `Boolean ispresent = driver.find_element_by_xpath('//input[@id='text2']').size()!= 0
>                                  {{Verify Element Present in Selenium WebDriver}} 

$ Cookies
    `# Go to the correct domain
driver.get('http://www.example.com')

# Now set the cookie. This one's valid for the entire domain
cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’}
driver.add_cookie(cookie)

# And now output all the available cookies for the current URL
driver.get_cookies()
>                                  {{First of all, you need to be on the domain that the cookie will be valid for}} 

