import boto3


class FaceRecognition:
    def __init__(self, file_path, key, secret, token):
        self.file_path = file_path
        self.aws_key = key
        self.aws_secret = secret
        self.access_token = token
        self.client = boto3.client("rekognition", aws_access_key_id=self.aws_key,
                                   aws_secret_access_key=self.aws_secret,
                                   aws_session_token=self.access_token
                                   )

    def detection(self):
        """Read file and response it with result"""
        with open(self.photo, 'rb') as image:
            response = self.client.detect_faces(Image={
                'Bytes': image.read()
            },
                Attributes=['ALL']
            )
        details = response['FaceDetails']

        if details:
            result = {
                'gender': response['FaceDetails'][0]['Gender']['Value'],
                'age_range': str(response['FaceDetails'][0]['AgeRange']['Low']) + '-' + str(
                    response['FaceDetails'][0]['AgeRange']['High']),
                'emotions': response['FaceDetails'][0]['Emotions'][0]['Type'],
                'sun_glasses': response['FaceDetails'][0]['Sunglasses']['Value'],
                'beard': response['FaceDetails'][0]['Beard']['Value'],
                'mustache': response['FaceDetails'][0]['Mustache']['Value'],
                'eyes_open': response['FaceDetails'][0]['EyesOpen']['Value'],
                'mouth_open': response['FaceDetails'][0]['MouthOpen']['Value'],
                'smile': response['FaceDetails'][0]['Smile']['Value']
            }
        else:
            result = 'Face was not found'
        return result

    def run(self):
        details = self.face_detection()
        if isinstance(details, dict):
            print('**************************The candidate has the following details*********************************')
            for each_key in details.keys():
                print(each_key + '=' + str(details[each_key]))

        else:
            print(details)