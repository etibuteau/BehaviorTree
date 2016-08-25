# Under MIT License, see LICENSE.txt
from ai.Algorithm.BehaviorTree.Task import Task
from ai.Algorithm.BehaviorTree.TaskController import TaskController
from ai.Algorithm.BehaviorTree.Blackboard import Blackboard

__author__ = 'RoboCupULaval'


class LeafTask(Task):

    """Leaf task (ou noeuds) dans le behavior tree.

    Specifie un TaskControler, par composition,
    pour s'occuper de tous les controles logiques
    sans charger la classe Task class avec des
    complications."""

    def __init__(self):
        self.task_controller = TaskController()
        self.blackboard = Blackboard














