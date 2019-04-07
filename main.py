from WorkflowController import WorkflowController

if __name__ == '__main__':
    control = WorkflowController(5)
    control.initialize()
    control.start()