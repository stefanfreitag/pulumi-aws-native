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

__all__ = [
    'GetSigningProfileResult',
    'AwaitableGetSigningProfileResult',
    'get_signing_profile',
    'get_signing_profile_output',
]

@pulumi.output_type
class GetSigningProfileResult:
    def __init__(__self__, arn=None, profile_name=None, profile_version=None, profile_version_arn=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if profile_name and not isinstance(profile_name, str):
            raise TypeError("Expected argument 'profile_name' to be a str")
        pulumi.set(__self__, "profile_name", profile_name)
        if profile_version and not isinstance(profile_version, str):
            raise TypeError("Expected argument 'profile_version' to be a str")
        pulumi.set(__self__, "profile_version", profile_version)
        if profile_version_arn and not isinstance(profile_version_arn, str):
            raise TypeError("Expected argument 'profile_version_arn' to be a str")
        pulumi.set(__self__, "profile_version_arn", profile_version_arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the specified signing profile.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> Optional[str]:
        """
        A name for the signing profile. AWS CloudFormation generates a unique physical ID and uses that ID for the signing profile name. 
        """
        return pulumi.get(self, "profile_name")

    @property
    @pulumi.getter(name="profileVersion")
    def profile_version(self) -> Optional[str]:
        """
        A version for the signing profile. AWS Signer generates a unique version for each profile of the same profile name.
        """
        return pulumi.get(self, "profile_version")

    @property
    @pulumi.getter(name="profileVersionArn")
    def profile_version_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the specified signing profile version.
        """
        return pulumi.get(self, "profile_version_arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.SigningProfileTag']]:
        """
        A list of tags associated with the signing profile.
        """
        return pulumi.get(self, "tags")


class AwaitableGetSigningProfileResult(GetSigningProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSigningProfileResult(
            arn=self.arn,
            profile_name=self.profile_name,
            profile_version=self.profile_version,
            profile_version_arn=self.profile_version_arn,
            tags=self.tags)


def get_signing_profile(arn: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSigningProfileResult:
    """
    A signing profile is a signing template that can be used to carry out a pre-defined signing job.


    :param str arn: The Amazon Resource Name (ARN) of the specified signing profile.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:signer:getSigningProfile', __args__, opts=opts, typ=GetSigningProfileResult).value

    return AwaitableGetSigningProfileResult(
        arn=pulumi.get(__ret__, 'arn'),
        profile_name=pulumi.get(__ret__, 'profile_name'),
        profile_version=pulumi.get(__ret__, 'profile_version'),
        profile_version_arn=pulumi.get(__ret__, 'profile_version_arn'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_signing_profile)
def get_signing_profile_output(arn: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSigningProfileResult]:
    """
    A signing profile is a signing template that can be used to carry out a pre-defined signing job.


    :param str arn: The Amazon Resource Name (ARN) of the specified signing profile.
    """
    ...
