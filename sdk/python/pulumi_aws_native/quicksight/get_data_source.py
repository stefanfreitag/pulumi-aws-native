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
    'GetDataSourceResult',
    'AwaitableGetDataSourceResult',
    'get_data_source',
    'get_data_source_output',
]

@pulumi.output_type
class GetDataSourceResult:
    def __init__(__self__, alternate_data_source_parameters=None, arn=None, created_time=None, data_source_parameters=None, error_info=None, last_updated_time=None, name=None, permissions=None, ssl_properties=None, status=None, tags=None, vpc_connection_properties=None):
        if alternate_data_source_parameters and not isinstance(alternate_data_source_parameters, list):
            raise TypeError("Expected argument 'alternate_data_source_parameters' to be a list")
        pulumi.set(__self__, "alternate_data_source_parameters", alternate_data_source_parameters)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if data_source_parameters and not isinstance(data_source_parameters, dict):
            raise TypeError("Expected argument 'data_source_parameters' to be a dict")
        pulumi.set(__self__, "data_source_parameters", data_source_parameters)
        if error_info and not isinstance(error_info, dict):
            raise TypeError("Expected argument 'error_info' to be a dict")
        pulumi.set(__self__, "error_info", error_info)
        if last_updated_time and not isinstance(last_updated_time, str):
            raise TypeError("Expected argument 'last_updated_time' to be a str")
        pulumi.set(__self__, "last_updated_time", last_updated_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if permissions and not isinstance(permissions, list):
            raise TypeError("Expected argument 'permissions' to be a list")
        pulumi.set(__self__, "permissions", permissions)
        if ssl_properties and not isinstance(ssl_properties, dict):
            raise TypeError("Expected argument 'ssl_properties' to be a dict")
        pulumi.set(__self__, "ssl_properties", ssl_properties)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if vpc_connection_properties and not isinstance(vpc_connection_properties, dict):
            raise TypeError("Expected argument 'vpc_connection_properties' to be a dict")
        pulumi.set(__self__, "vpc_connection_properties", vpc_connection_properties)

    @property
    @pulumi.getter(name="alternateDataSourceParameters")
    def alternate_data_source_parameters(self) -> Optional[Sequence['outputs.DataSourceParameters']]:
        """
        <p>A set of alternate data source parameters that you want to share for the credentials
                    stored with this data source. The credentials are applied in tandem with the data source
                    parameters when you copy a data source by using a create or update request. The API
                    operation compares the <code>DataSourceParameters</code> structure that's in the request
                    with the structures in the <code>AlternateDataSourceParameters</code> allow list. If the
                    structures are an exact match, the request is allowed to use the credentials from this
                    existing data source. If the <code>AlternateDataSourceParameters</code> list is null,
                    the <code>Credentials</code> originally used with this <code>DataSourceParameters</code>
                    are automatically allowed.</p>
        """
        return pulumi.get(self, "alternate_data_source_parameters")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        <p>The Amazon Resource Name (ARN) of the data source.</p>
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[str]:
        """
        <p>The time that this data source was created.</p>
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="dataSourceParameters")
    def data_source_parameters(self) -> Optional['outputs.DataSourceParameters']:
        return pulumi.get(self, "data_source_parameters")

    @property
    @pulumi.getter(name="errorInfo")
    def error_info(self) -> Optional['outputs.DataSourceErrorInfo']:
        return pulumi.get(self, "error_info")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[str]:
        """
        <p>The last time that this data source was updated.</p>
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        <p>A display name for the data source.</p>
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permissions(self) -> Optional[Sequence['outputs.DataSourceResourcePermission']]:
        """
        <p>A list of resource permissions on the data source.</p>
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="sslProperties")
    def ssl_properties(self) -> Optional['outputs.DataSourceSslProperties']:
        return pulumi.get(self, "ssl_properties")

    @property
    @pulumi.getter
    def status(self) -> Optional['DataSourceResourceStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.</p>
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcConnectionProperties")
    def vpc_connection_properties(self) -> Optional['outputs.DataSourceVpcConnectionProperties']:
        return pulumi.get(self, "vpc_connection_properties")


class AwaitableGetDataSourceResult(GetDataSourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataSourceResult(
            alternate_data_source_parameters=self.alternate_data_source_parameters,
            arn=self.arn,
            created_time=self.created_time,
            data_source_parameters=self.data_source_parameters,
            error_info=self.error_info,
            last_updated_time=self.last_updated_time,
            name=self.name,
            permissions=self.permissions,
            ssl_properties=self.ssl_properties,
            status=self.status,
            tags=self.tags,
            vpc_connection_properties=self.vpc_connection_properties)


def get_data_source(aws_account_id: Optional[str] = None,
                    data_source_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataSourceResult:
    """
    Definition of the AWS::QuickSight::DataSource Resource Type.
    """
    __args__ = dict()
    __args__['awsAccountId'] = aws_account_id
    __args__['dataSourceId'] = data_source_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:quicksight:getDataSource', __args__, opts=opts, typ=GetDataSourceResult).value

    return AwaitableGetDataSourceResult(
        alternate_data_source_parameters=pulumi.get(__ret__, 'alternate_data_source_parameters'),
        arn=pulumi.get(__ret__, 'arn'),
        created_time=pulumi.get(__ret__, 'created_time'),
        data_source_parameters=pulumi.get(__ret__, 'data_source_parameters'),
        error_info=pulumi.get(__ret__, 'error_info'),
        last_updated_time=pulumi.get(__ret__, 'last_updated_time'),
        name=pulumi.get(__ret__, 'name'),
        permissions=pulumi.get(__ret__, 'permissions'),
        ssl_properties=pulumi.get(__ret__, 'ssl_properties'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'),
        vpc_connection_properties=pulumi.get(__ret__, 'vpc_connection_properties'))


@_utilities.lift_output_func(get_data_source)
def get_data_source_output(aws_account_id: Optional[pulumi.Input[str]] = None,
                           data_source_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDataSourceResult]:
    """
    Definition of the AWS::QuickSight::DataSource Resource Type.
    """
    ...
