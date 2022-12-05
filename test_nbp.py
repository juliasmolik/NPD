import requests
import nbp_change

# custom class to be the mock return value
# will override the requests.Response returned from requests.get
class MockResponse:
    
    @staticmethod
    # mock json() method always returns a specific testing dictionary
    def json():
        return {'table': 'A', 
                'currency': 'euro', 
                'code': 'EUR', 
                'rates': [{'no': '225/A/NBP/2022', 'effectiveDate': '2022-11-22', 'mid': 4.7075}, 
                          {'no': '226/A/NBP/2022', 'effectiveDate': '2022-11-23', 'mid': 4.6958}, 
                          {'no': '227/A/NBP/2022', 'effectiveDate': '2022-11-24', 'mid': 4.6993}, 
                          {'no': '228/A/NBP/2022', 'effectiveDate': '2022-11-25', 'mid': 4.6884}, 
                          {'no': '229/A/NBP/2022', 'effectiveDate': '2022-11-28', 'mid': 4.6835}, 
                          {'no': '230/A/NBP/2022', 'effectiveDate': '2022-11-29', 'mid': 4.6813}, 
                          {'no': '231/A/NBP/2022', 'effectiveDate': '2022-11-30', 'mid': 4.6684}, 
                          {'no': '232/A/NBP/2022', 'effectiveDate': '2022-12-01', 'mid': 4.6892}, 
                          {'no': '233/A/NBP/2022', 'effectiveDate': '2022-12-02', 'mid': 4.685}, 
                          {'no': '234/A/NBP/2022', 'effectiveDate': '2022-12-05', 'mid': 4.6898}]}


def test_get_courses(monkeypatch, currency_code = "eur", days = 10):
    """
    Function testing the "get_courses" method from the nbp_change file
    
    :param monkeypatch: monkeypatch
    :param currency_code: the currency code from which to download the data
    :param days: the number of days from which to download data
    """

    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the .json() method.
    def mock_get(*args, **kwargs):
        return MockResponse()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)
    
    # nbp_change.get_courses, which contains requests.get, uses the monkeypatch
    result = nbp_change.get_courses(currency_code, days)
    assert result == ([4.7075, 4.6958, 4.6993, 4.6884, 4.6835, 4.6813, 4.6684, 4.6892, 4.685, 4.6898], 'euro')


def test_calc_statistics(monkeypatch, currency_list = ["eur"], days = 10):
    """
    Function testing the "calc_statistics" method from the nbp_change file
    
    :param monkeypatch: monkeypatch
    :param currency_list: a list of currency codes from which to download the data
    :param days: the number of days from which to download data
    """
    
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    
    result = nbp_change.calc_statistics(currency_list, days)
    assert result == ({'eur': {'change': 0.9962400424853958, 'course': 4.6898, 'full_name': 'euro'}})