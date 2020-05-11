import requests
import unittest
import pdb


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

if __name__ == '__main__':
    unittest.main()