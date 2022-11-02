from django.test import TestCase
import json

from feedbackreport.models import Feedback

class AddFeedbackReportTest(TestCase):
    def setup_account(self):
        self.client.post('/user/flu-register-user/',json.dumps({
            'email' : 'test@test.com',
            'name' : 'testwithdjango',
            'password': 'test',
        }),content_type='application/json')

    def test_addfeedback(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        response = self.client.post('/feedbackreport/add-feedback-report/',json.dumps({
            'session_id' : session.session_key,
            'input_feedback_title' : 'payment error',
            'input_feedback_feature' : 'payment',
            'input_feedback_texbox' : 'payment feature is not working',
        }),content_type='application/json')

        feedback = Feedback.objects.filter(feedback_feature = 'payment').first()

        self.assertIsNotNone(feedback)
        self.assertEqual(response.status_code, 200)