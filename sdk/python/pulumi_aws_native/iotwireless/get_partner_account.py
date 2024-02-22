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
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetPartnerAccountResult',
    'AwaitableGetPartnerAccountResult',
    'get_partner_account',
    'get_partner_account_output',
]

@pulumi.output_type
class GetPartnerAccountResult:
    def __init__(__self__, account_linked=None, arn=None, fingerprint=None, partner_type=None, sidewalk_response=None, tags=None):
        if account_linked and not isinstance(account_linked, bool):
            raise TypeError("Expected argument 'account_linked' to be a bool")
        pulumi.set(__self__, "account_linked", account_linked)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        pulumi.set(__self__, "fingerprint", fingerprint)
        if partner_type and not isinstance(partner_type, str):
            raise TypeError("Expected argument 'partner_type' to be a str")
        pulumi.set(__self__, "partner_type", partner_type)
        if sidewalk_response and not isinstance(sidewalk_response, dict):
            raise TypeError("Expected argument 'sidewalk_response' to be a dict")
        pulumi.set(__self__, "sidewalk_response", sidewalk_response)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="accountLinked")
    def account_linked(self) -> Optional[bool]:
        """
        Whether the partner account is linked to the AWS account.
        """
        return pulumi.get(self, "account_linked")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        PartnerAccount arn. Returned after successful create.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def fingerprint(self) -> Optional[str]:
        """
        The fingerprint of the Sidewalk application server private key.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter(name="partnerType")
    def partner_type(self) -> Optional['PartnerAccountPartnerType']:
        """
        The partner type
        """
        return pulumi.get(self, "partner_type")

    @property
    @pulumi.getter(name="sidewalkResponse")
    def sidewalk_response(self) -> Optional['outputs.PartnerAccountSidewalkAccountInfoWithFingerprint']:
        """
        The Sidewalk account credentials.
        """
        return pulumi.get(self, "sidewalk_response")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        A list of key-value pairs that contain metadata for the destination.
        """
        return pulumi.get(self, "tags")


class AwaitableGetPartnerAccountResult(GetPartnerAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPartnerAccountResult(
            account_linked=self.account_linked,
            arn=self.arn,
            fingerprint=self.fingerprint,
            partner_type=self.partner_type,
            sidewalk_response=self.sidewalk_response,
            tags=self.tags)


def get_partner_account(partner_account_id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPartnerAccountResult:
    """
    Create and manage partner account


    :param str partner_account_id: The partner account ID to disassociate from the AWS account
    """
    __args__ = dict()
    __args__['partnerAccountId'] = partner_account_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iotwireless:getPartnerAccount', __args__, opts=opts, typ=GetPartnerAccountResult).value

    return AwaitableGetPartnerAccountResult(
        account_linked=pulumi.get(__ret__, 'account_linked'),
        arn=pulumi.get(__ret__, 'arn'),
        fingerprint=pulumi.get(__ret__, 'fingerprint'),
        partner_type=pulumi.get(__ret__, 'partner_type'),
        sidewalk_response=pulumi.get(__ret__, 'sidewalk_response'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_partner_account)
def get_partner_account_output(partner_account_id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPartnerAccountResult]:
    """
    Create and manage partner account


    :param str partner_account_id: The partner account ID to disassociate from the AWS account
    """
    ...
