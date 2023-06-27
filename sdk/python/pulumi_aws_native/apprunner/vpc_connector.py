# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['VpcConnectorArgs', 'VpcConnector']

@pulumi.input_type
class VpcConnectorArgs:
    def __init__(__self__, *,
                 subnets: pulumi.Input[Sequence[pulumi.Input[str]]],
                 security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['VpcConnectorTagArgs']]]] = None,
                 vpc_connector_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VpcConnector resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnets: A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_groups: A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.
        :param pulumi.Input[Sequence[pulumi.Input['VpcConnectorTagArgs']]] tags: A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.
        :param pulumi.Input[str] vpc_connector_name: A name for the VPC connector. If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.
        """
        pulumi.set(__self__, "subnets", subnets)
        if security_groups is not None:
            pulumi.set(__self__, "security_groups", security_groups)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vpc_connector_name is not None:
            pulumi.set(__self__, "vpc_connector_name", vpc_connector_name)

    @property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.
        """
        return pulumi.get(self, "subnets")

    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnets", value)

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.
        """
        return pulumi.get(self, "security_groups")

    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_groups", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpcConnectorTagArgs']]]]:
        """
        A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpcConnectorTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vpcConnectorName")
    def vpc_connector_name(self) -> Optional[pulumi.Input[str]]:
        """
        A name for the VPC connector. If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.
        """
        return pulumi.get(self, "vpc_connector_name")

    @vpc_connector_name.setter
    def vpc_connector_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_connector_name", value)


class VpcConnector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpcConnectorTagArgs']]]]] = None,
                 vpc_connector_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The AWS::AppRunner::VpcConnector resource specifies an App Runner VpcConnector.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_groups: A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnets: A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpcConnectorTagArgs']]]] tags: A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.
        :param pulumi.Input[str] vpc_connector_name: A name for the VPC connector. If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpcConnectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::AppRunner::VpcConnector resource specifies an App Runner VpcConnector.

        :param str resource_name: The name of the resource.
        :param VpcConnectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpcConnectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpcConnectorTagArgs']]]]] = None,
                 vpc_connector_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpcConnectorArgs.__new__(VpcConnectorArgs)

            __props__.__dict__["security_groups"] = security_groups
            if subnets is None and not opts.urn:
                raise TypeError("Missing required property 'subnets'")
            __props__.__dict__["subnets"] = subnets
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vpc_connector_name"] = vpc_connector_name
            __props__.__dict__["vpc_connector_arn"] = None
            __props__.__dict__["vpc_connector_revision"] = None
        super(VpcConnector, __self__).__init__(
            'aws-native:apprunner:VpcConnector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VpcConnector':
        """
        Get an existing VpcConnector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VpcConnectorArgs.__new__(VpcConnectorArgs)

        __props__.__dict__["security_groups"] = None
        __props__.__dict__["subnets"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpc_connector_arn"] = None
        __props__.__dict__["vpc_connector_name"] = None
        __props__.__dict__["vpc_connector_revision"] = None
        return VpcConnector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.
        """
        return pulumi.get(self, "security_groups")

    @property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.
        """
        return pulumi.get(self, "subnets")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.VpcConnectorTag']]]:
        """
        A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcConnectorArn")
    def vpc_connector_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of this VPC connector.
        """
        return pulumi.get(self, "vpc_connector_arn")

    @property
    @pulumi.getter(name="vpcConnectorName")
    def vpc_connector_name(self) -> pulumi.Output[Optional[str]]:
        """
        A name for the VPC connector. If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.
        """
        return pulumi.get(self, "vpc_connector_name")

    @property
    @pulumi.getter(name="vpcConnectorRevision")
    def vpc_connector_revision(self) -> pulumi.Output[int]:
        """
        The revision of this VPC connector. It's unique among all the active connectors ("Status": "ACTIVE") that share the same Name.
        """
        return pulumi.get(self, "vpc_connector_revision")

