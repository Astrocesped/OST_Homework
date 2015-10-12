#!/usr/local/bin/python3
#
# Lesson 04: "Publish and Subscribe" Homework
#
__author__ = "cmontesr"
'''
Created on Sep 10, 2015

pubandsub_extended.py: Extends the functionality of the Publisher and
                       Subscriber classes found in the Lesson, which
                       introduce the user to the publish and subscribe
                       mechanism for distribution of data.
'''

from project_log import start_logging
from logging import info as log_info
from logging import error as log_error

start_logging()

class Publisher:
    def __init__(self):
        log_info("New Publisher instance created.")
        self.subscribers = []
        
    def subscribe(self, subscriber):
        if subscriber in self.subscribers:
            log_error("Attempt to re-sub an existing subscriber to Publisher")
            raise ValueError("Multiple subscriptions are not allowed")
        self.subscribers.append(subscriber)
        
    def unsubscribe(self, subscriber):
        if subscriber not in self.subscribers:
            log_error("Can't unsub non-existing subscriber from Publisher")
            raise ValueError("Can only unsubscribe subscriber")
        self.subscribers.remove(subscriber)
        
    def publish(self, s):
        log_info("New publication from Publisher triggered")
        for subscriber in self.subscribers:
            subscriber(s)
            

if __name__ == "__main__":
    
    def multiplier(s):
        print(2 * s)
    
    class SimpleSubscriber:
        """
        Subscriber whose only unsubscription condition is reach
        a certain number of received publications.
        """
        def __init__(self, name, max_publs=3):
            
            self.name = name
            self._max_publs = max_publs
            self._publs = 0
            log_info("New SimpleSubscriber instance: {0}".format(self.name))
        
        def process(self, s):
            """
            Transforms the retrieved published data into an uppercase string.
            """
            print(self.name, ":", str.upper(s))
            self._publs += 1
            
        def unsubscribe_condition(self):
            """
            If the maximum number of calls has been reached, request
            being removed from subscription.
            :return: Boolean indicating unsubsciption request
            """
            if self._publs >= self._max_publs:
                return True
            return False
            
        def __repr__(self):
            return self.name
    
    
    class ComposableSubscriber(SimpleSubscriber):
        """ Allows a function to subscribe to Publisher
        and possess its own methods. """
        
        def __init__(self, func, max_publs=3):
            SimpleSubscriber.__init__(self, func.__name__, max_publs)
            self.func = func
            log_info("New ComposableSubscriber inst: {0}".format(self.name))
        
        def process(self, *args, **kwargs):
            " Proxy the function, keep number of calls. "
            self.func(*args, **kwargs)
            self._publs += 1
    
    
    class SubscriberManager:
        " Keeps a tab of the subscribers to a certain publisher. "
        def __init__(self, publisher):
            self.subscriber_list = []
            self.publisher = publisher
            
            log_info("New SubscriberManager instance created")
        
        def check_unsubscriptions(self):
            " Checks for any subscriptor that has requested being removed. "
            for subscriber in self.subscriber_list:
                if subscriber.unsubscribe_condition():
                    self.publisher.unsubscribe(subscriber.process)
                    self.subscriber_list.remove(subscriber)
                    
                    log_info("{0} unsubscribed from {1}".format(
                            subscriber.name, publisher.__class__.__name__))
        
        def new_subscription(self, subscriber):
            """
            A new Subscriber has requested subscribe its process
            to the publisher. Add it to the manager's list.ty
            """
            self.publisher.subscribe(subscriber.process)
            self.subscriber_list.append(subscriber)
            
            log_info("{0} subscribed to {1}".format(
                    subscriber.name, publisher.__class__.__name__))
        
        def trigger_event(self, data):
            " The publisher has published something; notify subscribers. "
            # First check if any subscriber meets unsubscription
            # to avoid any erroneous publication
            self.check_unsubscriptions()
            
            # Now spread data with the Publisher's publish method
            self.publisher.publish(data)
            
            # Check if any subscriber has requested unsubscription after
            # the last publication, to avoid any future erroneous data sent
            self.check_unsubscriptions()
    
    publisher = Publisher()
    manager = SubscriberManager(publisher)
    
    manager.new_subscription(ComposableSubscriber(multiplier))
    
    for i in range(6):
        manager.new_subscription(SimpleSubscriber("Sub" + str(i)))
        
        line = input("Input {0} ".format(i))
        manager.trigger_event(line)
