import yagmail
import requests
import unittest
import pdb
import ast
from datetime import datetime, timedelta

class TestArgovisWebappRunning(unittest.TestCase):

    def test_check_home_module(self):
        url = "https://argovis.colorado.edu/ng/home"
        resp = requests.get(url)
        if not resp.status_code // 100 == 2:
            self.assertTrue(False, "Error: url: {0} Unexpected response {1}".format(url, resp))
        else: 
            self.assertTrue(True)

    def test_check_ar_module(self):
        url = "https://argovis.colorado.edu/ng/ar"
        resp = requests.get(url)
        if not resp.status_code // 100 == 2:
            self.assertTrue(False, "Error: url: {0} Unexpected response {1}".format(url, resp))
        else: 
            self.assertTrue(True)

    def test_check_covar_module(self):
        url = "https://argovis.colorado.edu/ng/covar"
        resp = requests.get(url)
        if not resp.status_code // 100 == 2:
            self.assertTrue(False, "Error: url: {0} Unexpected response {1}".format(url, resp))
        else: 
            self.assertTrue(True)

    def test_check_grid_module(self):
        url = "https://argovis.colorado.edu/ng/grid"
        resp = requests.get(url)
        if not resp.status_code // 100 == 2:
            self.assertTrue(False, "Error: url: {0} Unexpected response {1}".format(url, resp))
        else: 
            self.assertTrue(True)

    def test_check_profview_module(self):
        url = "https://argovis.colorado.edu/ng/profview"
        resp = requests.get(url)
        if not resp.status_code // 100 == 2:
            self.assertTrue(False, "Error: url: {0} Unexpected response {1}".format(url, resp))
        else: 
            self.assertTrue(True)

    def test_check_covar_module(self):
        url = "https://argovis.colorado.edu/ng/covar"
        resp = requests.get(url)
        if not resp.status_code // 100 == 2:
            self.assertTrue(False, "Error: url: {0} Unexpected response {1}".format(url, resp))
        else: 
            self.assertTrue(True)

    def test_check_not_a_module(self):
        url = "https://argovis.colorado.edu/catalog/profiles/2902536_900/page"
        resp = requests.get(url)
        if not resp.status_code // 100 == 2:
            self.assertTrue(False, "Error: url: {0} Unexpected response {1}".format(url, resp))
        else: 
            self.assertTrue(True)

    def test_check_current_database(self):
        url = "https://argovis.colorado.edu/selection/overview"
        resp = requests.get(url)
        if not resp.status_code // 100 == 2:
            self.assertTrue(False, "Error: url: {0} Unexpected response {1}".format(url, resp))
        else: 
            self.assertTrue(True)
        dict_str = resp.content.decode("UTF-8")
        overview = ast.literal_eval(dict_str)
        dateUpdated = datetime.strptime(overview["lastAdded"], '%Y-%m-%dT%H:%M:%S.%fZ')
        today = datetime.now()
        dt = today - dateUpdated
        self.assertTrue(dt.days == 0, "date updated does not match todays date")

def run_tests():
    testsRun = []
    testsRun.append( check_home_module() )
    testsRun.append( check_grid_module() )
    testsRun.append( check_ar_module() )
    testsRun.append( check_covar_module() )
    testsRun.append( check_profview_module() )
    testsRun.append( dummy_test_that_always_fails() )
    failedTests = [ test for test in testsRun if isinstance(test, str) ]
    write_report(failedTests)
    if not len(failedTests)==0:
        send_email()

def write_report(failedTests):
    with open('test-report.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % test for test in failedTests)

def send_email():
    receiver = "argovistesting@gmail.com"
    body = "Hello there from Yagmail"
    password = input("Type your password and press enter: ")
    filename='./test-report.txt'
    yag = yagmail.SMTP(receiver, password)
    yag.send(
        to=receiver,
        subject="Yagmail test with attachment",
        contents=body, 
        attachments=filename,
    )

if __name__ == '__main__':
    unittest.main()