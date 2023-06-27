# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DBSecurityGroupIngressInitArgs', 'DBSecurityGroupIngress']

@pulumi.input_type
class DBSecurityGroupIngressInitArgs:
    def __init__(__self__, *,
                 d_b_security_group_name: pulumi.Input[str],
                 c_idrip: Optional[pulumi.Input[str]] = None,
                 e_c2_security_group_id: Optional[pulumi.Input[str]] = None,
                 e_c2_security_group_name: Optional[pulumi.Input[str]] = None,
                 e_c2_security_group_owner_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DBSecurityGroupIngress resource.
        """
        pulumi.set(__self__, "d_b_security_group_name", d_b_security_group_name)
        if c_idrip is not None:
            pulumi.set(__self__, "c_idrip", c_idrip)
        if e_c2_security_group_id is not None:
            pulumi.set(__self__, "e_c2_security_group_id", e_c2_security_group_id)
        if e_c2_security_group_name is not None:
            pulumi.set(__self__, "e_c2_security_group_name", e_c2_security_group_name)
        if e_c2_security_group_owner_id is not None:
            pulumi.set(__self__, "e_c2_security_group_owner_id", e_c2_security_group_owner_id)

    @property
    @pulumi.getter(name="dBSecurityGroupName")
    def d_b_security_group_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "d_b_security_group_name")

    @d_b_security_group_name.setter
    def d_b_security_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "d_b_security_group_name", value)

    @property
    @pulumi.getter(name="cIDRIP")
    def c_idrip(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "c_idrip")

    @c_idrip.setter
    def c_idrip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "c_idrip", value)

    @property
    @pulumi.getter(name="eC2SecurityGroupId")
    def e_c2_security_group_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "e_c2_security_group_id")

    @e_c2_security_group_id.setter
    def e_c2_security_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "e_c2_security_group_id", value)

    @property
    @pulumi.getter(name="eC2SecurityGroupName")
    def e_c2_security_group_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "e_c2_security_group_name")

    @e_c2_security_group_name.setter
    def e_c2_security_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "e_c2_security_group_name", value)

    @property
    @pulumi.getter(name="eC2SecurityGroupOwnerId")
    def e_c2_security_group_owner_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "e_c2_security_group_owner_id")

    @e_c2_security_group_owner_id.setter
    def e_c2_security_group_owner_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "e_c2_security_group_owner_id", value)


warnings.warn("""DBSecurityGroupIngress is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class DBSecurityGroupIngress(pulumi.CustomResource):
    warnings.warn("""DBSecurityGroupIngress is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 c_idrip: Optional[pulumi.Input[str]] = None,
                 d_b_security_group_name: Optional[pulumi.Input[str]] = None,
                 e_c2_security_group_id: Optional[pulumi.Input[str]] = None,
                 e_c2_security_group_name: Optional[pulumi.Input[str]] = None,
                 e_c2_security_group_owner_id: Optional[pulumi.Input[str]] = None,
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
                 args: DBSecurityGroupIngressInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::RDS::DBSecurityGroupIngress

        :param str resource_name: The name of the resource.
        :param DBSecurityGroupIngressInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DBSecurityGroupIngressInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 c_idrip: Optional[pulumi.Input[str]] = None,
                 d_b_security_group_name: Optional[pulumi.Input[str]] = None,
                 e_c2_security_group_id: Optional[pulumi.Input[str]] = None,
                 e_c2_security_group_name: Optional[pulumi.Input[str]] = None,
                 e_c2_security_group_owner_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""DBSecurityGroupIngress is deprecated: DBSecurityGroupIngress is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DBSecurityGroupIngressInitArgs.__new__(DBSecurityGroupIngressInitArgs)

            __props__.__dict__["c_idrip"] = c_idrip
            if d_b_security_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'd_b_security_group_name'")
            __props__.__dict__["d_b_security_group_name"] = d_b_security_group_name
            __props__.__dict__["e_c2_security_group_id"] = e_c2_security_group_id
            __props__.__dict__["e_c2_security_group_name"] = e_c2_security_group_name
            __props__.__dict__["e_c2_security_group_owner_id"] = e_c2_security_group_owner_id
        super(DBSecurityGroupIngress, __self__).__init__(
            'aws-native:rds:DBSecurityGroupIngress',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DBSecurityGroupIngress':
        """
        Get an existing DBSecurityGroupIngress resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DBSecurityGroupIngressInitArgs.__new__(DBSecurityGroupIngressInitArgs)

        __props__.__dict__["c_idrip"] = None
        __props__.__dict__["d_b_security_group_name"] = None
        __props__.__dict__["e_c2_security_group_id"] = None
        __props__.__dict__["e_c2_security_group_name"] = None
        __props__.__dict__["e_c2_security_group_owner_id"] = None
        return DBSecurityGroupIngress(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cIDRIP")
    def c_idrip(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "c_idrip")

    @property
    @pulumi.getter(name="dBSecurityGroupName")
    def d_b_security_group_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "d_b_security_group_name")

    @property
    @pulumi.getter(name="eC2SecurityGroupId")
    def e_c2_security_group_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "e_c2_security_group_id")

    @property
    @pulumi.getter(name="eC2SecurityGroupName")
    def e_c2_security_group_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "e_c2_security_group_name")

    @property
    @pulumi.getter(name="eC2SecurityGroupOwnerId")
    def e_c2_security_group_owner_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "e_c2_security_group_owner_id")

