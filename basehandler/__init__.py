#Base Handler
class BaseHandler(object):   #To be subclassed to handle the GPIO and other Stuff
    #~~~~~~~~~~BUILT-IN~~~~~~~~~~#
    def __init__(self):
        '''
        You must subclass it to handle the GPIO and other Stuff
        '''
        self._connected_stuff = dict()

    def __dir__(self):
        directory = super().__dir__()
        directory.extend([key for key in self._connected_stuff])
        
    def __getattr__(self, key):
        if key in super().__getattribute__("_connected_stuff"):
            return super().__getattribute__("_connected_stuff")[key]
        else:
            raise AttributeError
    #~~~~~~~~~PROPERTIES~~~~~~~~~#
    @property
    def connected_stuff(self):
        return self._connected_stuff

    #~~~~~~~~~FUNCTIONS~~~~~~~~~~#          
    def connect_stuff(self, **kwargs):
        '''
        Yes, Stuff, You can handle other app if you like.
        If you name it "app" you can access it with handle.app
        '''
        for kwarg in kwargs:
            self._connected_stuff[kwarg] = kwargs[kwarg]

    def handle(self, signal, *args, **kwargs):
        try:
            self.get_signal(signal.action)(signal, *args, **kwargs)
        except KeyError:
            pass
            
    def get_signal(self, signal):
        return self.__getattribute__("signal_{}".format(signal))
            
    #Handling functions:
    #All signals must begin with "signal_"
