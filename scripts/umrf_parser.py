#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import torch
import transformers
import t5_prompt_creation

device = None

model = transformers.T5ForConditionalGeneration.from_pretrained('./saved_model')
model.eval()
tokenizer = transformers.T5Tokenizer.from_pretrained('./saved_tokenizer')

pub = rospy.Publisher('umrf_parses_output', String, queue_size=10)
exs = []

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard: %s", data.data)
    
    ex = [data.data]
    inputs = t5_prompt_creation.ensemble_prompt_creation(10, ex)
    
    encoded_input = tokenizer(inputs, max_length=512, padding='longest', truncation=True, return_tensors='pt').data
    input_ids = encoded_input['input_ids'].to(device)

    umrf_parse = model.generate(input_ids, max_length=200).squeeze()
    pred = tokenizer.decode(umrf_parse, skip_special_tokens=True)
    prepend_str = '{ "umrf_actions": '
    postpend_str = '}'
    output = prepend_str + pred + postpend_str
    print(output) 
    pub.publish(output)



def listener():
    rospy.init_node('umrf_parser_node', anonymous=True)

    rospy.Subscriber("umrf_parses", String, callback)


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    if torch.cuda.is_available():
        device = torch.device('cuda')
        print('gpu found')
    else:
        device = torch.device('cpu')
        print('using cpu')
    
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
