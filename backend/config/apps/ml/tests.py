from django.test import  TestCase
import inspect

import pandas as pd

from apps.ml.content_based_rec.recommender import Recommender
from apps.ml.registry import MLRegistry

class MLTests(TestCase):

    def test(self):
        # input_data = "https://open.spotify.com/playlist/37i9dQZF1DXbTxeAdrVG2l?si=233815c496e54e41"
        # input_data = "https://open.spotify.com/playlist/2OQTMm3MMqUMDRWJaafxWE?si=e58552b26479475f"
        input_data = {"link": "https://open.spotify.com/playlist/37i9dQZF1DXbTxeAdrVG2l?si=233815c496e54e41"}

        response = pd.DataFrame()

        recommender = Recommender()
        response = recommender.computeRecommendation(input_data)
        
        self.assertEqual('OK', response['status'])

    # test registry
    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "content_based_rec"
        algorithm_object = Recommender()
        algorithm_name = "cosine_similarity"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "ruchit"
        algorithm_description = "Music recommender using cosine similarity"
        algorithm_code = inspect.getsource(Recommender)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)