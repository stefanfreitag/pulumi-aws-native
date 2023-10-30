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
from ._enums import *
from ._inputs import *

__all__ = ['AccessPointArgs', 'AccessPoint']

@pulumi.input_type
class AccessPointArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 bucket_account_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[Any] = None,
                 public_access_block_configuration: Optional[pulumi.Input['AccessPointPublicAccessBlockConfigurationArgs']] = None,
                 vpc_configuration: Optional[pulumi.Input['AccessPointVpcConfigurationArgs']] = None):
        """
        The set of arguments for constructing a AccessPoint resource.
        :param pulumi.Input[str] bucket: The name of the bucket that you want to associate this Access Point with.
        :param pulumi.Input[str] bucket_account_id: The AWS account ID associated with the S3 bucket associated with this access point.
        :param pulumi.Input[str] name: The name you want to assign to this Access Point. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the access point name.
        :param Any policy: The Access Point Policy you want to apply to this access point.
        :param pulumi.Input['AccessPointPublicAccessBlockConfigurationArgs'] public_access_block_configuration: The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.
        :param pulumi.Input['AccessPointVpcConfigurationArgs'] vpc_configuration: If you include this field, Amazon S3 restricts access to this Access Point to requests from the specified Virtual Private Cloud (VPC).
        """
        pulumi.set(__self__, "bucket", bucket)
        if bucket_account_id is not None:
            pulumi.set(__self__, "bucket_account_id", bucket_account_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if public_access_block_configuration is not None:
            pulumi.set(__self__, "public_access_block_configuration", public_access_block_configuration)
        if vpc_configuration is not None:
            pulumi.set(__self__, "vpc_configuration", vpc_configuration)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        The name of the bucket that you want to associate this Access Point with.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="bucketAccountId")
    def bucket_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS account ID associated with the S3 bucket associated with this access point.
        """
        return pulumi.get(self, "bucket_account_id")

    @bucket_account_id.setter
    def bucket_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket_account_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name you want to assign to this Access Point. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the access point name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[Any]:
        """
        The Access Point Policy you want to apply to this access point.
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[Any]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="publicAccessBlockConfiguration")
    def public_access_block_configuration(self) -> Optional[pulumi.Input['AccessPointPublicAccessBlockConfigurationArgs']]:
        """
        The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.
        """
        return pulumi.get(self, "public_access_block_configuration")

    @public_access_block_configuration.setter
    def public_access_block_configuration(self, value: Optional[pulumi.Input['AccessPointPublicAccessBlockConfigurationArgs']]):
        pulumi.set(self, "public_access_block_configuration", value)

    @property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> Optional[pulumi.Input['AccessPointVpcConfigurationArgs']]:
        """
        If you include this field, Amazon S3 restricts access to this Access Point to requests from the specified Virtual Private Cloud (VPC).
        """
        return pulumi.get(self, "vpc_configuration")

    @vpc_configuration.setter
    def vpc_configuration(self, value: Optional[pulumi.Input['AccessPointVpcConfigurationArgs']]):
        pulumi.set(self, "vpc_configuration", value)


class AccessPoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 bucket_account_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[Any] = None,
                 public_access_block_configuration: Optional[pulumi.Input[pulumi.InputType['AccessPointPublicAccessBlockConfigurationArgs']]] = None,
                 vpc_configuration: Optional[pulumi.Input[pulumi.InputType['AccessPointVpcConfigurationArgs']]] = None,
                 __props__=None):
        """
        The AWS::S3::AccessPoint resource is an Amazon S3 resource type that you can use to access buckets.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket that you want to associate this Access Point with.
        :param pulumi.Input[str] bucket_account_id: The AWS account ID associated with the S3 bucket associated with this access point.
        :param pulumi.Input[str] name: The name you want to assign to this Access Point. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the access point name.
        :param Any policy: The Access Point Policy you want to apply to this access point.
        :param pulumi.Input[pulumi.InputType['AccessPointPublicAccessBlockConfigurationArgs']] public_access_block_configuration: The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.
        :param pulumi.Input[pulumi.InputType['AccessPointVpcConfigurationArgs']] vpc_configuration: If you include this field, Amazon S3 restricts access to this Access Point to requests from the specified Virtual Private Cloud (VPC).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessPointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::S3::AccessPoint resource is an Amazon S3 resource type that you can use to access buckets.

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
                 bucket: Optional[pulumi.Input[str]] = None,
                 bucket_account_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[Any] = None,
                 public_access_block_configuration: Optional[pulumi.Input[pulumi.InputType['AccessPointPublicAccessBlockConfigurationArgs']]] = None,
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
            __props__.__dict__["bucket_account_id"] = bucket_account_id
            __props__.__dict__["name"] = name
            __props__.__dict__["policy"] = policy
            __props__.__dict__["public_access_block_configuration"] = public_access_block_configuration
            __props__.__dict__["vpc_configuration"] = vpc_configuration
            __props__.__dict__["alias"] = None
            __props__.__dict__["arn"] = None
            __props__.__dict__["network_origin"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["bucket", "bucket_account_id", "name", "vpc_configuration"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(AccessPoint, __self__).__init__(
            'aws-native:s3:AccessPoint',
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

        __props__.__dict__["alias"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["bucket"] = None
        __props__.__dict__["bucket_account_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_origin"] = None
        __props__.__dict__["policy"] = None
        __props__.__dict__["public_access_block_configuration"] = None
        __props__.__dict__["vpc_configuration"] = None
        return AccessPoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def alias(self) -> pulumi.Output[str]:
        """
        The alias of this Access Point. This alias can be used for compatibility purposes with other AWS services and third-party applications.
        """
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the specified accesspoint.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        The name of the bucket that you want to associate this Access Point with.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="bucketAccountId")
    def bucket_account_id(self) -> pulumi.Output[Optional[str]]:
        """
        The AWS account ID associated with the S3 bucket associated with this access point.
        """
        return pulumi.get(self, "bucket_account_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name you want to assign to this Access Point. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the access point name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkOrigin")
    def network_origin(self) -> pulumi.Output['AccessPointNetworkOrigin']:
        """
        Indicates whether this Access Point allows access from the public Internet. If VpcConfiguration is specified for this Access Point, then NetworkOrigin is VPC, and the Access Point doesn't allow access from the public Internet. Otherwise, NetworkOrigin is Internet, and the Access Point allows access from the public Internet, subject to the Access Point and bucket access policies.
        """
        return pulumi.get(self, "network_origin")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[Optional[Any]]:
        """
        The Access Point Policy you want to apply to this access point.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="publicAccessBlockConfiguration")
    def public_access_block_configuration(self) -> pulumi.Output[Optional['outputs.AccessPointPublicAccessBlockConfiguration']]:
        """
        The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.
        """
        return pulumi.get(self, "public_access_block_configuration")

    @property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> pulumi.Output[Optional['outputs.AccessPointVpcConfiguration']]:
        """
        If you include this field, Amazon S3 restricts access to this Access Point to requests from the specified Virtual Private Cloud (VPC).
        """
        return pulumi.get(self, "vpc_configuration")

