from flask import Flask,request
import boto3, json

app = Flask(__name__)
@app.route('/key')

  
def hello_world():
  lambda_client = boto3.client('lambda')
  # t = input('Enter a sentence: ')
  t=request.args.get('text')
  test_event = {"keywords":t}
  # print(type(test_event))

  response = lambda_client.invoke(
    FunctionName='SEOO',
    InvocationType = 'RequestResponse',
    Payload=json.dumps(test_event)
  )

  respon = json.load(response['Payload'])
  # respon1 = response['Payload']['body']['ctext']
  # dixt={"category": entityrecognition(t)}


  print()
  return(respon)

if __name__ == '__main__':
     app.run()



# print(response['Payload'])
# print(response['Payload'].read().decode("utf-8"))
#create post or get and pass through browser

