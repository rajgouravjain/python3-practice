import json
from SpiffWorkflow import Workflow
from SpiffWorkflow.specs import WorkflowSpec
from SpiffWorkflow.serializer.json import JSONSerializer
import workflow1 
#TestWorkflowSpec

spec = workflow1.TestWorkflowSpec()

# Create the workflow.
workflow = Workflow(spec)

# Execute until all tasks are done or require manual intervention.
# For the sake of this tutorial, we ignore the "manual" flag on the
# tasks. In practice, you probably don't want to do that.

workflow.complete_all(halt_on_manual=False)
#print(workflow.get_task('task_a2').results)

# Alternatively, this is what a UI would do for a manual task.
#workflow.complete_task_from_id(...)
