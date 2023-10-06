# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['NetworkInterfacePermissionArgs', 'NetworkInterfacePermission']

@pulumi.input_type
class NetworkInterfacePermissionArgs:
    def __init__(__self__, *,
                 aws_account_id: pulumi.Input[str],
                 network_interface_id: pulumi.Input[str],
                 permission: pulumi.Input[str]):
        """
        The set of arguments for constructing a NetworkInterfacePermission resource.
        """
        NetworkInterfacePermissionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            aws_account_id=aws_account_id,
            network_interface_id=network_interface_id,
            permission=permission,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             aws_account_id: pulumi.Input[str],
             network_interface_id: pulumi.Input[str],
             permission: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("aws_account_id", aws_account_id)
        _setter("network_interface_id", network_interface_id)
        _setter("permission", permission)

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "aws_account_id")

    @aws_account_id.setter
    def aws_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "aws_account_id", value)

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "network_interface_id")

    @network_interface_id.setter
    def network_interface_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_interface_id", value)

    @property
    @pulumi.getter
    def permission(self) -> pulumi.Input[str]:
        return pulumi.get(self, "permission")

    @permission.setter
    def permission(self, value: pulumi.Input[str]):
        pulumi.set(self, "permission", value)


warnings.warn("""NetworkInterfacePermission is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class NetworkInterfacePermission(pulumi.CustomResource):
    warnings.warn("""NetworkInterfacePermission is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 permission: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::NetworkInterfacePermission

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkInterfacePermissionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::NetworkInterfacePermission

        :param str resource_name: The name of the resource.
        :param NetworkInterfacePermissionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkInterfacePermissionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            NetworkInterfacePermissionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_account_id: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 permission: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""NetworkInterfacePermission is deprecated: NetworkInterfacePermission is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkInterfacePermissionArgs.__new__(NetworkInterfacePermissionArgs)

            if aws_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'aws_account_id'")
            __props__.__dict__["aws_account_id"] = aws_account_id
            if network_interface_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_interface_id'")
            __props__.__dict__["network_interface_id"] = network_interface_id
            if permission is None and not opts.urn:
                raise TypeError("Missing required property 'permission'")
            __props__.__dict__["permission"] = permission
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["aws_account_id", "network_interface_id", "permission"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(NetworkInterfacePermission, __self__).__init__(
            'aws-native:ec2:NetworkInterfacePermission',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkInterfacePermission':
        """
        Get an existing NetworkInterfacePermission resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkInterfacePermissionArgs.__new__(NetworkInterfacePermissionArgs)

        __props__.__dict__["aws_account_id"] = None
        __props__.__dict__["network_interface_id"] = None
        __props__.__dict__["permission"] = None
        return NetworkInterfacePermission(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "aws_account_id")

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "network_interface_id")

    @property
    @pulumi.getter
    def permission(self) -> pulumi.Output[str]:
        return pulumi.get(self, "permission")

