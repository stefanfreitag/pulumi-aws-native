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
    'GetInstanceResult',
    'AwaitableGetInstanceResult',
    'get_instance',
    'get_instance_output',
]

@pulumi.output_type
class GetInstanceResult:
    def __init__(__self__, arn=None, attributes=None, created_time=None, id=None, instance_status=None, service_role=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if attributes and not isinstance(attributes, dict):
            raise TypeError("Expected argument 'attributes' to be a dict")
        pulumi.set(__self__, "attributes", attributes)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_status and not isinstance(instance_status, str):
            raise TypeError("Expected argument 'instance_status' to be a str")
        pulumi.set(__self__, "instance_status", instance_status)
        if service_role and not isinstance(service_role, str):
            raise TypeError("Expected argument 'service_role' to be a str")
        pulumi.set(__self__, "service_role", service_role)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        An instanceArn is automatically generated on creation based on instanceId.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def attributes(self) -> Optional['outputs.InstanceAttributes']:
        """
        The attributes for the instance.
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[str]:
        """
        Timestamp of instance creation logged as part of instance creation.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        An instanceId is automatically generated on creation and assigned as the unique identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceStatus")
    def instance_status(self) -> Optional['InstanceStatus']:
        """
        Specifies the creation status of new instance.
        """
        return pulumi.get(self, "instance_status")

    @property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> Optional[str]:
        """
        Service linked role created as part of instance creation.
        """
        return pulumi.get(self, "service_role")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetInstanceResult(GetInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceResult(
            arn=self.arn,
            attributes=self.attributes,
            created_time=self.created_time,
            id=self.id,
            instance_status=self.instance_status,
            service_role=self.service_role,
            tags=self.tags)


def get_instance(arn: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceResult:
    """
    Resource Type definition for AWS::Connect::Instance


    :param str arn: An instanceArn is automatically generated on creation based on instanceId.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:connect:getInstance', __args__, opts=opts, typ=GetInstanceResult).value

    return AwaitableGetInstanceResult(
        arn=pulumi.get(__ret__, 'arn'),
        attributes=pulumi.get(__ret__, 'attributes'),
        created_time=pulumi.get(__ret__, 'created_time'),
        id=pulumi.get(__ret__, 'id'),
        instance_status=pulumi.get(__ret__, 'instance_status'),
        service_role=pulumi.get(__ret__, 'service_role'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_instance)
def get_instance_output(arn: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceResult]:
    """
    Resource Type definition for AWS::Connect::Instance


    :param str arn: An instanceArn is automatically generated on creation based on instanceId.
    """
    ...
