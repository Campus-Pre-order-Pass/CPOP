
from Camera.views import save_model
from helper.base.base_test_case import TestAPIBaseCaseV2


class CameraSaveDataTestCase(TestAPIBaseCaseV2):
    def test_save_model(self):
        res = save_model(1, 100)
        self.assertEqual(res, True)
