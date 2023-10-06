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
from ._inputs import *

__all__ = ['NetworkAclEntryArgs', 'NetworkAclEntry']

@pulumi.input_type
class NetworkAclEntryArgs:
    def __init__(__self__, *,
                 network_acl_id: pulumi.Input[str],
                 protocol: pulumi.Input[int],
                 rule_action: pulumi.Input[str],
                 rule_number: pulumi.Input[int],
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 egress: Optional[pulumi.Input[bool]] = None,
                 icmp: Optional[pulumi.Input['NetworkAclEntryIcmpArgs']] = None,
                 ipv6_cidr_block: Optional[pulumi.Input[str]] = None,
                 port_range: Optional[pulumi.Input['NetworkAclEntryPortRangeArgs']] = None):
        """
        The set of arguments for constructing a NetworkAclEntry resource.
        """
        NetworkAclEntryArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            network_acl_id=network_acl_id,
            protocol=protocol,
            rule_action=rule_action,
            rule_number=rule_number,
            cidr_block=cidr_block,
            egress=egress,
            icmp=icmp,
            ipv6_cidr_block=ipv6_cidr_block,
            port_range=port_range,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             network_acl_id: pulumi.Input[str],
             protocol: pulumi.Input[int],
             rule_action: pulumi.Input[str],
             rule_number: pulumi.Input[int],
             cidr_block: Optional[pulumi.Input[str]] = None,
             egress: Optional[pulumi.Input[bool]] = None,
             icmp: Optional[pulumi.Input['NetworkAclEntryIcmpArgs']] = None,
             ipv6_cidr_block: Optional[pulumi.Input[str]] = None,
             port_range: Optional[pulumi.Input['NetworkAclEntryPortRangeArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("network_acl_id", network_acl_id)
        _setter("protocol", protocol)
        _setter("rule_action", rule_action)
        _setter("rule_number", rule_number)
        if cidr_block is not None:
            _setter("cidr_block", cidr_block)
        if egress is not None:
            _setter("egress", egress)
        if icmp is not None:
            _setter("icmp", icmp)
        if ipv6_cidr_block is not None:
            _setter("ipv6_cidr_block", ipv6_cidr_block)
        if port_range is not None:
            _setter("port_range", port_range)

    @property
    @pulumi.getter(name="networkAclId")
    def network_acl_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "network_acl_id")

    @network_acl_id.setter
    def network_acl_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_acl_id", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[int]:
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[int]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> pulumi.Input[str]:
        return pulumi.get(self, "rule_action")

    @rule_action.setter
    def rule_action(self, value: pulumi.Input[str]):
        pulumi.set(self, "rule_action", value)

    @property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> pulumi.Input[int]:
        return pulumi.get(self, "rule_number")

    @rule_number.setter
    def rule_number(self, value: pulumi.Input[int]):
        pulumi.set(self, "rule_number", value)

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cidr_block")

    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr_block", value)

    @property
    @pulumi.getter
    def egress(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "egress")

    @egress.setter
    def egress(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "egress", value)

    @property
    @pulumi.getter
    def icmp(self) -> Optional[pulumi.Input['NetworkAclEntryIcmpArgs']]:
        return pulumi.get(self, "icmp")

    @icmp.setter
    def icmp(self, value: Optional[pulumi.Input['NetworkAclEntryIcmpArgs']]):
        pulumi.set(self, "icmp", value)

    @property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ipv6_cidr_block")

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_cidr_block", value)

    @property
    @pulumi.getter(name="portRange")
    def port_range(self) -> Optional[pulumi.Input['NetworkAclEntryPortRangeArgs']]:
        return pulumi.get(self, "port_range")

    @port_range.setter
    def port_range(self, value: Optional[pulumi.Input['NetworkAclEntryPortRangeArgs']]):
        pulumi.set(self, "port_range", value)


warnings.warn("""NetworkAclEntry is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class NetworkAclEntry(pulumi.CustomResource):
    warnings.warn("""NetworkAclEntry is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 egress: Optional[pulumi.Input[bool]] = None,
                 icmp: Optional[pulumi.Input[pulumi.InputType['NetworkAclEntryIcmpArgs']]] = None,
                 ipv6_cidr_block: Optional[pulumi.Input[str]] = None,
                 network_acl_id: Optional[pulumi.Input[str]] = None,
                 port_range: Optional[pulumi.Input[pulumi.InputType['NetworkAclEntryPortRangeArgs']]] = None,
                 protocol: Optional[pulumi.Input[int]] = None,
                 rule_action: Optional[pulumi.Input[str]] = None,
                 rule_number: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::NetworkAclEntry

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkAclEntryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::NetworkAclEntry

        :param str resource_name: The name of the resource.
        :param NetworkAclEntryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkAclEntryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            NetworkAclEntryArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 egress: Optional[pulumi.Input[bool]] = None,
                 icmp: Optional[pulumi.Input[pulumi.InputType['NetworkAclEntryIcmpArgs']]] = None,
                 ipv6_cidr_block: Optional[pulumi.Input[str]] = None,
                 network_acl_id: Optional[pulumi.Input[str]] = None,
                 port_range: Optional[pulumi.Input[pulumi.InputType['NetworkAclEntryPortRangeArgs']]] = None,
                 protocol: Optional[pulumi.Input[int]] = None,
                 rule_action: Optional[pulumi.Input[str]] = None,
                 rule_number: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        pulumi.log.warn("""NetworkAclEntry is deprecated: NetworkAclEntry is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkAclEntryArgs.__new__(NetworkAclEntryArgs)

            __props__.__dict__["cidr_block"] = cidr_block
            __props__.__dict__["egress"] = egress
            if icmp is not None and not isinstance(icmp, NetworkAclEntryIcmpArgs):
                icmp = icmp or {}
                def _setter(key, value):
                    icmp[key] = value
                NetworkAclEntryIcmpArgs._configure(_setter, **icmp)
            __props__.__dict__["icmp"] = icmp
            __props__.__dict__["ipv6_cidr_block"] = ipv6_cidr_block
            if network_acl_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_acl_id'")
            __props__.__dict__["network_acl_id"] = network_acl_id
            if port_range is not None and not isinstance(port_range, NetworkAclEntryPortRangeArgs):
                port_range = port_range or {}
                def _setter(key, value):
                    port_range[key] = value
                NetworkAclEntryPortRangeArgs._configure(_setter, **port_range)
            __props__.__dict__["port_range"] = port_range
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
            if rule_action is None and not opts.urn:
                raise TypeError("Missing required property 'rule_action'")
            __props__.__dict__["rule_action"] = rule_action
            if rule_number is None and not opts.urn:
                raise TypeError("Missing required property 'rule_number'")
            __props__.__dict__["rule_number"] = rule_number
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["egress", "network_acl_id", "rule_number"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(NetworkAclEntry, __self__).__init__(
            'aws-native:ec2:NetworkAclEntry',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkAclEntry':
        """
        Get an existing NetworkAclEntry resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkAclEntryArgs.__new__(NetworkAclEntryArgs)

        __props__.__dict__["cidr_block"] = None
        __props__.__dict__["egress"] = None
        __props__.__dict__["icmp"] = None
        __props__.__dict__["ipv6_cidr_block"] = None
        __props__.__dict__["network_acl_id"] = None
        __props__.__dict__["port_range"] = None
        __props__.__dict__["protocol"] = None
        __props__.__dict__["rule_action"] = None
        __props__.__dict__["rule_number"] = None
        return NetworkAclEntry(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "cidr_block")

    @property
    @pulumi.getter
    def egress(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "egress")

    @property
    @pulumi.getter
    def icmp(self) -> pulumi.Output[Optional['outputs.NetworkAclEntryIcmp']]:
        return pulumi.get(self, "icmp")

    @property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ipv6_cidr_block")

    @property
    @pulumi.getter(name="networkAclId")
    def network_acl_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "network_acl_id")

    @property
    @pulumi.getter(name="portRange")
    def port_range(self) -> pulumi.Output[Optional['outputs.NetworkAclEntryPortRange']]:
        return pulumi.get(self, "port_range")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[int]:
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> pulumi.Output[str]:
        return pulumi.get(self, "rule_action")

    @property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> pulumi.Output[int]:
        return pulumi.get(self, "rule_number")

