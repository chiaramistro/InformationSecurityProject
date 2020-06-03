import mechanize

def my_compiler_function(row):
    br = mechanize.Browser()
    # print("Hello world!" + row[0] + " - " + row[1])
    # Ignore robots.txt
    br.set_handle_robots(False)
    # Set a legit user agent
    br.addHeaders = [('User-agent', 'Firefox')]

    # Retrieve the Google home page, saving the response
    br.open("http://127.0.0.1/wp53/my-form-page/")

    print(br.title())

    # Select the search box and search for 'foo'
    forms = br.forms()
    myid = forms[1].attrs["id"]
    if myid == "wpmtst-submission-form":
        print("WIN")
        br.select_form(nr=1)
        print(br.form)
        br.form['client_name'] = row[0]
        br.form['email'] = row[1]
        br.form['company_name'] = row[2]
        br.form['company_website'] = row[3]
        br.form['post_title'] = row[4]
        br.form['post_content'] = row[5]
        print(br.form)

        # Get the search results
        response1 = br.submit()
        print(br.form)