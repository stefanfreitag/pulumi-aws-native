# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DbSecurityGroupIngressInitArgs', 'DbSecurityGroupIngress']

@pulumi.input_type
class DbSecurityGroupIngressInitArgs:
    def __init__(__self__, *,
                 db_security_group_name: pulumi.Input[str],
                 cidrip: Optional[pulumi.Input[str]] = None,
                 ec2_security_group_id: Optional[pulumi.Input[str]] = None,
                 ec2_security_group_name: Optional[pulumi.Input[str]] = None,
                 ec2_security_group_owner_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DbSecurityGroupIngress resource.
        """
        DbSecurityGroupIngressInitArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            db_security_group_name=db_security_group_name,
            cidrip=cidrip,
            ec2_security_group_id=ec2_security_group_id,
            ec2_security_group_name=ec2_security_group_name,
            ec2_security_group_owner_id=ec2_security_group_owner_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             db_security_group_name: pulumi.Input[str],
             cidrip: Optional[pulumi.Input[str]] = None,
             ec2_security_group_id: Optional[pulumi.Input[str]] = None,
             ec2_security_group_name: Optional[pulumi.Input[str]] = None,
             ec2_security_group_owner_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("db_security_group_name", db_security_group_name)
        if cidrip is not None:
            _setter("cidrip", cidrip)
        if ec2_security_group_id is not None:
            _setter("ec2_security_group_id", ec2_security_group_id)
        if ec2_security_group_name is not None:
            _setter("ec2_security_group_name", ec2_security_group_name)
        if ec2_security_group_owner_id is not None:
            _setter("ec2_security_group_owner_id", ec2_security_group_owner_id)

    @property
    @pulumi.getter(name="dbSecurityGroupName")
    def db_security_group_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "db_security_group_name")

    @db_security_group_name.setter
    def db_security_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "db_security_group_name", value)

    @property
    @pulumi.getter
    def cidrip(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cidrip")

    @cidrip.setter
    def cidrip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidrip", value)

    @property
    @pulumi.getter(name="ec2SecurityGroupId")
    def ec2_security_group_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ec2_security_group_id")

    @ec2_security_group_id.setter
    def ec2_security_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ec2_security_group_id", value)

    @property
    @pulumi.getter(name="ec2SecurityGroupName")
    def ec2_security_group_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ec2_security_group_name")

    @ec2_security_group_name.setter
    def ec2_security_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ec2_security_group_name", value)

    @property
    @pulumi.getter(name="ec2SecurityGroupOwnerId")
    def ec2_security_group_owner_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ec2_security_group_owner_id")

    @ec2_security_group_owner_id.setter
    def ec2_security_group_owner_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ec2_security_group_owner_id", value)


warnings.warn("""DbSecurityGroupIngress is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class DbSecurityGroupIngress(pulumi.CustomResource):
    warnings.warn("""DbSecurityGroupIngress is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidrip: Optional[pulumi.Input[str]] = None,
                 db_security_group_name: Optional[pulumi.Input[str]] = None,
                 ec2_security_group_id: Optional[pulumi.Input[str]] = None,
                 ec2_security_group_name: Optional[pulumi.Input[str]] = None,
                 ec2_security_group_owner_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::RDS::DBSecurityGroupIngress

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DbSecurityGroupIngressInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::RDS::DBSecurityGroupIngress

        :param str resource_name: The name of the resource.
        :param DbSecurityGroupIngressInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DbSecurityGroupIngressInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DbSecurityGroupIngressInitArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidrip: Optional[pulumi.Input[str]] = None,
                 db_security_group_name: Optional[pulumi.Input[str]] = None,
                 ec2_security_group_id: Optional[pulumi.Input[str]] = None,
                 ec2_security_group_name: Optional[pulumi.Input[str]] = None,
                 ec2_security_group_owner_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""DbSecurityGroupIngress is deprecated: DbSecurityGroupIngress is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DbSecurityGroupIngressInitArgs.__new__(DbSecurityGroupIngressInitArgs)

            __props__.__dict__["cidrip"] = cidrip
            if db_security_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'db_security_group_name'")
            __props__.__dict__["db_security_group_name"] = db_security_group_name
            __props__.__dict__["ec2_security_group_id"] = ec2_security_group_id
            __props__.__dict__["ec2_security_group_name"] = ec2_security_group_name
            __props__.__dict__["ec2_security_group_owner_id"] = ec2_security_group_owner_id
        super(DbSecurityGroupIngress, __self__).__init__(
            'aws-native:rds:DbSecurityGroupIngress',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DbSecurityGroupIngress':
        """
        Get an existing DbSecurityGroupIngress resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DbSecurityGroupIngressInitArgs.__new__(DbSecurityGroupIngressInitArgs)

        __props__.__dict__["cidrip"] = None
        __props__.__dict__["db_security_group_name"] = None
        __props__.__dict__["ec2_security_group_id"] = None
        __props__.__dict__["ec2_security_group_name"] = None
        __props__.__dict__["ec2_security_group_owner_id"] = None
        return DbSecurityGroupIngress(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cidrip(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "cidrip")

    @property
    @pulumi.getter(name="dbSecurityGroupName")
    def db_security_group_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "db_security_group_name")

    @property
    @pulumi.getter(name="ec2SecurityGroupId")
    def ec2_security_group_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ec2_security_group_id")

    @property
    @pulumi.getter(name="ec2SecurityGroupName")
    def ec2_security_group_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ec2_security_group_name")

    @property
    @pulumi.getter(name="ec2SecurityGroupOwnerId")
    def ec2_security_group_owner_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ec2_security_group_owner_id")

