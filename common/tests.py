from rest_framework.test import APITestCase
from common.models import Page, GalleryPhoto, Settings
from PIL import Image
import tempfile


class TestPages(APITestCase):

    def test_page(self):
        # Page.objects.create(slug='slug', title='TestTitle', content='TestContent')

        data = {
            'slug': 'vs--vs-vs-s--gf',
            'title': 'TestTitle',
            'content': 'TestContent',
        }

        response = self.client.post('/api/v1/page/create', data=data)

        self.assertEqual(response.status_code, 201)


class TestGalleryPhoto(APITestCase):

    def test_example_image(self):
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        return tmp_file

        response = self.client.post('/api/v1/photo/', {'image': example_image()}, format='multipart')

        self.assertEqual(response.status_code, 201)


