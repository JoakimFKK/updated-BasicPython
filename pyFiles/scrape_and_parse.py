from urllib.request import urlopen

def first_ex():
    url = "http://olympus.realpython.org/profiles/aphrodite"
    ### Getting everything
    html_page = urlopen(url)
    html_text = html_page.read().decode("utf-8")
    print(html_text)


# ### Example
def second_ex():
    url = "http://olympus.realpython.org/profiles/poseidon"

    ### Getting text within <title> og </title>
    page = urlopen(url)
    html = page.read().decode('utf-8')

    start_tag = "<title>"
    end_tag = "</title>"

    start_index = html.find(start_tag) + len(start_tag)
    end_index = html.find(end_tag)

    print(html[start_index:end_index])