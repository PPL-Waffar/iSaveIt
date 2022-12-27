from django.test import TestCase
import json
from feedbackreport.models import Feedback

testemail = 'test@test.com'
content_type = 'application/json'
add_feedback_url = '/feedbackreport/add-feedback-report/'
delete_feedback_url = '/feedbackreport/delete-feedback-report/'
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
            'feedback1': 5,
            'feedback2' : 'i hope i will save money',
            'feedback3' : 'less impulsive expenses',
            'feedback4' : 'very helpful and fun to do',
            'feedback5' : 'i think the application has quite good features',

        }),content_type=content_type)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_deletefeedback(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = testemail
        session.save()

        response = self.client.post(add_feedback_url,json.dumps({
            'session_id' : session.session_key,
            'feedback1': 5,
            'feedback2' : 'i hope i will save money',
            'feedback3' : 'less impulsive expenses',
            'feedback4' : 'very helpful and fun to do',
            'feedback5' : 'i think the application has quite good features',

        }),content_type=content_type)

        response = self.client.delete(delete_feedback_url,json.dumps({
            'session_id': session.session_key,
            'input_id': 1,
        }),content_type=content_type)

        self.assertEqual(response.status_code, 200)

    def test_viewfeedback(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = testemail
        session.save()

        self.client.post(add_feedback_url,json.dumps({
            'session_id' : session.session_key,
            'feedback1': 5,
            'feedback2' : 'i hope i will save money',
            'feedback3' : 'less impulsive expenses',
            'feedback4' : 'very helpful and fun to do',
            'feedback5' : 'i think the application has quite good features',

        }),content_type=content_type)
        self.client.post(add_feedback_url,json.dumps({
            'session_id' : session.session_key,
            'feedback1': 3,
            'feedback2' : 'i hope i will save money2',
            'feedback3' : 'less impulsive expense2s',
            'feedback4' : 'very helpful and fun to do2',
            'feedback5' : 'i think the application has quite good features2',

        }),content_type=content_type)

        self.client.post(add_feedback_url,json.dumps({
            'session_id' : session.session_key,
            'feedback1': 4,
            'feedback2' : 'i hope i will save money4',
            'feedback3' : 'less impulsive expenses4',
            'feedback4' : 'very helpful and fun to 4do',
            'feedback5' : 'i think the application has4 quite good features',

        }),content_type=content_type)

        self.client.delete('/feedbackreport/delete-feedback-report/',json.dumps({
            'session_id': session.session_key,
            'input_id': 1,
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
            'feedback1': 5,
            'feedback2' : 'i hope i will save money',
            'feedback3' : 'less impulsive expenses',
            'feedback4' : 'very helpful and fun to do',
            'feedback5' : 'i think the application has quite good features',

        }),content_type=content_type)

        response = self.client.get('/feedbackreport/view-feedback-report/',{
            'session_id': session.session_key,
        })

        self.assertNotEqual(json.loads(response.content)[0]['feedback_goal'], 'home page error')