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
from ._inputs import *

__all__ = ['CustomLineItemArgs', 'CustomLineItem']

@pulumi.input_type
class CustomLineItemArgs:
    def __init__(__self__, *,
                 billing_group_arn: pulumi.Input[str],
                 billing_period_range: Optional[pulumi.Input['CustomLineItemBillingPeriodRangeArgs']] = None,
                 custom_line_item_charge_details: Optional[pulumi.Input['CustomLineItemChargeDetailsArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['CustomLineItemTagArgs']]]] = None):
        """
        The set of arguments for constructing a CustomLineItem resource.
        :param pulumi.Input[str] billing_group_arn: Billing Group ARN
        """
        pulumi.set(__self__, "billing_group_arn", billing_group_arn)
        if billing_period_range is not None:
            pulumi.set(__self__, "billing_period_range", billing_period_range)
        if custom_line_item_charge_details is not None:
            pulumi.set(__self__, "custom_line_item_charge_details", custom_line_item_charge_details)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="billingGroupArn")
    def billing_group_arn(self) -> pulumi.Input[str]:
        """
        Billing Group ARN
        """
        return pulumi.get(self, "billing_group_arn")

    @billing_group_arn.setter
    def billing_group_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "billing_group_arn", value)

    @property
    @pulumi.getter(name="billingPeriodRange")
    def billing_period_range(self) -> Optional[pulumi.Input['CustomLineItemBillingPeriodRangeArgs']]:
        return pulumi.get(self, "billing_period_range")

    @billing_period_range.setter
    def billing_period_range(self, value: Optional[pulumi.Input['CustomLineItemBillingPeriodRangeArgs']]):
        pulumi.set(self, "billing_period_range", value)

    @property
    @pulumi.getter(name="customLineItemChargeDetails")
    def custom_line_item_charge_details(self) -> Optional[pulumi.Input['CustomLineItemChargeDetailsArgs']]:
        return pulumi.get(self, "custom_line_item_charge_details")

    @custom_line_item_charge_details.setter
    def custom_line_item_charge_details(self, value: Optional[pulumi.Input['CustomLineItemChargeDetailsArgs']]):
        pulumi.set(self, "custom_line_item_charge_details", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CustomLineItemTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CustomLineItemTagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""CustomLineItem is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class CustomLineItem(pulumi.CustomResource):
    warnings.warn("""CustomLineItem is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_group_arn: Optional[pulumi.Input[str]] = None,
                 billing_period_range: Optional[pulumi.Input[pulumi.InputType['CustomLineItemBillingPeriodRangeArgs']]] = None,
                 custom_line_item_charge_details: Optional[pulumi.Input[pulumi.InputType['CustomLineItemChargeDetailsArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomLineItemTagArgs']]]]] = None,
                 __props__=None):
        """
        A custom line item is an one time charge that is applied to a specific billing group's bill.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] billing_group_arn: Billing Group ARN
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomLineItemArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A custom line item is an one time charge that is applied to a specific billing group's bill.

        :param str resource_name: The name of the resource.
        :param CustomLineItemArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomLineItemArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_group_arn: Optional[pulumi.Input[str]] = None,
                 billing_period_range: Optional[pulumi.Input[pulumi.InputType['CustomLineItemBillingPeriodRangeArgs']]] = None,
                 custom_line_item_charge_details: Optional[pulumi.Input[pulumi.InputType['CustomLineItemChargeDetailsArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomLineItemTagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""CustomLineItem is deprecated: CustomLineItem is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomLineItemArgs.__new__(CustomLineItemArgs)

            if billing_group_arn is None and not opts.urn:
                raise TypeError("Missing required property 'billing_group_arn'")
            __props__.__dict__["billing_group_arn"] = billing_group_arn
            __props__.__dict__["billing_period_range"] = billing_period_range
            __props__.__dict__["custom_line_item_charge_details"] = custom_line_item_charge_details
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["association_size"] = None
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["currency_code"] = None
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["product_code"] = None
        super(CustomLineItem, __self__).__init__(
            'aws-native:billingconductor:CustomLineItem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CustomLineItem':
        """
        Get an existing CustomLineItem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CustomLineItemArgs.__new__(CustomLineItemArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["association_size"] = None
        __props__.__dict__["billing_group_arn"] = None
        __props__.__dict__["billing_period_range"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["currency_code"] = None
        __props__.__dict__["custom_line_item_charge_details"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["product_code"] = None
        __props__.__dict__["tags"] = None
        return CustomLineItem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="associationSize")
    def association_size(self) -> pulumi.Output[int]:
        """
        Number of source values associated to this custom line item
        """
        return pulumi.get(self, "association_size")

    @property
    @pulumi.getter(name="billingGroupArn")
    def billing_group_arn(self) -> pulumi.Output[str]:
        """
        Billing Group ARN
        """
        return pulumi.get(self, "billing_group_arn")

    @property
    @pulumi.getter(name="billingPeriodRange")
    def billing_period_range(self) -> pulumi.Output[Optional['outputs.CustomLineItemBillingPeriodRange']]:
        return pulumi.get(self, "billing_period_range")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[int]:
        """
        Creation timestamp in UNIX epoch time format
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> pulumi.Output['CustomLineItemCurrencyCode']:
        return pulumi.get(self, "currency_code")

    @property
    @pulumi.getter(name="customLineItemChargeDetails")
    def custom_line_item_charge_details(self) -> pulumi.Output[Optional['outputs.CustomLineItemChargeDetails']]:
        return pulumi.get(self, "custom_line_item_charge_details")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[int]:
        """
        Latest modified timestamp in UNIX epoch time format
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="productCode")
    def product_code(self) -> pulumi.Output[str]:
        return pulumi.get(self, "product_code")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.CustomLineItemTag']]]:
        return pulumi.get(self, "tags")

