# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['ControlPanelArgs', 'ControlPanel']

@pulumi.input_type
class ControlPanelArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 cluster_arn: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ControlPanel resource.
        :param pulumi.Input[str] name: The name of the control panel. You can use any non-white space character in the name.
        :param pulumi.Input[str] cluster_arn: Cluster to associate with the Control Panel
        """
        pulumi.set(__self__, "name", name)
        if cluster_arn is not None:
            pulumi.set(__self__, "cluster_arn", cluster_arn)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the control panel. You can use any non-white space character in the name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Cluster to associate with the Control Panel
        """
        return pulumi.get(self, "cluster_arn")

    @cluster_arn.setter
    def cluster_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_arn", value)


class ControlPanel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        AWS Route53 Recovery Control Control Panel resource schema .

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_arn: Cluster to associate with the Control Panel
        :param pulumi.Input[str] name: The name of the control panel. You can use any non-white space character in the name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ControlPanelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        AWS Route53 Recovery Control Control Panel resource schema .

        :param str resource_name: The name of the resource.
        :param ControlPanelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ControlPanelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ControlPanelArgs.__new__(ControlPanelArgs)

            __props__.__dict__["cluster_arn"] = cluster_arn
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["control_panel_arn"] = None
            __props__.__dict__["default_control_panel"] = None
            __props__.__dict__["routing_control_count"] = None
            __props__.__dict__["status"] = None
        super(ControlPanel, __self__).__init__(
            'aws-native:route53recoverycontrol:ControlPanel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ControlPanel':
        """
        Get an existing ControlPanel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ControlPanelArgs.__new__(ControlPanelArgs)

        __props__.__dict__["cluster_arn"] = None
        __props__.__dict__["control_panel_arn"] = None
        __props__.__dict__["default_control_panel"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["routing_control_count"] = None
        __props__.__dict__["status"] = None
        return ControlPanel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> pulumi.Output[Optional[str]]:
        """
        Cluster to associate with the Control Panel
        """
        return pulumi.get(self, "cluster_arn")

    @property
    @pulumi.getter(name="controlPanelArn")
    def control_panel_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the cluster.
        """
        return pulumi.get(self, "control_panel_arn")

    @property
    @pulumi.getter(name="defaultControlPanel")
    def default_control_panel(self) -> pulumi.Output[bool]:
        """
        A flag that Amazon Route 53 Application Recovery Controller sets to true to designate the default control panel for a cluster. When you create a cluster, Amazon Route 53 Application Recovery Controller creates a control panel, and sets this flag for that control panel. If you create a control panel yourself, this flag is set to false.
        """
        return pulumi.get(self, "default_control_panel")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the control panel. You can use any non-white space character in the name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="routingControlCount")
    def routing_control_count(self) -> pulumi.Output[int]:
        """
        Count of associated routing controls
        """
        return pulumi.get(self, "routing_control_count")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['ControlPanelStatus']:
        """
        The deployment status of control panel. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.
        """
        return pulumi.get(self, "status")

