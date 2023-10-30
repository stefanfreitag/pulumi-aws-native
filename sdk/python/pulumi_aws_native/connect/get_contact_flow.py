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
    'GetContactFlowResult',
    'AwaitableGetContactFlowResult',
    'get_contact_flow',
    'get_contact_flow_output',
]

@pulumi.output_type
class GetContactFlowResult:
    def __init__(__self__, contact_flow_arn=None, content=None, description=None, instance_arn=None, name=None, state=None, tags=None):
        if contact_flow_arn and not isinstance(contact_flow_arn, str):
            raise TypeError("Expected argument 'contact_flow_arn' to be a str")
        pulumi.set(__self__, "contact_flow_arn", contact_flow_arn)
        if content and not isinstance(content, str):
            raise TypeError("Expected argument 'content' to be a str")
        pulumi.set(__self__, "content", content)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if instance_arn and not isinstance(instance_arn, str):
            raise TypeError("Expected argument 'instance_arn' to be a str")
        pulumi.set(__self__, "instance_arn", instance_arn)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="contactFlowArn")
    def contact_flow_arn(self) -> Optional[str]:
        """
        The identifier of the contact flow (ARN).
        """
        return pulumi.get(self, "contact_flow_arn")

    @property
    @pulumi.getter
    def content(self) -> Optional[str]:
        """
        The content of the contact flow in JSON format.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the contact flow.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> Optional[str]:
        """
        The identifier of the Amazon Connect instance (ARN).
        """
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the contact flow.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> Optional['ContactFlowState']:
        """
        The state of the contact flow.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ContactFlowTag']]:
        """
        One or more tags.
        """
        return pulumi.get(self, "tags")


class AwaitableGetContactFlowResult(GetContactFlowResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContactFlowResult(
            contact_flow_arn=self.contact_flow_arn,
            content=self.content,
            description=self.description,
            instance_arn=self.instance_arn,
            name=self.name,
            state=self.state,
            tags=self.tags)


def get_contact_flow(contact_flow_arn: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContactFlowResult:
    """
    Resource Type definition for AWS::Connect::ContactFlow


    :param str contact_flow_arn: The identifier of the contact flow (ARN).
    """
    __args__ = dict()
    __args__['contactFlowArn'] = contact_flow_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:connect:getContactFlow', __args__, opts=opts, typ=GetContactFlowResult).value

    return AwaitableGetContactFlowResult(
        contact_flow_arn=pulumi.get(__ret__, 'contact_flow_arn'),
        content=pulumi.get(__ret__, 'content'),
        description=pulumi.get(__ret__, 'description'),
        instance_arn=pulumi.get(__ret__, 'instance_arn'),
        name=pulumi.get(__ret__, 'name'),
        state=pulumi.get(__ret__, 'state'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_contact_flow)
def get_contact_flow_output(contact_flow_arn: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContactFlowResult]:
    """
    Resource Type definition for AWS::Connect::ContactFlow


    :param str contact_flow_arn: The identifier of the contact flow (ARN).
    """
    ...
