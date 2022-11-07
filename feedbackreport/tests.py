from django.test import TestCase
import json
from feedbackreport.models import Feedback

testemail = 'test@test.com'
content_type = 'application/json'
add_feedback_url = '/feedbackreport/add-feedback-report/'
payment_error_title = 'payment error'
payment_error_content = 'payment feature is not working'

class FeedbackReportTest(TestCase):
    def setup_account(self):
        self.client.post('/user/flu-register-user/',json.dumps({
            'email' : 'test@test.com',
            'name' : 'testwithdjango',
            'password': 'test',
        }),content_type=content_type)

    def test_addfeedback(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = testemail
        session.save()

        response = self.client.post(add_feedback_url,json.dumps({
            'session_id' : session.session_key,
            'input_feedback_title' : payment_error_title,
            'input_feedback_feature' : 'payment',
            'input_feedback_texbox' : payment_error_content,
        }),content_type=content_type)

        feedback = Feedback.objects.filter(feedback_feature = 'payment').first()

        self.assertIsNotNone(feedback)
        self.assertEqual(response.status_code, 200)

    def test_deletefeedback(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = testemail
        session.save()

        self.client.post(add_feedback_url,json.dumps({
            'session_id' : session.session_key,
            'input_feedback_title' : payment_error_title,
            'input_feedback_feature' : 'payment',
            'input_feedback_texbox' : payment_error_content,
        }),content_type=content_type)

        response = self.client.delete('/feedbackreport/delete-feedback-report/',json.dumps({
            'session_id': session.session_key,
            'input_feedback_title' : payment_error_title,
        }),content_type=content_type)

        self.assertEqual(response.status_code, 200)
    def test_viewfeedback(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = testemail
        session.save()

        self.client.post(add_feedback_url,json.dumps({
            'session_id' : session.session_key,
            'input_feedback_title' : payment_error_title,
            'input_feedback_feature' : 'payment',
            'input_feedback_texbox' : payment_error_content,
        }),content_type=content_type)

        self.client.post(add_feedback_url,json.dumps({
            'session_id' : session.session_key,
            'input_feedback_title' : 'home page error',
            'input_feedback_feature' : 'home page',
            'input_feedback_texbox' : 'home page is not working',
        }),content_type=content_type)

        self.client.post(add_feedback_url,json.dumps({
            'session_id' : session.session_key,
            'input_feedback_title' : 'pocket error',
            'input_feedback_feature' : 'pocket',
            'input_feedback_texbox' : 'pocket is not working',
        }),content_type=content_type)

        self.client.delete('/feedbackreport/delete-feedback-report/',json.dumps({
            'session_id': session.session_key,
            'input_feedback_title' : 'pocket error',
        }),content_type=content_type)

        response = self.client.get('/feedbackreport/view-feedback-report/',{
            'session_id': session.session_key,
        })

        self.assertEqual(response.status_code, 200)

    def test_viewfeedback_negative(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = testemail
        session.save()

        self.client.post(add_feedback_url,json.dumps({
            'session_id' : session.session_key,
            'input_feedback_title' : payment_error_title,
            'input_feedback_feature' : 'payment',
            'input_feedback_texbox' : payment_error_content,
        }),content_type=content_type)

        response = self.client.get('/feedbackreport/view-feedback-report/',{
            'session_id': session.session_key,
        })

        self.assertNotEqual(json.loads(response.content)[0]['feedback_title'], 'home page error')