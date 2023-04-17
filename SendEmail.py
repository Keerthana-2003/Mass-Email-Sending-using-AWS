import boto3

ses_client = boto3.client('ses')

def lambda_handler(event, context):
    try:
        response = ses_client.send_email(
            Destination={
                'ToAddresses': ['sendermail@gmail.com'],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': 'This is the message body.',
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': 'This is the subject line.',
                },
            },
            Source='reciever@gmail.com',
        )
        print("Email sent! Message ID:"),
        print(response['MessageId'])
    except Exception as e:
        print(e)
        print('Error sending email.')
