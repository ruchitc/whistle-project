"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# ML registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.content_based_rec.recommender import Recommender

try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    rec = Recommender()
    # add to ML registry
    registry.add_algorithm(endpoint_name="content_based_rec",
                            algorithm_object=rec,
                            algorithm_name="cosine_similarity",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="ruchit",
                            algorithm_description="Music recommender using cosine similarity",
                            algorithm_code=inspect.getsource(Recommender))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))