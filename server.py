import time
import json
from google.cloud import pubsub_v1
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="justbaat-debug-firebase-adminsdk.json"

from google.api_core import retry
from ffmpegManipulations import test
from metahuman import createMetaHuman

project_id='justbaat-debug'
subscription_id= 'metahuman-topic-debug-sub'

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def handleMessage(messageStr) -> None:
    try:
        msg = json.loads(messageStr);
        # msg = json.loads('{"id": "asdasd","ffmpegManipulations": {"watermark": {"url": "https://firebasestorage.googleapis.com/v0/b/justbaat-dev.appspot.com/o/Web%2Fcropped-favicon-32x32.png?alt=media&token=115e1e5b-b4ad-4941-9827-b4dbf4ad1885","position": {"placement": "TOP_RIGHT",}},"videoCaptions": {"assFile":"sadsa"}}}');
        metaHumanId=msg["id"]
        for key in msg["ffmpegManipulations"]:
            jobMetadata=msg["ffmpegManipulations"][key]
            if (key=="metahumanCreate"):
                createMetaHuman(jobMetadata,metaHumanId)
            if (key=="watermark"):
                test(jobMetadata,metaHumanId)
            if (key=="videoCaptions"):
                test(jobMetadata,metaHumanId)
            
            
    except Exception as err:
        print(
            f"Error consuming message {err}"
        )


# Wrap the subscriber in a 'with' block to automatically call close() to
# close the underlying gRPC channel when done.
with subscriber:
    while True:
        # The subscriber pulls a specific number of messages. The actual
        # number of messages pulled may be smaller than max_messages.
        response = subscriber.pull(
            request={"subscription": subscription_path, "max_messages": 1},
        )
        if len(response.received_messages) > 0:   
            ack_ids = []
            for received_message in response.received_messages:
                
                
                print(f"Received: {received_message.message.data}.")
                handleMessage(received_message.message.data)
                # Acknowledges the received messages so they will not be sent again.
                subscriber.acknowledge(
                    request={"subscription": subscription_path, "ack_ids": [received_message.ack_id]}
                )
                

            
        

       