import os
import io
from PIL import Image
from django.test import TestCase
from rest_framework.test import APIClient


class InventoryViewSet(TestCase):
    check_id = None
    test_image = None

    @classmethod
    def setUpClass(self):
        """
            1. SetUpClass will be called before executing the module.
            2. Settings the APIClient object.
        """
        self.client_obj = APIClient()

    def setUp(self):
        """
            SetUp method will be called before executing each test case.
            Validating with Post request by providing valid data
        """
        self.test_image = self.generate_photo_file('testInventoryViewSet',
                                                   'png', 500, 500)
        payload = {
            "name": "Abcd",
            "description": "Abcdefgh",
            "price": 1.0,
            "image": self.test_image
        }

        # Request the data by API call.
        response = self.client.post('/api/inventory/',
                                    payload, follow=True)

        # Checking the response
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('name'), 'Abcd')

        # Storing ID for further test cases checking
        type(self).check_id = response.json().get('id')

    def tearDown(self):
        """
            tearDown method will be called after executing each test case.
            Removes the test image by mentioning its path.
        """
        self.delete_temp_photo()

    @classmethod
    def tearDownClass(self):
        """
            TearDownClass will be called after executing the module.
        """
        self.delete_temp_photo(self)

    def generate_photo_file(self, file_name, ext, widht, height):
        """
            Generates the test image by using Pillow library
        """
        file = io.BytesIO()
        image = Image.new('RGBA', size=(widht, height), color=(155, 0, 0))
        image.save(file, ext)
        file.name = file_name + '.' + ext
        file.seek(0)
        return file

    def delete_temp_photo(self):
        """
            Removes the test pictures based on condition.
        """
        if self.test_image:
            delete_path = 'media/{}'.format(self.test_image.name)
        else:
            delete_path = 'media/{}'.format('testInventoryViewSet_*')
        file_path = os.path.join(os.getcwd(), delete_path)
        cmd = 'rm -rf {}'.format(file_path)
        os.system(cmd)

    # Checking with POST InValid data like Image Extension
    def test_InventoryViewSet_with_post_invalid_data_image_extension(self):
        """
            Validating Post request by providing InValid data like
            Image Extension.
        """
        actual = "Ensure that Image format should be `['png', 'jpg', 'jpeg']`"
        payload = {
            "name": "Abcd",
            "description": "Abcdefgh",
            "price": 1.0,
            "image": self.generate_photo_file('testInventoryViewSet',
                                              'gif', 10, 10)
        }

        # Request the data by API call.
        response = self.client.post('/api/inventory/',
                                    payload, follow=True)

        # Checking the response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json().get('image')[0], actual)

    # Checking with POST InValid data like Image Dimension
    def test_InventoryViewSet_with_post_invalid_data_dimension(self):
        """
            Validating Post request by providing InValid data like
            Image Dimensions.
        """
        actual = "Width x Height `(1000 x 1000)` must not exceed `800 x 800`"
        payload = {
            "name": "Abcd",
            "description": "Abcdefgh",
            "price": 1.0,
            "image": self.generate_photo_file('testInventoryViewSet',
                                              'png', 1000, 1000)
        }

        # Request the data by API call.
        response = self.client.post('/api/inventory/',
                                    payload, follow=True)

        # Checking the response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json().get('image')[0], actual)

    # Get request with valid response
    def test_InventoryViewSet_with_get_request(self):
        """
            Validating with Get request.
        """

        # Request the data by API call.
        response = self.client.get('/api/inventory/', follow=True)

        # Checking the response
        self.assertEqual(response.status_code, 200)
        self.assertGreater(response.json().get('count'), 0)

    # Get request with valid Id
    def test_InventoryViewSet_with_get_request_validId(self):
        """
            Validating with Get request by providing Valid Id.
        """

        # Request the data by API call.
        response = self.client.get('/api/inventory/{}/'.format(
            self.check_id), follow=True)

        # Checking the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('id'), self.check_id)

    # Get request with Invalid Id
    def test_InventoryViewSet_with_get_request_InvalidId(self):
        """
            Validating with Get request by providing Invalid Id.
        """

        # Request the data by API call.
        response = self.client.get('/api/inventory/{}/'.format(
            1), follow=True)

        # Checking the response
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json().get('detail'), 'Not found.')

    # Put request with valid Id and Valid data
    def test_InventoryViewSet_with_put_request_validId(self):
        """
            Validating with Put request by providing Valid Id and data.
        """
        self.test_image = self.generate_photo_file('testInventoryViewSet',
                                                   'png', 500, 500)
        payload = {
            "name": "Abcd",
            "description": "Abcdefgh",
            "price": 2.0,
            "image": self.test_image
        }

        # Request the data by API call.
        response = self.client_obj.put('/api/inventory/{p}/'.format(
            p=self.check_id), payload)

        # Checking the response
        self.assertEqual(response.status_code, 200)

    # Put request with valid Id and InValid data
    def test_InventoryViewSet_with_put_request_invalid_data(self):
        """
            Validating with Put request by providing Valid Id and Invalid data.
        """
        # Actual error messages
        actual_name = 'Ensure this field has at least 3 characters.'
        actual_price = 'Ensure this value is greater than or equal to 0.50.'
        actual_image = ('Width x Height `(1000 x 500)` must not exceed '
                        '`800 x 800`')
        self.test_image = self.generate_photo_file('testInventoryViewSet',
                                                   'png', 1000, 500)
        payload = {
            "name": "Ab",
            "description": "Abcdefgh",
            "price": -2.0,
            "image": self.test_image
        }

        # Request the data by API call.
        response = self.client_obj.put('/api/inventory/{}/'.format(
            self.check_id), payload, follow=True)

        # Checking the response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json().get("name")[0], actual_name)
        self.assertEqual(response.json().get("price")[0], actual_price)
        self.assertEqual(response.json().get("image")[0], actual_image)

    # Patch request with valid Id and Valid data
    def test_InventoryViewSet_with_patch_request_validId(self):
        """
            Validating with Patch request by providing Valid Id and data.
        """
        payload = {
            "name": "Abcdef",
        }

        # Request the data by API call.
        response = self.client_obj.patch('/api/inventory/{}/'.format(
            self.check_id), payload, follow=True)

        # Checking the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('name'), payload.get("name"))

    # Delete with Valid Id
    def test_InventoryViewSet_with_delete_valid_id(self):
        """
            Validating with delete request by providing Valid Id
        """

        # Request the data by API call.
        response = self.client.delete('/api/inventory/{}/'.format(
            self.check_id), follow=True)

        # Checking the response
        self.assertEqual(response.status_code, 204)

    # Delete with InValid Id
    def test_InventoryViewSet_with_delete_invalid_id(self):
        """
            Validating with delete request by providing Invalid Id
        """

        # Request the data by API call.
        response = self.client.delete('/api/inventory/{}/'.format(
            1), follow=True)

        # Checking the response
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json().get('detail'), 'Not found.')
