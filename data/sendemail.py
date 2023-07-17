from data import private 
import ElasticEmail
from ElasticEmail.api import emails_api
from ElasticEmail.model.email_content import EmailContent
from ElasticEmail.model.body_part import BodyPart
from ElasticEmail.model.body_content_type import BodyContentType
from ElasticEmail.model.email_recipient import EmailRecipient
from ElasticEmail.model.email_message_data import EmailMessageData
from pprint import pprint
sendf = open("data/temp.txt" ,"r").read()
configuration = ElasticEmail.Configuration()
configuration.api_key['apikey'] = private.apikey

with ElasticEmail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = emails_api.EmailsApi(api_client)
    email_message_data = EmailMessageData(
        recipients=[
            EmailRecipient(
                email= private.recieveradress,
                fields={
                    "name": "",
                },
            ),
        ],
        content=EmailContent(
            body=[
                BodyPart(
                    content_type=BodyContentType("PlainText"),
                    content= str(sendf),
                    charset="utf-8",
                ),
            ],
            _from= private.signupemail,
            reply_to=	private.signupemail,
            subject= "Ip Address",
        ),
    ) # EmailMessageData | Email data
def sendip():
    try:
        # Send Bulk Emails
        api_response = api_instance.emails_post(email_message_data)
        pprint(api_response)
    except ElasticEmail.ApiException as e:
        print("Exception when calling EmailsApi->emails_post: %s\n" % e)