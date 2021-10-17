# rabbitmq
A simple RabbitMQ python script


	import json
	import time
	import QueueManager

	class SampleQueueWriteManager:

	    def __init__(self):
		self.queue_manager = QueueManager()


	    def process_write_data(self):
			"""
			======================================================================
			* Method Name : process_write_data
			* Description : Read the JSON data and send it to the queue
			* Args   : None
			* Return : None
			======================================================================
			"""
		while True:

		    with open('D:\Projects\sample_json.json', 'r') as file:
			json_dict = json.load(file)

		    point_list = {}

				for data in json_dict:
				    point_list['uid'] = data['ID']
			point_list['name'] = data['Name']
			self.add_to_queue(point_list)

		    time.sleep(5)


	    def add_to_queue(self, json_point_list):
			"""
			======================================================================
			* Method Name : add_to_queue
			* Description : Add the data to queue
			* Args   : json_point_list
			* Return : None
			======================================================================
			"""
		queue_name = json_point_list['device_name']

			self.queue_manager.create_queue(queue_name)
			self.queue_manager.add_data_to_queue(queue_name, json_point_list)
