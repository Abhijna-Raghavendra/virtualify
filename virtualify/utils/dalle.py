USER_ID = 'openai'
APP_ID = 'dall-e'
MODEL_ID = 'dall-e-3'
MODEL_VERSION_ID = 'dc9dcb6ee67543cebc0b9a025861b868'


from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2


def dallE(prompt,PAT):
     channel = ClarifaiChannel.get_grpc_channel()
     stub = service_pb2_grpc.V2Stub(channel)
     metadata = (('authorization', 'Key ' + PAT),)
     
     userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)
     post_model_outputs_response = stub.PostModelOutputs(
         service_pb2.PostModelOutputsRequest(
             user_app_id=userDataObject, 
             model_id=MODEL_ID,
             version_id=MODEL_VERSION_ID,  
             inputs=[
                 resources_pb2.Input(
                     data=resources_pb2.Data(
                         text=resources_pb2.Text(
                             raw=prompt
                            # url=TEXT_FILE_URL
                            # raw=file_bytes
                            )
                            )
                            )
                            ]
                            ),
                            metadata=metadata
                            )
     if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        print(post_model_outputs_response.status)
        raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

    # Since we have one input, one output will exist here
     output = post_model_outputs_response.outputs[0].data.image.base64
     image_filename = f"gen-image.jpg"
     with open(image_filename, 'wb') as f:
         f.write(output)
         
     return output    
    