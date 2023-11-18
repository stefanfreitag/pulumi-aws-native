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

__all__ = [
    'GetPipeResult',
    'AwaitableGetPipeResult',
    'get_pipe',
    'get_pipe_output',
]

@pulumi.output_type
class GetPipeResult:
    def __init__(__self__, arn=None, creation_time=None, current_state=None, description=None, desired_state=None, enrichment=None, enrichment_parameters=None, last_modified_time=None, log_configuration=None, role_arn=None, state_reason=None, tags=None, target=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if current_state and not isinstance(current_state, str):
            raise TypeError("Expected argument 'current_state' to be a str")
        pulumi.set(__self__, "current_state", current_state)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if desired_state and not isinstance(desired_state, str):
            raise TypeError("Expected argument 'desired_state' to be a str")
        pulumi.set(__self__, "desired_state", desired_state)
        if enrichment and not isinstance(enrichment, str):
            raise TypeError("Expected argument 'enrichment' to be a str")
        pulumi.set(__self__, "enrichment", enrichment)
        if enrichment_parameters and not isinstance(enrichment_parameters, dict):
            raise TypeError("Expected argument 'enrichment_parameters' to be a dict")
        pulumi.set(__self__, "enrichment_parameters", enrichment_parameters)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if log_configuration and not isinstance(log_configuration, dict):
            raise TypeError("Expected argument 'log_configuration' to be a dict")
        pulumi.set(__self__, "log_configuration", log_configuration)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if state_reason and not isinstance(state_reason, str):
            raise TypeError("Expected argument 'state_reason' to be a str")
        pulumi.set(__self__, "state_reason", state_reason)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if target and not isinstance(target, str):
            raise TypeError("Expected argument 'target' to be a str")
        pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="currentState")
    def current_state(self) -> Optional['PipeState']:
        return pulumi.get(self, "current_state")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional['PipeRequestedPipeState']:
        return pulumi.get(self, "desired_state")

    @property
    @pulumi.getter
    def enrichment(self) -> Optional[str]:
        return pulumi.get(self, "enrichment")

    @property
    @pulumi.getter(name="enrichmentParameters")
    def enrichment_parameters(self) -> Optional['outputs.PipeEnrichmentParameters']:
        return pulumi.get(self, "enrichment_parameters")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[str]:
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(self) -> Optional['outputs.PipeLogConfiguration']:
        return pulumi.get(self, "log_configuration")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> Optional[str]:
        return pulumi.get(self, "state_reason")

    @property
    @pulumi.getter
    def tags(self) -> Optional['outputs.PipeTagMap']:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def target(self) -> Optional[str]:
        return pulumi.get(self, "target")


class AwaitableGetPipeResult(GetPipeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPipeResult(
            arn=self.arn,
            creation_time=self.creation_time,
            current_state=self.current_state,
            description=self.description,
            desired_state=self.desired_state,
            enrichment=self.enrichment,
            enrichment_parameters=self.enrichment_parameters,
            last_modified_time=self.last_modified_time,
            log_configuration=self.log_configuration,
            role_arn=self.role_arn,
            state_reason=self.state_reason,
            tags=self.tags,
            target=self.target)


def get_pipe(name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPipeResult:
    """
    Definition of AWS::Pipes::Pipe Resource Type
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:pipes:getPipe', __args__, opts=opts, typ=GetPipeResult).value

    return AwaitableGetPipeResult(
        arn=pulumi.get(__ret__, 'arn'),
        creation_time=pulumi.get(__ret__, 'creation_time'),
        current_state=pulumi.get(__ret__, 'current_state'),
        description=pulumi.get(__ret__, 'description'),
        desired_state=pulumi.get(__ret__, 'desired_state'),
        enrichment=pulumi.get(__ret__, 'enrichment'),
        enrichment_parameters=pulumi.get(__ret__, 'enrichment_parameters'),
        last_modified_time=pulumi.get(__ret__, 'last_modified_time'),
        log_configuration=pulumi.get(__ret__, 'log_configuration'),
        role_arn=pulumi.get(__ret__, 'role_arn'),
        state_reason=pulumi.get(__ret__, 'state_reason'),
        tags=pulumi.get(__ret__, 'tags'),
        target=pulumi.get(__ret__, 'target'))


@_utilities.lift_output_func(get_pipe)
def get_pipe_output(name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPipeResult]:
    """
    Definition of AWS::Pipes::Pipe Resource Type
    """
    ...
