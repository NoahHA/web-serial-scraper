from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fpdf import FPDF

# start maximized makes sure everything on the page is visible
options = Options()
options.add_argument("--start-maximized")

# creates an empty PDF file
pdf = FPDF()
pdf.add_page()

num_chapters = 109

for i in range(num_chapters):

    browser = webdriver.Chrome(options=options)

    url = f"https://www.fictionpress.com/s/2961893/{i}/Mother-of-Learning"
    browser.get(url)

    main_text = browser.find_element_by_id("storytextp").text
    txt = main_text.encode("latin-1", "ignore").decode("latin-1")

    pdf.set_xy(10.0, 30.0)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 7, txt)

    pdf.add_page()
    browser.quit()

pdf.output("Mother of Learning.pdf")
