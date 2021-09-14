from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fpdf import FPDF

options = Options()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)

browser.get("https://palewebserial.wordpress.com/2020/05/05/blood-run-cold-0-0/")

pdf = FPDF()
pdf.add_page()

while True:
    title = browser.find_element_by_class_name("entry-title").text
    main_text = browser.find_element_by_class_name("entry-content").text

    main_text = main_text.replace("Previous Chapter", "").replace("Next Chapter", "")
    head, sep, tail = main_text.partition("SHARE THIS")

    txt = head.encode("latin-1", "ignore").decode("latin-1")
    title = title.encode("latin-1", "ignore").decode("latin-1")

    pdf.set_xy(10.0, 10.0)
    pdf.set_font("Arial", "B", 20)
    pdf.cell(40, 10, title)

    pdf.set_xy(10.0, 30.0)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 7, txt)

    # clicks next chapter until the last chapter is reached
    try:
        browser.find_element_by_link_text("Next Chapter").click()
    except NoSuchElementException:
        break

    pdf.add_page()

# outputs text to a PDF
pdf.output("Pale Webserial.pdf")
browser.quit()
