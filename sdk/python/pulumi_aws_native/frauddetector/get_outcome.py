# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import outputs as _root_outputs

__all__ = [
    'GetOutcomeResult',
    'AwaitableGetOutcomeResult',
    'get_outcome',
    'get_outcome_output',
]

@pulumi.output_type
class GetOutcomeResult:
    def __init__(__self__, arn=None, created_time=None, description=None, last_updated_time=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if last_updated_time and not isinstance(last_updated_time, str):
            raise TypeError("Expected argument 'last_updated_time' to be a str")
        pulumi.set(__self__, "last_updated_time", last_updated_time)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The outcome ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[str]:
        """
        The timestamp when the outcome was created.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The outcome description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[str]:
        """
        The timestamp when the outcome was last updated.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        Tags associated with this outcome.
        """
        return pulumi.get(self, "tags")


class AwaitableGetOutcomeResult(GetOutcomeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOutcomeResult(
            arn=self.arn,
            created_time=self.created_time,
            description=self.description,
            last_updated_time=self.last_updated_time,
            tags=self.tags)


def get_outcome(arn: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOutcomeResult:
    """
    An outcome for rule evaluation.


    :param str arn: The outcome ARN.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:frauddetector:getOutcome', __args__, opts=opts, typ=GetOutcomeResult).value

    return AwaitableGetOutcomeResult(
        arn=pulumi.get(__ret__, 'arn'),
        created_time=pulumi.get(__ret__, 'created_time'),
        description=pulumi.get(__ret__, 'description'),
        last_updated_time=pulumi.get(__ret__, 'last_updated_time'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_outcome)
def get_outcome_output(arn: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOutcomeResult]:
    """
    An outcome for rule evaluation.


    :param str arn: The outcome ARN.
    """
    ...
