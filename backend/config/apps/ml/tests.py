from django.test import  TestCase

import pandas as pd

from apps.ml.content_based_rec.recommender import Recommender

class MLTests(TestCase):

    def test(self):
        # input_data = "https://open.spotify.com/playlist/37i9dQZF1DXbTxeAdrVG2l?si=233815c496e54e41"
        # input_data = "https://open.spotify.com/playlist/2OQTMm3MMqUMDRWJaafxWE?si=e58552b26479475f"
        input_data = {"link": "https://open.spotify.com/playlist/37i9dQZF1DXbTxeAdrVG2l?si=233815c496e54e41"}

        response = pd.DataFrame()

        recommender = Recommender()
        response = recommender.computeRecommendation(input_data)
        
        self.assertEqual('OK', response['status'])