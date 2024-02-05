from django.test import TestCase
from helper.base.base_test_case import TestAPIBaseCaseV2 , TestAPIBaseCase


class TestAPIBaseCase(TestAPIBaseCaseV2):
    def test_get_tokens(self):
       
        response = self.client.get( self.reverse('Auth:get_token'))
        
        # 確保返回的狀態碼是 200 OK
        self.assertEqual(response.status_code, 200)

        # 確保響應中有 'token' 這個鍵
        self.assertIn('token', response.data.get('token'))
    # def test_token(self):
    #     if request_csrf_token == "":
    #     # Fall back to X-CSRFToken, to make things easier for AJAX,
    #     # and possible for PUT/DELETE.
    #     request_csrf_token = request.META.get('HTTP_X_CSRFTOKEN', '')

    #     if not constant_time_compare(request_csrf_token, csrf_token):
    #         return self._reject(request, REASON_BAD_TOKEN)