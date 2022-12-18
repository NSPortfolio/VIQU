import dash
from dash import html
from app import app

def test_app(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)
    dash_duo.wait_for_element("#radio_buttons", timeout=10)
    dash_duo.wait_for_element("#figure", timeout=10)
    
