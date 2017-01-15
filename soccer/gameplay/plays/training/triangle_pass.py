import robocup
import constants
import play
import enum
import behavior
import main
import skills.move
import plays.testing.line_up
import time
import tactics.coordinanted_pass
import tactics.behavior_sequence


# Maintains the state of the ball's position by keeping track of which
# half the ball is on and prints on both entering a given state and
# continously during the execution of a given state.
class TrianglePass(play.Play):
    class State(enum.Enum):
        # Define your states here.
        # eg: some_state = 0
        # -----------------------
        waiting = 0;
        aligning = 1;
        passing = 2;
        receiving = 3;


    def __init__(self):
        super().__init__(continuous=True)

        # This is a local variable of this class
        # Refer to it with self.current_time
        self.current_time = time.localtime().tm_min
        self.current_side = 0;

        # Register the states you defined using 'add_state'.
        # eg: self.add_state(WhichHalf.State.<???>,
        #                    behavior.Behavior.State.running)
        # ----------------------------------------------------

        self.add_state(TrianglePass.State.waiting, behavior.Behavior.State.running);
        self.add_state(TrianglePass.State.aligning, behavior.Behavior.State.running);
        self.add_state(TrianglePass.State.passing, behavior.Behavior.State.running);
        self.add_state(TrianglePass.State.receiving, behavior.Behavior.State.running);

        # Add your state transitions using 'add_transition'.
        # eg: self.add_transition(behavior.Behavior.State.start,
        #                         self.State.<???>, lambda: True,
        #                         'immediately')
        # eg: self.add_transition(self.State.<???>, self.State.<???>,
        #                         lambda: <???>,
        #                         'state change message')
        # ------------------------------------------------------------

        # EXAMPLE TRANSITION, YOU MAY WANT TO REPLACE THIS
        self.add_transition(behavior.Behavior.State.start, self.State.aligning, lambda: True, 'immediately');
        self.add_transition(self.State.aligning, self.State.passing, self.isCompleted, 'passing');
        #self.add_transition(behavior.Behavior.State.aligning, behavior.Behavior.State.waiting, lambda: isAligned(), 'waiting');
        #self.add_transition(behavior.Behavior.State.waiting, behavior.Behavior.State.receiving, lambda: previousHasBall(), 'receiving');
        #self.add_transition(behavior.Behavior.State.receiving, behavior.Behavior.State.passing, lambda: hasBall(), 'passing');
        #self.add_transition(behioavr.Behavior.State.passing, behavior.Behavior.State.aligning, lambda: passedBall(), 'aligning');

    # Define your own 'on_enter' and 'execute' functions here.
    # eg: def on_enter_<???>(self):
    #         print('Something?')
    # eg: def execute_<???>(self):
    #         print('Something?')
    # ---------------------------------------------------------


    # Demo of moving to a point.


    def on_enter_aligning(self):
        point1 = robocup.Point(-1.0, 4.0);
        point2 = robocup.Point(1.0, 4.0);
        point3 = robocup.Point(0.0, 2.0);
        points = [point1, point2, point3];
        for i in range(3):
            self.add_subbehavior(skills.move.Move(points[i]), 'Robot' + str(i))
    		# move_point = robocup.Point(points[i].x, points[i].y);
        

        self.add_subbehavior(plays.testing.line_up.LineUp(), 'line up');

    def on_exit_aligning(self):
        self.remove_all_subbehaviors();    

    def execute_passing(self):
        point1 = robocup.Point(-1.0, 4.0);
        point2 = robocup.Point(1.0, 4.0);
        point3 = robocup.Point(0.0, 2.0);
        points = [point1, point2, point3];
        
        if (self.isCompleted()):
            self.remove_all_subbehaviors();
            pass_behavior = tactics.coordianted_pass.CoordinatedPass();
            pass_behavior.receive_point = points[current_side];
            current_side = (current_side + 1) % 3;
            self.add_subbehavior(pass_behavior, 'passing');



    def isCompleted(self):
        for behavior in self.all_subbehaviors():
            if (not behavior.is_done_running()):
                return False;
        return True;

