from weasyprint import HTML, CSS
from bs4 import BeautifulSoup




def combine_html_css(html, css_file_path):
    with open(css_file_path, 'r', encoding='utf-8') as css_file:
        css_content = css_file.read()

    css_tag = f"<style>\n{css_content}\n</style>"
    head_pos = html.find('</head>')
    if head_pos != -1:
        combined_html = html[:head_pos] + css_tag + html[head_pos:]
    else:
        combined_html = html + css_tag
    return combined_html


def convert_html_to_pdf(html_string, pdf_path):
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)

    return not pisa_status.err


def remove_section(html_string, section_id):
    soup = BeautifulSoup(html_string, 'html.parser')
    section_to_remove = soup.find(id=section_id)
    if section_to_remove:
        section_to_remove.decompose()
    return str(soup)


def remove_class(html_string, class_name):
    soup = BeautifulSoup(html_string, 'html.parser')
    elements_to_remove = soup.find_all(class_=class_name)
    for element in elements_to_remove:
        element.decompose()
    return str(soup)


def remove_specific_tag(html_string, tag, attributes):
    soup = BeautifulSoup(html_string, 'html.parser')
    tag_to_remove = soup.find(tag, attrs=attributes)
    if tag_to_remove:
        tag_to_remove.decompose()
    return str(soup)


def convert_to_local_copy():
    with open('../src/resume.html', 'r') as f:
        html_string = f.read()
    html_local = remove_section(html_string, 'personal_projects')
    html_local = remove_class(html_local, 'counter_st')

    attributes = {
        "download": "messer_chris_resume.pdf",
        "href": "https://s3.amazonaws.com/chrislmesser.com/messer_chris_resume.pdf"}

    html_local = remove_specific_tag(html_local, 'a', attributes)
    # with open('../src/resume_local.html', 'w', encoding='utf-8') as file:
    #     file.write(html_local)
    # stylized_html = combine_html_css(html_local, '../src/mystyle.css')
    # convert_html_to_pdf(stylized_html, '../src/resume_local.pdf')
    import os

    os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

    HTML(string=html_local).write_pdf(target='../src/resume_local.pdf', stylesheets=[CSS('../src/mystyle.css')])