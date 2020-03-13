# Capybara

> Source: http://www.rubydoc.info/github/teamcapybara/capybara/master

> Aliases: 

$ Navigating
    `visit('/projects')            {{Navigate to a path}} 
    `page.current_path             {{Get current page path}} 
    `page.current_url              {{Get current page url}} 
    `have_current_path('/projects')
>                                  {{Check current path matches a value}} 

$ Clicking Links and Buttons
    `click_link('id-of-link')      {{Click link with a given ID}} 
    `click_link('Link Text')       {{Click link containing some text}} 
    `click_button('Save')          {{Click button containing some text}} 
    `click_on('Link Text')         {{Click on either link or button containing some text}} 

$ Interacting with Forms
    `fill_in('input_name', with: 'text for the input')
>                                  {{Fill input with text}} 
    `choose('A Radio Button')      {{Choose radio button with a given name}} 
    `check('A Checkbox')           {{Check box with a given name}} 
    `uncheck('A Checkbox')         {{Uncheck box with a given name}} 
    `select('Option', from: 'Select Box')
>                                  {{Select option within select box}} 

$ Querying
    `page.has_selector?('table tr')
>                                  {{Check page has selector}} 
    `page.has_xpath?(''.//table/tr'')
>                                  {{Check page has xpath}} 
    `page.has_css?('table tr.foo') {{Check page has css}} 
    `page.have_field('field_name') {{Check page has field with a given name}} 

$ Finding
    `find_field('Field Name')      {{Find field with a given name}} 
    `find_button(id: 'my_button')  {{Find button with a given ID}} 
    `find_link('Send')             {{Find link with given text}} 
    `find(:xpath, './/table/tr')   {{Find element by xpath}} 

