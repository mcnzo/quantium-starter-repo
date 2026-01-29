from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def pytest_setup_options():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Runs the browser in the background
    return options

from dash.testing.application_runners import import_app

def test_001_header_exists(dash_duo):
    # 1. Start the app
    app = import_app("app")
    dash_duo.start_server(app)

    # 2. Wait for the header and check its text
    # Replace 'h1' with the actual ID if you gave your header one, 
    # otherwise we look for the tag.
    dash_duo.wait_for_element("h1", timeout=10)
    header_text = dash_duo.find_element("h1").text
    
    assert header_text == "Pink Morsel Sales Visualiser"

def test_002_visualisation_exists(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    # Check for the graph by its ID
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    
    assert dash_duo.find_element("#sales-line-chart").is_displayed()

def test_003_region_picker_exists(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    # Check for the radio items by its ID
    dash_duo.wait_for_element("#region-filter", timeout=10)
    
    assert dash_duo.find_element("#region-filter").is_displayed()