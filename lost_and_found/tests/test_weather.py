from lost_and_found.weather import Weather

def test_get_current_weather_format():
    # This test just checks if the return string contains expected parts
    result = Weather.get_current_weather("London")
    # Assert that the result is a string
    assert isinstance(result, str)
    assert "°C" in result or "Weather not available" in result