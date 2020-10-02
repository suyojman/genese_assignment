from face_recognition import FaceRecognition

file_path="path_of_the_file"
key="aws_key"
secret="aws_secret"
token="aws_token"

instance = FaceRecognition(file_path,key,secret,token)
results = instance.detection()

if isinstance(results, dict):
    print("The details of the candidate are as follows: ")
    for each_key in results.keys():
        print(each_key + '=' + str(results[each_key]))

else:
    print(results)