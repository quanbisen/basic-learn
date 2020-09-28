import unittest

from anonymous_survey import AnonymousSurvey


class AnonymousSurveyTestCase(unittest.TestCase):

    def test_store_single_response(self):
        """ 测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)


if __name__ == '__main__':
    unittest.main()