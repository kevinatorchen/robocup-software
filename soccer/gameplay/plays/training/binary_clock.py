import robocup
import constants
import play
import enum
import behavior
import main
import skills.move
import plays.testing.line_up
import time


# Maintains the state of the ball's position by keeping track of which
# half the ball is on and prints on both entering a given state and
# continously during the execution of a given state.
class BinaryClock(play.Play):
    class State(enum.Enum):
        # Define your states here.
        # eg: some_state = 0
        
        DISPLAY = 0
        DUMMY = 1

        # -----------------------

    def __init__(self):
        super().__init__(continuous=True)

        # This is a local variable of this class
        # Refer to it with self.current_time
        self.current_time = time.localtime().tm_min

        # Register the states you defined using 'add_state'.
        # eg: self.add_state(WhichHalf.State.<???>,
        #                    behavior.Behavior.State.running)
        # ----------------------------------------------------
        self.add_state(BinaryClock.State.DISPLAY, behavior.Behavior.State.running);
        self.add_state(BinaryClock.State.DUMMY, behavior.Behavior.State.running);

        # Add your state transitions using 'add_transition'.
        # eg: self.add_transition(behavior.Behavior.State.start,
        #                         self.State.<???>, lambda: True,
        #                         'immediately')
        # eg: self.add_transition(self.State.<???>, self.State.<???>,
        #                         lambda: <???>,
        #                         'state change message')
        # ------------------------------------------------------------

    def shouldAppear(self, robo_number):
        binary = format(mins, '06b')
        return binary[robo_number] == '1'

        # EXAMPLE TRANSITION, YOU MAY WANT TO REPLACE THIS
        self.add_transition(behavior.Behavior.State.start,
        	self.State.DUMMY, lambda: True, 'immediately')
        self.add_transition(self.State.DUMMY, self.State.DISPLAY,
        	lambda: true, 'Displaying again!')
        self.add_transition(self.State.DISPLAY, self.State.DUMMY,
        	lambda: false, 'Going to Dummy state!')


    # Define your own 'on_enter' and 'execute' functions here.
    # eg: def on_enter_<???>(self):
    #         print('Something?')
    # eg: def execute_<???>(self):
    #         print('Something?')
    # ---------------------------------------------------------


    # Demo of moving to a point.
    def on_enter_DUMMY(self):
    	increment = constants.Field.Length / 20
    	starting_position = constants.Field.Length / 2
    	
    	for i in range(6):
    		move_point = roboCup.Point(0, starting_position + increment * i)
    		self.add_subbehavior(skills.move.Move(move_point), 'Move to center')

