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
from ._enums import *

__all__ = [
    'GetAgentResult',
    'AwaitableGetAgentResult',
    'get_agent',
    'get_agent_output',
]

@pulumi.output_type
class GetAgentResult:
    def __init__(__self__, agent_arn=None, agent_name=None, endpoint_type=None, tags=None):
        if agent_arn and not isinstance(agent_arn, str):
            raise TypeError("Expected argument 'agent_arn' to be a str")
        pulumi.set(__self__, "agent_arn", agent_arn)
        if agent_name and not isinstance(agent_name, str):
            raise TypeError("Expected argument 'agent_name' to be a str")
        pulumi.set(__self__, "agent_name", agent_name)
        if endpoint_type and not isinstance(endpoint_type, str):
            raise TypeError("Expected argument 'endpoint_type' to be a str")
        pulumi.set(__self__, "endpoint_type", endpoint_type)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="agentArn")
    def agent_arn(self) -> Optional[str]:
        """
        The DataSync Agent ARN.
        """
        return pulumi.get(self, "agent_arn")

    @property
    @pulumi.getter(name="agentName")
    def agent_name(self) -> Optional[str]:
        """
        The name configured for the agent. Text reference used to identify the agent in the console.
        """
        return pulumi.get(self, "agent_name")

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional['AgentEndpointType']:
        """
        The service endpoints that the agent will connect to.
        """
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetAgentResult(GetAgentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAgentResult(
            agent_arn=self.agent_arn,
            agent_name=self.agent_name,
            endpoint_type=self.endpoint_type,
            tags=self.tags)


def get_agent(agent_arn: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAgentResult:
    """
    Resource schema for AWS::DataSync::Agent.


    :param str agent_arn: The DataSync Agent ARN.
    """
    __args__ = dict()
    __args__['agentArn'] = agent_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:datasync:getAgent', __args__, opts=opts, typ=GetAgentResult).value

    return AwaitableGetAgentResult(
        agent_arn=pulumi.get(__ret__, 'agent_arn'),
        agent_name=pulumi.get(__ret__, 'agent_name'),
        endpoint_type=pulumi.get(__ret__, 'endpoint_type'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_agent)
def get_agent_output(agent_arn: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAgentResult]:
    """
    Resource schema for AWS::DataSync::Agent.


    :param str agent_arn: The DataSync Agent ARN.
    """
    ...
