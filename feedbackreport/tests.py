from django.test import TestCase
import json

from feedbackreport.models import Feedback

class FeedbackReportTest(TestCase):
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

    def test_deletefeedback(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        content_type = 'application/json'

        self.client.post('/feedbackreport/add-feedback-report/',json.dumps({
            'session_id' : session.session_key,
            'input_feedback_rating' : 5,
            'input_feedback_goal' : 'i hope i will save money',
            'input_feedback_text' : 'less impulsive expenses',
            'input_feedback_text2' : 'very helpful and fun to do',
            'input_feedback_comment' : 'i think the application has quite good features',

        }),content_type=content_type)

        response = self.client.delete('/feedbackreport/delete-feedback-report/',json.dumps({
            'session_id': session.session_key,
            'id': 1,
        }),content_type=content_type)

        self.assertEqual(response.status_code, 200)

    def test_viewfeedback(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        self.client.post('/feedbackreport/add-feedback-report/',json.dumps({
            'session_id' : session.session_key,
            'input_feedback_title' : 'payment error',
            'input_feedback_feature' : 'payment',
            'input_feedback_texbox' : 'payment feature is not working',
        }),content_type='application/json')

        self.client.post('/feedbackreport/add-feedback-report/',json.dumps({
            'session_id' : session.session_key,
            'input_feedback_title' : 'home page error',
            'input_feedback_feature' : 'home page',
            'input_feedback_texbox' : 'home page is not working',
        }),content_type='application/json')

        self.client.post('/feedbackreport/add-feedback-report/',json.dumps({
            'session_id' : session.session_key,
            'input_feedback_title' : 'pocket error',
            'input_feedback_feature' : 'pocket',
            'input_feedback_texbox' : 'pocket is not working',
        }),content_type='application/json')

        self.client.delete('/feedbackreport/delete-feedback-report/',json.dumps({
            'session_id': session.session_key,
            'input_feedback_title' : 'pocket error',
        }),content_type='application/json')

        response = self.client.get('/feedbackreport/view-feedback-report/',{
            'session_id': session.session_key,
        })

        self.assertEqual(response.status_code, 200)
    
    def test_viewfeedback_negative(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = 'test@test.com'
        session.save()

        self.client.post('/feedbackreport/add-feedback-report/',json.dumps({
            'session_id' : session.session_key,
            'input_feedback_title' : 'payment error',
            'input_feedback_feature' : 'payment',
            'input_feedback_texbox' : 'payment feature is not working',
        }),content_type='application/json')

        response = self.client.get('/feedbackreport/view-feedback-report/',{
            'session_id': session.session_key,
        })

        self.assertNotEqual(json.loads(response.content)[0]['feedback_title'], 'home page error')