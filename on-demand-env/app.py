#!/usr/bin/env python3
import os

import aws_cdk as cdk

from on_demand_env.on_demand_env_stack import OnDemandEnvStack

# Load environment name from environment variable
env_name = os.environ.get("ENV_NAME", "dev")
region = os.environ.get("AWS_REGION", "eu-central-1")
account_id = os.environ.get("AWS_ACCOUNT_ID", "434834777527")

app = cdk.App()
OnDemandEnvStack(app, env_name, env={'region': region, 'account': account_id})
app.synth()
