# Under MIT License, see LICENSE.txt
__author__ = 'RoboCupULaval'


class TaskController:
    """Class added by composition to any task,
    to keep track of the Task state
    and logic flow.

    This state-control class is separated
    from the Task class so the Decorators
    have a chance at compile-time security.
    @author Ying"""

    def __init__(self):
        self.done = False
        self.success = True
        self.started = False

    def set_task(self,task):
        """Sets the task reference
        @param task Task to monitor"""
        self.task = task

    def safe_start(self,task):
        """Starts the monitored class"""
        self.started = True
        task.start()

    def safe_end(self,task):
        """Ends the monitored task"""
        self.done = False
        self.started = False
        task.end()

    def finish_with_success(self):
        """Ends the monitored class, with success"""
        self.success = True
        self.done = True

    def finish_with_failure(self):
        """Ends the monitored class, with failure"""
        self.success = False
        self.done = True

    def succeeded(self):
        """Indicates whether the task finished successfully
        @return True if it did, false if it didn't """
        return self.success

    def failed(self):
        """Indicates whether the task finished with failure
        @return True if it did, false if it didn't"""
        return not self.success

    def finished(self):
        """Indicates whether the task finished
        @return True if it did, false if it didn't """
        return self.done

    def started(self):
        """Indicates whether the class has started or not
        @return True if it has, false if it hasn't"""
        return self.started

    def reset_task(self):
        """Marks the class as just started."""
        self.done = False
