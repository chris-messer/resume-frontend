import pytest

def test_remove_section():
    from src.convert_to_pdf import remove_section
    html = '<div id="header">Header</div><div id="content">Content</div>'
    transformed_html = remove_section(html, 'content')
    target_html = '<div id="header">Header</div>'
    assert transformed_html == target_html


def test_remove_class():
    from src.convert_to_pdf import remove_class
    html = '<div class="info">Info</div><dt class="counter_st"></dt><div class="info">Another Element</div>'
    transformed_html = remove_class(html, 'counter_st')
    target_html = '<div class="info">Info</div><div class="info">Another Element</div>'
    assert transformed_html == target_html

# def test_create_local():
#     from src.convert_to_pdf import convert_to_local_copy
#     convert_to_local_copy()
#     assert True