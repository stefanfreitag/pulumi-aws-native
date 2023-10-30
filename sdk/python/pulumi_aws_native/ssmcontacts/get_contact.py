# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetContactResult',
    'AwaitableGetContactResult',
    'get_contact',
    'get_contact_output',
]

@pulumi.output_type
class GetContactResult:
    def __init__(__self__, arn=None, display_name=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the contact.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Name of the contact. String value with 3 to 256 characters. Only alphabetical, space, numeric characters, dash, or underscore allowed.
        """
        return pulumi.get(self, "display_name")


class AwaitableGetContactResult(GetContactResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContactResult(
            arn=self.arn,
            display_name=self.display_name)


def get_contact(arn: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContactResult:
    """
    Resource Type definition for AWS::SSMContacts::Contact


    :param str arn: The Amazon Resource Name (ARN) of the contact.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ssmcontacts:getContact', __args__, opts=opts, typ=GetContactResult).value

    return AwaitableGetContactResult(
        arn=pulumi.get(__ret__, 'arn'),
        display_name=pulumi.get(__ret__, 'display_name'))


@_utilities.lift_output_func(get_contact)
def get_contact_output(arn: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContactResult]:
    """
    Resource Type definition for AWS::SSMContacts::Contact


    :param str arn: The Amazon Resource Name (ARN) of the contact.
    """
    ...
