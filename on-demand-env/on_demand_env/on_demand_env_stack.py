from aws_cdk import (
    # Duration,
    Stack,
    CfnOutput,
    aws_ec2 as ec2,

)
from constructs import Construct

class OnDemandEnvStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # lookup default vpc
        vpc = ec2.Vpc.from_lookup(
            self, "VPC",
            is_default=True
        )

        # create ec2 instance security group
        ec2_instance_security_group = ec2.SecurityGroup(
            self, "EC2InstanceSecurityGroup",
            vpc=vpc,
            allow_all_outbound=True
        )

        # allow ssh into instance
        ec2_instance_security_group.add_ingress_rule(
            ec2.Peer.ipv4("0.0.0.0/0"),
            ec2.Port.tcp(22)
        )

        # create ec2 instance
        ec2_instance = ec2.Instance(
            self, "EC2Instance",
            vpc=vpc,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2,
                ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            security_group=ec2_instance_security_group
        )

        # Output instance details
        instance_id = CfnOutput(self, "InstanceId", value=ec2_instance.instance_id)
        instance_public_ip = CfnOutput(self, "InstancePublicIp", value=ec2_instance.instance_public_ip)
        instance_private_ip = CfnOutput(self, "InstancePrivateIp", value=ec2_instance.instance_private_ip)
        instance_public_dns = CfnOutput(self, "InstancePublicDns", value=ec2_instance.instance_public_dns_name)
        security_group_id = CfnOutput(self, "SecurityGroupId", value=ec2_instance_security_group.security_group_id)
        


            