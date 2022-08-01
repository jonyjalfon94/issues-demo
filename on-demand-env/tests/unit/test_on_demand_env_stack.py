import aws_cdk as core
import aws_cdk.assertions as assertions

from on_demand_env.on_demand_env_stack import OnDemandEnvStack

# example tests. To run these tests, uncomment this file along with the example
# resource in on_demand_env/on_demand_env_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = OnDemandEnvStack(app, "on-demand-env")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
