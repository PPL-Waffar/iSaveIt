from django.test import TestCase
import json
from feedbackreport.models import Feedback

testemail = 'test@test.com'
content_type = 'application/json'
add_feedback_url = '/feedbackreport/add-feedback-report/'
delete_feedback_url = '/feedbackreport/delete-feedback-report/'
edit_feedback_url = '/feedbackreport/edit-feedback-report/'
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
            'input_feedback_rating' : 5,
            'input_feedback_goal' : 'i hope i will save money',
            'input_feedback_text' : 'less impulsive expenses',
            'input_feedback_text2' : 'very helpful and fun to do',
            'input_feedback_comment' : 'i think the application has quite good features',

        }),content_type=content_type)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_deletefeedback(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = testemail
        session.save()

        self.client.post(add_feedback_url,json.dumps({
            'session_id' : session.session_key,
            'input_feedback_rating' : 5,
            'input_feedback_goal' : 'i hope i will save money',
            'input_feedback_text' : 'less impulsive expenses',
            'input_feedback_text2' : 'very helpful and fun to do',
            'input_feedback_comment' : 'i think the application has quite good features',

        }),content_type=content_type)

        response = self.client.delete(delete_feedback_url,json.dumps({
            'session_id': session.session_key,
            'id': 1,
        }),content_type=content_type)

        self.assertEqual(response.status_code, 200)

    def test_viewfeedback(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = testemail
        session.save()

        self.client.post(add_feedback_url,json.dumps({
            'session_id' : session.session_key,
            'input_feedback_rating' : 5,
            'input_feedback_goal' : 'i hope i will save money',
            'input_feedback_text' : 'less impulsive expenses',
            'input_feedback_text2' : 'very helpful and fun to do',
            'input_feedback_comment' : 'i think the application has quite good features',

        }),content_type=content_type)

        self.client.post(add_feedback_url,json.dumps({
            'session_id' : session.session_key,
            'input_feedback_rating' : 9,
            'input_feedback_goal' : 'i hope i will save money2',
            'input_feedback_text' : 'less impulsive expenses2',
            'input_feedback_text2' : 'very helpful and fun to do2',
            'input_feedback_comment' : 'i think the application has quite good features2',

        }),content_type=content_type)

        self.client.post(add_feedback_url,json.dumps({
            'session_id' : session.session_key,
            'input_feedback_rating' : 8,
            'input_feedback_goal' : 'i hope i will save money3',
            'input_feedback_text' : 'less impulsive expenses3',
            'input_feedback_text2' : 'very helpful and fun to do3',
            'input_feedback_comment' : 'i think the application has quite good features3',

        }),content_type=content_type)

        self.client.delete('/feedbackreport/delete-feedback-report/',json.dumps({
            'session_id': session.session_key,
            'id': 1,
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
            'input_feedback_rating' : 5,
            'input_feedback_goal' : 'i hope i will save money',
            'input_feedback_text' : 'less impulsive expenses',
            'input_feedback_text2' : 'very helpful and fun to do',
            'input_feedback_comment' : 'i think the application has quite good features',
            }),content_type=content_type)

        response = self.client.get('/feedbackreport/view-feedback-report/',{
            'session_id': session.session_key,
        })

        self.assertNotEqual(json.loads(response.content)[0]['feedback_goal'], 'home page error')
    
    def test_editfeedback(self):
        self.setup_account()
        session = self.client.session
        session['_auth_user_id'] = testemail
        session.save()

        self.client.post(add_feedback_url,json.dumps({
            'session_id' : session.session_key,
            'input_feedback_rating' : 5,
            'input_feedback_goal' : 'i hope i will save money',
            'input_feedback_text' : 'less impulsive expenses',
            'input_feedback_text2' : 'very helpful and fun to do',
            'input_feedback_comment' : 'i think the application has quite good features',

        }),content_type=content_type)

        response = self.client.post(edit_feedback_url,json.dumps({
            'session_id': session.session_key,
            'id': 1,
            'input_feedback_rating' : 2,
            'input_feedback_goal' : 'i hope i will save money more',
            'input_feedback_text' : 'not less impulsive',
            'input_feedback_text2' : 'not very helpful',
            'input_feedback_comment' : 'not quite good features',
        }),content_type=content_type)
        