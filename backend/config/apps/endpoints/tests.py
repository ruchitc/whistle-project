from django.test import TestCase

from rest_framework.test import APIClient
# Create your tests here.
class EndpointTests(TestCase):

    def test_predict_view(self):
        client = APIClient()
        input_data = {
                    "link": "https://open.spotify.com/playlist/37i9dQZF1DXbTxeAdrVG2l?si=233815c496e54e41"
                      }
        classifier_url = "/api/v1/content_based_rec/predict"
        response = client.post(classifier_url, input_data, format='json')

        # self.assertEqual('OK', response['status'])
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data["label"], "<=50K")
        self.assertTrue("request_id" in response.data)
        self.assertTrue("status" in response.data)