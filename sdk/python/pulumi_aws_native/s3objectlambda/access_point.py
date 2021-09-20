# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['AccessPointArgs', 'AccessPoint']

@pulumi.input_type
class AccessPointArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 object_lambda_configuration: Optional[pulumi.Input['AccessPointObjectLambdaConfigurationArgs']] = None):
        """
        The set of arguments for constructing a AccessPoint resource.
        :param pulumi.Input[str] name: The name you want to assign to this Object lambda Access Point.
        :param pulumi.Input['AccessPointObjectLambdaConfigurationArgs'] object_lambda_configuration: The Object lambda Access Point Configuration that configures transformations to be applied on the objects on specified S3 Actions
        """
        pulumi.set(__self__, "name", name)
        if object_lambda_configuration is not None:
            pulumi.set(__self__, "object_lambda_configuration", object_lambda_configuration)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name you want to assign to this Object lambda Access Point.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="objectLambdaConfiguration")
    def object_lambda_configuration(self) -> Optional[pulumi.Input['AccessPointObjectLambdaConfigurationArgs']]:
        """
        The Object lambda Access Point Configuration that configures transformations to be applied on the objects on specified S3 Actions
        """
        return pulumi.get(self, "object_lambda_configuration")

    @object_lambda_configuration.setter
    def object_lambda_configuration(self, value: Optional[pulumi.Input['AccessPointObjectLambdaConfigurationArgs']]):
        pulumi.set(self, "object_lambda_configuration", value)


class AccessPoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 object_lambda_configuration: Optional[pulumi.Input[pulumi.InputType['AccessPointObjectLambdaConfigurationArgs']]] = None,
                 __props__=None):
        """
        The AWS::S3ObjectLambda::AccessPoint resource is an Amazon S3ObjectLambda resource type that you can use to add computation to S3 actions

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name you want to assign to this Object lambda Access Point.
        :param pulumi.Input[pulumi.InputType['AccessPointObjectLambdaConfigurationArgs']] object_lambda_configuration: The Object lambda Access Point Configuration that configures transformations to be applied on the objects on specified S3 Actions
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessPointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::S3ObjectLambda::AccessPoint resource is an Amazon S3ObjectLambda resource type that you can use to add computation to S3 actions

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
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 object_lambda_configuration: Optional[pulumi.Input[pulumi.InputType['AccessPointObjectLambdaConfigurationArgs']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccessPointArgs.__new__(AccessPointArgs)

            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["object_lambda_configuration"] = object_lambda_configuration
            __props__.__dict__["arn"] = None
            __props__.__dict__["creation_date"] = None
            __props__.__dict__["policy_status"] = None
            __props__.__dict__["public_access_block_configuration"] = None
        super(AccessPoint, __self__).__init__(
            'aws-native:s3objectlambda:AccessPoint',
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
        __props__.__dict__["creation_date"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["object_lambda_configuration"] = None
        __props__.__dict__["policy_status"] = None
        __props__.__dict__["public_access_block_configuration"] = None
        return AccessPoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[str]:
        """
        The date and time when the Object lambda Access Point was created.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name you want to assign to this Object lambda Access Point.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="objectLambdaConfiguration")
    def object_lambda_configuration(self) -> pulumi.Output[Optional['outputs.AccessPointObjectLambdaConfiguration']]:
        """
        The Object lambda Access Point Configuration that configures transformations to be applied on the objects on specified S3 Actions
        """
        return pulumi.get(self, "object_lambda_configuration")

    @property
    @pulumi.getter(name="policyStatus")
    def policy_status(self) -> pulumi.Output[Any]:
        return pulumi.get(self, "policy_status")

    @property
    @pulumi.getter(name="publicAccessBlockConfiguration")
    def public_access_block_configuration(self) -> pulumi.Output['outputs.AccessPointPublicAccessBlockConfiguration']:
        """
        The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.
        """
        return pulumi.get(self, "public_access_block_configuration")

