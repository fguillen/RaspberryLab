from adafruit_led_animation.animation import Animation

# class definiation named similarly to the filename,
# extend the Animation class from the library
class DemoAnimation(Animation):

    # init function definition called by user
    # code to create an instance of the class
    def __init__(self, pixel_object, speed, color):

        # call the init function for the super class Animation,
        # pass through all of the arguments that came to us
        super().__init__(pixel_object, speed, color)

        # initialize any other variables you need for your
        # custom animation here
        # i.e. self.my_var = "something"

    # draw function will get called from animate when the time
    # comes for it based on the configured speed
    def draw(self):
        # do something with self.pixel_object
        self.pixel_object.fill(self.color)
