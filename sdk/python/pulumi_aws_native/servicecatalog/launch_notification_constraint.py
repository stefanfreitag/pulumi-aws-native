# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['LaunchNotificationConstraintArgs', 'LaunchNotificationConstraint']

@pulumi.input_type
class LaunchNotificationConstraintArgs:
    def __init__(__self__, *,
                 notification_arns: pulumi.Input[Sequence[pulumi.Input[str]]],
                 portfolio_id: pulumi.Input[str],
                 product_id: pulumi.Input[str],
                 accept_language: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LaunchNotificationConstraint resource.
        """
        pulumi.set(__self__, "notification_arns", notification_arns)
        pulumi.set(__self__, "portfolio_id", portfolio_id)
        pulumi.set(__self__, "product_id", product_id)
        if accept_language is not None:
            pulumi.set(__self__, "accept_language", accept_language)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="notificationArns")
    def notification_arns(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "notification_arns")

    @notification_arns.setter
    def notification_arns(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "notification_arns", value)

    @property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "portfolio_id")

    @portfolio_id.setter
    def portfolio_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "portfolio_id", value)

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "product_id")

    @product_id.setter
    def product_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "product_id", value)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "accept_language")

    @accept_language.setter
    def accept_language(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accept_language", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


warnings.warn("""LaunchNotificationConstraint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class LaunchNotificationConstraint(pulumi.CustomResource):
    warnings.warn("""LaunchNotificationConstraint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accept_language: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 notification_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 portfolio_id: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ServiceCatalog::LaunchNotificationConstraint

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LaunchNotificationConstraintArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ServiceCatalog::LaunchNotificationConstraint

        :param str resource_name: The name of the resource.
        :param LaunchNotificationConstraintArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LaunchNotificationConstraintArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accept_language: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 notification_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 portfolio_id: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""LaunchNotificationConstraint is deprecated: LaunchNotificationConstraint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LaunchNotificationConstraintArgs.__new__(LaunchNotificationConstraintArgs)

            __props__.__dict__["accept_language"] = accept_language
            __props__.__dict__["description"] = description
            if notification_arns is None and not opts.urn:
                raise TypeError("Missing required property 'notification_arns'")
            __props__.__dict__["notification_arns"] = notification_arns
            if portfolio_id is None and not opts.urn:
                raise TypeError("Missing required property 'portfolio_id'")
            __props__.__dict__["portfolio_id"] = portfolio_id
            if product_id is None and not opts.urn:
                raise TypeError("Missing required property 'product_id'")
            __props__.__dict__["product_id"] = product_id
        super(LaunchNotificationConstraint, __self__).__init__(
            'aws-native:servicecatalog:LaunchNotificationConstraint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LaunchNotificationConstraint':
        """
        Get an existing LaunchNotificationConstraint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LaunchNotificationConstraintArgs.__new__(LaunchNotificationConstraintArgs)

        __props__.__dict__["accept_language"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["notification_arns"] = None
        __props__.__dict__["portfolio_id"] = None
        __props__.__dict__["product_id"] = None
        return LaunchNotificationConstraint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "accept_language")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="notificationArns")
    def notification_arns(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "notification_arns")

    @property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "portfolio_id")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "product_id")

