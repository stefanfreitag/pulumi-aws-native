# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['AccessPointArgs', 'AccessPoint']

@pulumi.input_type
class AccessPointArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 vpc_configuration: pulumi.Input['AccessPointVpcConfigurationArgs'],
                 name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[Any] = None):
        """
        The set of arguments for constructing a AccessPoint resource.
        :param pulumi.Input[str] bucket: The Amazon Resource Name (ARN) of the bucket you want to associate this AccessPoint with.
        :param pulumi.Input['AccessPointVpcConfigurationArgs'] vpc_configuration: Virtual Private Cloud (VPC) from which requests can be made to the AccessPoint.
        :param pulumi.Input[str] name: A name for the AccessPoint.
        :param Any policy: The access point policy associated with this access point.
        """
        AccessPointArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bucket=bucket,
            vpc_configuration=vpc_configuration,
            name=name,
            policy=policy,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bucket: pulumi.Input[str],
             vpc_configuration: pulumi.Input['AccessPointVpcConfigurationArgs'],
             name: Optional[pulumi.Input[str]] = None,
             policy: Optional[Any] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("bucket", bucket)
        _setter("vpc_configuration", vpc_configuration)
        if name is not None:
            _setter("name", name)
        if policy is not None:
            _setter("policy", policy)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the bucket you want to associate this AccessPoint with.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> pulumi.Input['AccessPointVpcConfigurationArgs']:
        """
        Virtual Private Cloud (VPC) from which requests can be made to the AccessPoint.
        """
        return pulumi.get(self, "vpc_configuration")

    @vpc_configuration.setter
    def vpc_configuration(self, value: pulumi.Input['AccessPointVpcConfigurationArgs']):
        pulumi.set(self, "vpc_configuration", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A name for the AccessPoint.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[Any]:
        """
        The access point policy associated with this access point.
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[Any]):
        pulumi.set(self, "policy", value)


class AccessPoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[Any] = None,
                 vpc_configuration: Optional[pulumi.Input[pulumi.InputType['AccessPointVpcConfigurationArgs']]] = None,
                 __props__=None):
        """
        Resource Type Definition for AWS::S3Outposts::AccessPoint

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The Amazon Resource Name (ARN) of the bucket you want to associate this AccessPoint with.
        :param pulumi.Input[str] name: A name for the AccessPoint.
        :param Any policy: The access point policy associated with this access point.
        :param pulumi.Input[pulumi.InputType['AccessPointVpcConfigurationArgs']] vpc_configuration: Virtual Private Cloud (VPC) from which requests can be made to the AccessPoint.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessPointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type Definition for AWS::S3Outposts::AccessPoint

        :param str resource_name: The name of the resource.
        :param AccessPointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessPointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AccessPointArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[Any] = None,
                 vpc_configuration: Optional[pulumi.Input[pulumi.InputType['AccessPointVpcConfigurationArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccessPointArgs.__new__(AccessPointArgs)

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            __props__.__dict__["name"] = name
            __props__.__dict__["policy"] = policy
            if vpc_configuration is not None and not isinstance(vpc_configuration, AccessPointVpcConfigurationArgs):
                vpc_configuration = vpc_configuration or {}
                def _setter(key, value):
                    vpc_configuration[key] = value
                AccessPointVpcConfigurationArgs._configure(_setter, **vpc_configuration)
            if vpc_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_configuration'")
            __props__.__dict__["vpc_configuration"] = vpc_configuration
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["bucket", "name", "vpc_configuration"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(AccessPoint, __self__).__init__(
            'aws-native:s3outposts:AccessPoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AccessPoint':
        """
        Get an existing AccessPoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AccessPointArgs.__new__(AccessPointArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["bucket"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["policy"] = None
        __props__.__dict__["vpc_configuration"] = None
        return AccessPoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the specified AccessPoint.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the bucket you want to associate this AccessPoint with.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A name for the AccessPoint.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[Optional[Any]]:
        """
        The access point policy associated with this access point.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> pulumi.Output['outputs.AccessPointVpcConfiguration']:
        """
        Virtual Private Cloud (VPC) from which requests can be made to the AccessPoint.
        """
        return pulumi.get(self, "vpc_configuration")

