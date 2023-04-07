# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['KeySigningKeyArgs', 'KeySigningKey']

@pulumi.input_type
class KeySigningKeyArgs:
    def __init__(__self__, *,
                 hosted_zone_id: pulumi.Input[str],
                 key_management_service_arn: pulumi.Input[str],
                 status: pulumi.Input['KeySigningKeyStatus'],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a KeySigningKey resource.
        :param pulumi.Input[str] hosted_zone_id: The unique string (ID) used to identify a hosted zone.
        :param pulumi.Input[str] key_management_service_arn: The Amazon resource name (ARN) for a customer managed key (CMK) in AWS Key Management Service (KMS). The KeyManagementServiceArn must be unique for each key signing key (KSK) in a single hosted zone.
        :param pulumi.Input['KeySigningKeyStatus'] status: A string specifying the initial status of the key signing key (KSK). You can set the value to ACTIVE or INACTIVE.
        :param pulumi.Input[str] name: An alphanumeric string used to identify a key signing key (KSK). Name must be unique for each key signing key in the same hosted zone.
        """
        pulumi.set(__self__, "hosted_zone_id", hosted_zone_id)
        pulumi.set(__self__, "key_management_service_arn", key_management_service_arn)
        pulumi.set(__self__, "status", status)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Input[str]:
        """
        The unique string (ID) used to identify a hosted zone.
        """
        return pulumi.get(self, "hosted_zone_id")

    @hosted_zone_id.setter
    def hosted_zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "hosted_zone_id", value)

    @property
    @pulumi.getter(name="keyManagementServiceArn")
    def key_management_service_arn(self) -> pulumi.Input[str]:
        """
        The Amazon resource name (ARN) for a customer managed key (CMK) in AWS Key Management Service (KMS). The KeyManagementServiceArn must be unique for each key signing key (KSK) in a single hosted zone.
        """
        return pulumi.get(self, "key_management_service_arn")

    @key_management_service_arn.setter
    def key_management_service_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_management_service_arn", value)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input['KeySigningKeyStatus']:
        """
        A string specifying the initial status of the key signing key (KSK). You can set the value to ACTIVE or INACTIVE.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input['KeySigningKeyStatus']):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        An alphanumeric string used to identify a key signing key (KSK). Name must be unique for each key signing key in the same hosted zone.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class KeySigningKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hosted_zone_id: Optional[pulumi.Input[str]] = None,
                 key_management_service_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['KeySigningKeyStatus']] = None,
                 __props__=None):
        """
        Represents a key signing key (KSK) associated with a hosted zone. You can only have two KSKs per hosted zone.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hosted_zone_id: The unique string (ID) used to identify a hosted zone.
        :param pulumi.Input[str] key_management_service_arn: The Amazon resource name (ARN) for a customer managed key (CMK) in AWS Key Management Service (KMS). The KeyManagementServiceArn must be unique for each key signing key (KSK) in a single hosted zone.
        :param pulumi.Input[str] name: An alphanumeric string used to identify a key signing key (KSK). Name must be unique for each key signing key in the same hosted zone.
        :param pulumi.Input['KeySigningKeyStatus'] status: A string specifying the initial status of the key signing key (KSK). You can set the value to ACTIVE or INACTIVE.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KeySigningKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a key signing key (KSK) associated with a hosted zone. You can only have two KSKs per hosted zone.

        :param str resource_name: The name of the resource.
        :param KeySigningKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KeySigningKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hosted_zone_id: Optional[pulumi.Input[str]] = None,
                 key_management_service_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['KeySigningKeyStatus']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KeySigningKeyArgs.__new__(KeySigningKeyArgs)

            if hosted_zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'hosted_zone_id'")
            __props__.__dict__["hosted_zone_id"] = hosted_zone_id
            if key_management_service_arn is None and not opts.urn:
                raise TypeError("Missing required property 'key_management_service_arn'")
            __props__.__dict__["key_management_service_arn"] = key_management_service_arn
            __props__.__dict__["name"] = name
            if status is None and not opts.urn:
                raise TypeError("Missing required property 'status'")
            __props__.__dict__["status"] = status
        super(KeySigningKey, __self__).__init__(
            'aws-native:route53:KeySigningKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'KeySigningKey':
        """
        Get an existing KeySigningKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = KeySigningKeyArgs.__new__(KeySigningKeyArgs)

        __props__.__dict__["hosted_zone_id"] = None
        __props__.__dict__["key_management_service_arn"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["status"] = None
        return KeySigningKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Output[str]:
        """
        The unique string (ID) used to identify a hosted zone.
        """
        return pulumi.get(self, "hosted_zone_id")

    @property
    @pulumi.getter(name="keyManagementServiceArn")
    def key_management_service_arn(self) -> pulumi.Output[str]:
        """
        The Amazon resource name (ARN) for a customer managed key (CMK) in AWS Key Management Service (KMS). The KeyManagementServiceArn must be unique for each key signing key (KSK) in a single hosted zone.
        """
        return pulumi.get(self, "key_management_service_arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        An alphanumeric string used to identify a key signing key (KSK). Name must be unique for each key signing key in the same hosted zone.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['KeySigningKeyStatus']:
        """
        A string specifying the initial status of the key signing key (KSK). You can set the value to ACTIVE or INACTIVE.
        """
        return pulumi.get(self, "status")

