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
    'GetRemediationConfigurationResult',
    'AwaitableGetRemediationConfigurationResult',
    'get_remediation_configuration',
    'get_remediation_configuration_output',
]

@pulumi.output_type
class GetRemediationConfigurationResult:
    def __init__(__self__, automatic=None, execution_controls=None, id=None, maximum_automatic_attempts=None, parameters=None, resource_type=None, retry_attempt_seconds=None, target_id=None, target_type=None, target_version=None):
        if automatic and not isinstance(automatic, bool):
            raise TypeError("Expected argument 'automatic' to be a bool")
        pulumi.set(__self__, "automatic", automatic)
        if execution_controls and not isinstance(execution_controls, dict):
            raise TypeError("Expected argument 'execution_controls' to be a dict")
        pulumi.set(__self__, "execution_controls", execution_controls)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if maximum_automatic_attempts and not isinstance(maximum_automatic_attempts, int):
            raise TypeError("Expected argument 'maximum_automatic_attempts' to be a int")
        pulumi.set(__self__, "maximum_automatic_attempts", maximum_automatic_attempts)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if resource_type and not isinstance(resource_type, str):
            raise TypeError("Expected argument 'resource_type' to be a str")
        pulumi.set(__self__, "resource_type", resource_type)
        if retry_attempt_seconds and not isinstance(retry_attempt_seconds, int):
            raise TypeError("Expected argument 'retry_attempt_seconds' to be a int")
        pulumi.set(__self__, "retry_attempt_seconds", retry_attempt_seconds)
        if target_id and not isinstance(target_id, str):
            raise TypeError("Expected argument 'target_id' to be a str")
        pulumi.set(__self__, "target_id", target_id)
        if target_type and not isinstance(target_type, str):
            raise TypeError("Expected argument 'target_type' to be a str")
        pulumi.set(__self__, "target_type", target_type)
        if target_version and not isinstance(target_version, str):
            raise TypeError("Expected argument 'target_version' to be a str")
        pulumi.set(__self__, "target_version", target_version)

    @property
    @pulumi.getter
    def automatic(self) -> Optional[bool]:
        return pulumi.get(self, "automatic")

    @property
    @pulumi.getter(name="executionControls")
    def execution_controls(self) -> Optional['outputs.RemediationConfigurationExecutionControls']:
        return pulumi.get(self, "execution_controls")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maximumAutomaticAttempts")
    def maximum_automatic_attempts(self) -> Optional[int]:
        return pulumi.get(self, "maximum_automatic_attempts")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Any]:
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[str]:
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter(name="retryAttemptSeconds")
    def retry_attempt_seconds(self) -> Optional[int]:
        return pulumi.get(self, "retry_attempt_seconds")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[str]:
        return pulumi.get(self, "target_id")

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[str]:
        return pulumi.get(self, "target_type")

    @property
    @pulumi.getter(name="targetVersion")
    def target_version(self) -> Optional[str]:
        return pulumi.get(self, "target_version")


class AwaitableGetRemediationConfigurationResult(GetRemediationConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRemediationConfigurationResult(
            automatic=self.automatic,
            execution_controls=self.execution_controls,
            id=self.id,
            maximum_automatic_attempts=self.maximum_automatic_attempts,
            parameters=self.parameters,
            resource_type=self.resource_type,
            retry_attempt_seconds=self.retry_attempt_seconds,
            target_id=self.target_id,
            target_type=self.target_type,
            target_version=self.target_version)


def get_remediation_configuration(id: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRemediationConfigurationResult:
    """
    Resource Type definition for AWS::Config::RemediationConfiguration
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:configuration:getRemediationConfiguration', __args__, opts=opts, typ=GetRemediationConfigurationResult).value

    return AwaitableGetRemediationConfigurationResult(
        automatic=pulumi.get(__ret__, 'automatic'),
        execution_controls=pulumi.get(__ret__, 'execution_controls'),
        id=pulumi.get(__ret__, 'id'),
        maximum_automatic_attempts=pulumi.get(__ret__, 'maximum_automatic_attempts'),
        parameters=pulumi.get(__ret__, 'parameters'),
        resource_type=pulumi.get(__ret__, 'resource_type'),
        retry_attempt_seconds=pulumi.get(__ret__, 'retry_attempt_seconds'),
        target_id=pulumi.get(__ret__, 'target_id'),
        target_type=pulumi.get(__ret__, 'target_type'),
        target_version=pulumi.get(__ret__, 'target_version'))


@_utilities.lift_output_func(get_remediation_configuration)
def get_remediation_configuration_output(id: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRemediationConfigurationResult]:
    """
    Resource Type definition for AWS::Config::RemediationConfiguration
    """
    ...
