"""
======================================================================
* Module Name : queue_manager.py
* Created by  : Alan Raj C
* Created on  : 10-Oct-2021
* Description : This file manages the class handling Queues in RabbitMQ.
                Please see the README file for the usage
======================================================================
"""

import pika


class QueueManager:
    """
    ======================================================================
    * Class Name  : QueueManager
    * Description : Contain all the methods in/for handling a queue
    ======================================================================
    """

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()


    def create_rabbitmq_connection(self):
        """
        ======================================================================
        * Method Name : create_rabbitmq_connection
        * Description : Creates the connection with the RabbitMQ server
        * Args   : None
        * Return : None
        ======================================================================
        """
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()


    def add_data_to_queue(self, queue_name, json_point_list):
        """
        ======================================================================
        * Method Name : add_data_to_queue
        * Description : Add data to the queue created
        * Args   : queue_name
                 : json_point_list -> Body of the queue
        * Return : None
        ======================================================================
        """
        point_list = str(json_point_list)
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=point_list)


    def create_queue(self, queue_name):
        """
        ======================================================================
        * Method Name : create_queue
        * Description : Create a queue with the given queue name.
        * Args   : queue_name
        * Return : None
        ======================================================================
        """
        self.channel.queue_declare(queue=queue_name)


    def consume_queues(self, queue_name, callback):
        """
        ======================================================================
        * Method Name : consume_queues
        * Description : Consume/subscribe to the given queue
        * Args   : queue_name
                 : callback       -> The callback method
        * Return : None
        ======================================================================
        """
        self.channel.basic_consume(queue=queue_name, on_message_callback=callback)


    def consume_start(self):
        """
        ======================================================================
        * Method Name : consume_start
        * Description : Start the Consume/subscribe process
        * Args   : None
        * Return : None
        ======================================================================
        """
        self.channel.start_consuming()
