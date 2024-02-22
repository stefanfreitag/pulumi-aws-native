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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._enums import *
from ._inputs import *

__all__ = ['PartnerAccountArgs', 'PartnerAccount']

@pulumi.input_type
class PartnerAccountArgs:
    def __init__(__self__, *,
                 account_linked: Optional[pulumi.Input[bool]] = None,
                 partner_account_id: Optional[pulumi.Input[str]] = None,
                 partner_type: Optional[pulumi.Input['PartnerAccountPartnerType']] = None,
                 sidewalk: Optional[pulumi.Input['PartnerAccountSidewalkAccountInfoArgs']] = None,
                 sidewalk_response: Optional[pulumi.Input['PartnerAccountSidewalkAccountInfoWithFingerprintArgs']] = None,
                 sidewalk_update: Optional[pulumi.Input['PartnerAccountSidewalkUpdateAccountArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a PartnerAccount resource.
        :param pulumi.Input[bool] account_linked: Whether the partner account is linked to the AWS account.
        :param pulumi.Input[str] partner_account_id: The partner account ID to disassociate from the AWS account
        :param pulumi.Input['PartnerAccountPartnerType'] partner_type: The partner type
        :param pulumi.Input['PartnerAccountSidewalkAccountInfoArgs'] sidewalk: The Sidewalk account credentials.
        :param pulumi.Input['PartnerAccountSidewalkAccountInfoWithFingerprintArgs'] sidewalk_response: The Sidewalk account credentials.
        :param pulumi.Input['PartnerAccountSidewalkUpdateAccountArgs'] sidewalk_update: The Sidewalk account credentials.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: A list of key-value pairs that contain metadata for the destination.
        """
        if account_linked is not None:
            pulumi.set(__self__, "account_linked", account_linked)
        if partner_account_id is not None:
            pulumi.set(__self__, "partner_account_id", partner_account_id)
        if partner_type is not None:
            pulumi.set(__self__, "partner_type", partner_type)
        if sidewalk is not None:
            pulumi.set(__self__, "sidewalk", sidewalk)
        if sidewalk_response is not None:
            pulumi.set(__self__, "sidewalk_response", sidewalk_response)
        if sidewalk_update is not None:
            pulumi.set(__self__, "sidewalk_update", sidewalk_update)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="accountLinked")
    def account_linked(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the partner account is linked to the AWS account.
        """
        return pulumi.get(self, "account_linked")

    @account_linked.setter
    def account_linked(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "account_linked", value)

    @property
    @pulumi.getter(name="partnerAccountId")
    def partner_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The partner account ID to disassociate from the AWS account
        """
        return pulumi.get(self, "partner_account_id")

    @partner_account_id.setter
    def partner_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partner_account_id", value)

    @property
    @pulumi.getter(name="partnerType")
    def partner_type(self) -> Optional[pulumi.Input['PartnerAccountPartnerType']]:
        """
        The partner type
        """
        return pulumi.get(self, "partner_type")

    @partner_type.setter
    def partner_type(self, value: Optional[pulumi.Input['PartnerAccountPartnerType']]):
        pulumi.set(self, "partner_type", value)

    @property
    @pulumi.getter
    def sidewalk(self) -> Optional[pulumi.Input['PartnerAccountSidewalkAccountInfoArgs']]:
        """
        The Sidewalk account credentials.
        """
        return pulumi.get(self, "sidewalk")

    @sidewalk.setter
    def sidewalk(self, value: Optional[pulumi.Input['PartnerAccountSidewalkAccountInfoArgs']]):
        pulumi.set(self, "sidewalk", value)

    @property
    @pulumi.getter(name="sidewalkResponse")
    def sidewalk_response(self) -> Optional[pulumi.Input['PartnerAccountSidewalkAccountInfoWithFingerprintArgs']]:
        """
        The Sidewalk account credentials.
        """
        return pulumi.get(self, "sidewalk_response")

    @sidewalk_response.setter
    def sidewalk_response(self, value: Optional[pulumi.Input['PartnerAccountSidewalkAccountInfoWithFingerprintArgs']]):
        pulumi.set(self, "sidewalk_response", value)

    @property
    @pulumi.getter(name="sidewalkUpdate")
    def sidewalk_update(self) -> Optional[pulumi.Input['PartnerAccountSidewalkUpdateAccountArgs']]:
        """
        The Sidewalk account credentials.
        """
        return pulumi.get(self, "sidewalk_update")

    @sidewalk_update.setter
    def sidewalk_update(self, value: Optional[pulumi.Input['PartnerAccountSidewalkUpdateAccountArgs']]):
        pulumi.set(self, "sidewalk_update", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        A list of key-value pairs that contain metadata for the destination.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""PartnerAccount is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class PartnerAccount(pulumi.CustomResource):
    warnings.warn("""PartnerAccount is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_linked: Optional[pulumi.Input[bool]] = None,
                 partner_account_id: Optional[pulumi.Input[str]] = None,
                 partner_type: Optional[pulumi.Input['PartnerAccountPartnerType']] = None,
                 sidewalk: Optional[pulumi.Input[pulumi.InputType['PartnerAccountSidewalkAccountInfoArgs']]] = None,
                 sidewalk_response: Optional[pulumi.Input[pulumi.InputType['PartnerAccountSidewalkAccountInfoWithFingerprintArgs']]] = None,
                 sidewalk_update: Optional[pulumi.Input[pulumi.InputType['PartnerAccountSidewalkUpdateAccountArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Create and manage partner account

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] account_linked: Whether the partner account is linked to the AWS account.
        :param pulumi.Input[str] partner_account_id: The partner account ID to disassociate from the AWS account
        :param pulumi.Input['PartnerAccountPartnerType'] partner_type: The partner type
        :param pulumi.Input[pulumi.InputType['PartnerAccountSidewalkAccountInfoArgs']] sidewalk: The Sidewalk account credentials.
        :param pulumi.Input[pulumi.InputType['PartnerAccountSidewalkAccountInfoWithFingerprintArgs']] sidewalk_response: The Sidewalk account credentials.
        :param pulumi.Input[pulumi.InputType['PartnerAccountSidewalkUpdateAccountArgs']] sidewalk_update: The Sidewalk account credentials.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: A list of key-value pairs that contain metadata for the destination.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[PartnerAccountArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create and manage partner account

        :param str resource_name: The name of the resource.
        :param PartnerAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PartnerAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_linked: Optional[pulumi.Input[bool]] = None,
                 partner_account_id: Optional[pulumi.Input[str]] = None,
                 partner_type: Optional[pulumi.Input['PartnerAccountPartnerType']] = None,
                 sidewalk: Optional[pulumi.Input[pulumi.InputType['PartnerAccountSidewalkAccountInfoArgs']]] = None,
                 sidewalk_response: Optional[pulumi.Input[pulumi.InputType['PartnerAccountSidewalkAccountInfoWithFingerprintArgs']]] = None,
                 sidewalk_update: Optional[pulumi.Input[pulumi.InputType['PartnerAccountSidewalkUpdateAccountArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""PartnerAccount is deprecated: PartnerAccount is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PartnerAccountArgs.__new__(PartnerAccountArgs)

            __props__.__dict__["account_linked"] = account_linked
            __props__.__dict__["partner_account_id"] = partner_account_id
            __props__.__dict__["partner_type"] = partner_type
            __props__.__dict__["sidewalk"] = sidewalk
            __props__.__dict__["sidewalk_response"] = sidewalk_response
            __props__.__dict__["sidewalk_update"] = sidewalk_update
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["fingerprint"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["partner_account_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(PartnerAccount, __self__).__init__(
            'aws-native:iotwireless:PartnerAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PartnerAccount':
        """
        Get an existing PartnerAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PartnerAccountArgs.__new__(PartnerAccountArgs)

        __props__.__dict__["account_linked"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["fingerprint"] = None
        __props__.__dict__["partner_account_id"] = None
        __props__.__dict__["partner_type"] = None
        __props__.__dict__["sidewalk"] = None
        __props__.__dict__["sidewalk_response"] = None
        __props__.__dict__["sidewalk_update"] = None
        __props__.__dict__["tags"] = None
        return PartnerAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountLinked")
    def account_linked(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the partner account is linked to the AWS account.
        """
        return pulumi.get(self, "account_linked")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        PartnerAccount arn. Returned after successful create.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        """
        The fingerprint of the Sidewalk application server private key.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter(name="partnerAccountId")
    def partner_account_id(self) -> pulumi.Output[Optional[str]]:
        """
        The partner account ID to disassociate from the AWS account
        """
        return pulumi.get(self, "partner_account_id")

    @property
    @pulumi.getter(name="partnerType")
    def partner_type(self) -> pulumi.Output[Optional['PartnerAccountPartnerType']]:
        """
        The partner type
        """
        return pulumi.get(self, "partner_type")

    @property
    @pulumi.getter
    def sidewalk(self) -> pulumi.Output[Optional['outputs.PartnerAccountSidewalkAccountInfo']]:
        """
        The Sidewalk account credentials.
        """
        return pulumi.get(self, "sidewalk")

    @property
    @pulumi.getter(name="sidewalkResponse")
    def sidewalk_response(self) -> pulumi.Output[Optional['outputs.PartnerAccountSidewalkAccountInfoWithFingerprint']]:
        """
        The Sidewalk account credentials.
        """
        return pulumi.get(self, "sidewalk_response")

    @property
    @pulumi.getter(name="sidewalkUpdate")
    def sidewalk_update(self) -> pulumi.Output[Optional['outputs.PartnerAccountSidewalkUpdateAccount']]:
        """
        The Sidewalk account credentials.
        """
        return pulumi.get(self, "sidewalk_update")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        A list of key-value pairs that contain metadata for the destination.
        """
        return pulumi.get(self, "tags")

