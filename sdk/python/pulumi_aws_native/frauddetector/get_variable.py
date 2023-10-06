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
from ._enums import *

__all__ = [
    'GetVariableResult',
    'AwaitableGetVariableResult',
    'get_variable',
    'get_variable_output',
]

@pulumi.output_type
class GetVariableResult:
    def __init__(__self__, arn=None, created_time=None, data_source=None, data_type=None, default_value=None, description=None, last_updated_time=None, tags=None, variable_type=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if data_source and not isinstance(data_source, str):
            raise TypeError("Expected argument 'data_source' to be a str")
        pulumi.set(__self__, "data_source", data_source)
        if data_type and not isinstance(data_type, str):
            raise TypeError("Expected argument 'data_type' to be a str")
        pulumi.set(__self__, "data_type", data_type)
        if default_value and not isinstance(default_value, str):
            raise TypeError("Expected argument 'default_value' to be a str")
        pulumi.set(__self__, "default_value", default_value)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if last_updated_time and not isinstance(last_updated_time, str):
            raise TypeError("Expected argument 'last_updated_time' to be a str")
        pulumi.set(__self__, "last_updated_time", last_updated_time)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if variable_type and not isinstance(variable_type, str):
            raise TypeError("Expected argument 'variable_type' to be a str")
        pulumi.set(__self__, "variable_type", variable_type)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The ARN of the variable.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[str]:
        """
        The time when the variable was created.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional['VariableDataSource']:
        """
        The source of the data.
        """
        return pulumi.get(self, "data_source")

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional['VariableDataType']:
        """
        The data type.
        """
        return pulumi.get(self, "data_type")

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[str]:
        """
        The default value for the variable when no value is received.
        """
        return pulumi.get(self, "default_value")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[str]:
        """
        The time when the variable was last updated.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.VariableTag']]:
        """
        Tags associated with this variable.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="variableType")
    def variable_type(self) -> Optional['VariableType']:
        """
        The variable type. For more information see https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types
        """
        return pulumi.get(self, "variable_type")


class AwaitableGetVariableResult(GetVariableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVariableResult(
            arn=self.arn,
            created_time=self.created_time,
            data_source=self.data_source,
            data_type=self.data_type,
            default_value=self.default_value,
            description=self.description,
            last_updated_time=self.last_updated_time,
            tags=self.tags,
            variable_type=self.variable_type)


def get_variable(arn: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVariableResult:
    """
    A resource schema for a Variable in Amazon Fraud Detector.


    :param str arn: The ARN of the variable.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:frauddetector:getVariable', __args__, opts=opts, typ=GetVariableResult).value

    return AwaitableGetVariableResult(
        arn=pulumi.get(__ret__, 'arn'),
        created_time=pulumi.get(__ret__, 'created_time'),
        data_source=pulumi.get(__ret__, 'data_source'),
        data_type=pulumi.get(__ret__, 'data_type'),
        default_value=pulumi.get(__ret__, 'default_value'),
        description=pulumi.get(__ret__, 'description'),
        last_updated_time=pulumi.get(__ret__, 'last_updated_time'),
        tags=pulumi.get(__ret__, 'tags'),
        variable_type=pulumi.get(__ret__, 'variable_type'))


@_utilities.lift_output_func(get_variable)
def get_variable_output(arn: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVariableResult]:
    """
    A resource schema for a Variable in Amazon Fraud Detector.


    :param str arn: The ARN of the variable.
    """
    ...
