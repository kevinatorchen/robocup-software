import robocup
import constants
import play
import enum
import behavior
import main


# Maintains the state of the ball's position by keeping track of which
# half the ball is on and prints on both entering a given state and
# continously during the execution of a given state.
class WhichHalf(play.Play):
	class State(enum.Enum):
	# Define your states here.
	# eg: some_state = 0
	# -----------------------
		upper_half = 0
		lower_half = 1

	def __init__(self):
		super().__init__(continuous=True)

	# Register the states you defined using 'add_state'.
	# eg: self.add_state(WhichHalf.State.<???>,
	#                    behavior.Behavior.State.running)
	# ----------------------------------------------------

		self.add_state(WhichHalf.State.upper_half, behavior.Behavior.State.running)
		self.add_state(WhichHalf.State.lower_half, behavior.Behavior.State.running)

	# Add your state transitions using 'add_transition'.
	# eg: self.add_transition(behavior.Behavior.State.start,
	#                         self.State.<???>, lambda: True,
	#                         'immediately')
	# eg: self.add_transition(self.State.<???>, self.State.<???>,
	#                         lambda: <???>,
	#                         'state change message')
	# ------------------------------------------------------------

		self.add_transition(behavior.Behavior.State.start, self.State.upper_half,
					self.isUpperHalf, 'is upper')
		self.add_transition(behavior.Behavior.State.start, self.State.lower_half, 
					self.isLowerHalf, 'is lower')
		self.add_transition(self.State.upper_half, self.State.lower_half, self.isLowerHalf,
					'is lower')
		self.add_transition(self.State.lower_half, self.State.upper_half, self.isUpperHalf,
					'is upper')

	# replace self.lowerHalf with lambda: main.ball().pos.y < constants.Field.Length / 2

	# Define your own 'on_enter' and 'execute' functions here.
	# eg: def on_enter_<???>(self):
	#         print('Something?')
	# eg: def execute_<???>(self):
	#         print('Something?')
	# ---------------------------------------------------------
	def on_enter_upper_half(self):
		print('Wow! You have entered the upper half.')

	def on_enter_lower_half(self):
		print('Wow! You have entered the lower half.')

	#def execute_upper_half(self):
	#	print('Still on upper half.')

	#def execute_lower_half(self):
	#	print('Still on lower half.')

	def isUpperHalf(self):
	#	print('Wow! You have entered the upper half.')
		return main.ball().pos.y > constants.Field.Length / 2

	def isLowerHalf(self):
	#	print('Wow! You have entered the lower half.')
		return main.ball().pos.y < constants.Field.Length / 2
