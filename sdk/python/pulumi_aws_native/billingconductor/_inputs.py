# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'BillingGroupAccountGroupingArgs',
    'BillingGroupComputationPreferenceArgs',
    'CustomLineItemBillingPeriodRangeArgs',
    'CustomLineItemChargeDetailsArgs',
    'CustomLineItemFlatChargeDetailsArgs',
    'CustomLineItemLineItemFilterArgs',
    'CustomLineItemPercentageChargeDetailsArgs',
    'PricingRuleFreeTierArgs',
    'TieringPropertiesArgs',
]

@pulumi.input_type
class BillingGroupAccountGroupingArgs:
    def __init__(__self__, *,
                 linked_account_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 auto_associate: Optional[pulumi.Input[bool]] = None):
        pulumi.set(__self__, "linked_account_ids", linked_account_ids)
        if auto_associate is not None:
            pulumi.set(__self__, "auto_associate", auto_associate)

    @property
    @pulumi.getter(name="linkedAccountIds")
    def linked_account_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "linked_account_ids")

    @linked_account_ids.setter
    def linked_account_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "linked_account_ids", value)

    @property
    @pulumi.getter(name="autoAssociate")
    def auto_associate(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "auto_associate")

    @auto_associate.setter
    def auto_associate(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_associate", value)


@pulumi.input_type
class BillingGroupComputationPreferenceArgs:
    def __init__(__self__, *,
                 pricing_plan_arn: pulumi.Input[str]):
        """
        :param pulumi.Input[str] pricing_plan_arn: ARN of the attached pricing plan
        """
        pulumi.set(__self__, "pricing_plan_arn", pricing_plan_arn)

    @property
    @pulumi.getter(name="pricingPlanArn")
    def pricing_plan_arn(self) -> pulumi.Input[str]:
        """
        ARN of the attached pricing plan
        """
        return pulumi.get(self, "pricing_plan_arn")

    @pricing_plan_arn.setter
    def pricing_plan_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "pricing_plan_arn", value)


@pulumi.input_type
class CustomLineItemBillingPeriodRangeArgs:
    def __init__(__self__, *,
                 exclusive_end_billing_period: Optional[pulumi.Input[str]] = None,
                 inclusive_start_billing_period: Optional[pulumi.Input[str]] = None):
        if exclusive_end_billing_period is not None:
            pulumi.set(__self__, "exclusive_end_billing_period", exclusive_end_billing_period)
        if inclusive_start_billing_period is not None:
            pulumi.set(__self__, "inclusive_start_billing_period", inclusive_start_billing_period)

    @property
    @pulumi.getter(name="exclusiveEndBillingPeriod")
    def exclusive_end_billing_period(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "exclusive_end_billing_period")

    @exclusive_end_billing_period.setter
    def exclusive_end_billing_period(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "exclusive_end_billing_period", value)

    @property
    @pulumi.getter(name="inclusiveStartBillingPeriod")
    def inclusive_start_billing_period(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "inclusive_start_billing_period")

    @inclusive_start_billing_period.setter
    def inclusive_start_billing_period(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "inclusive_start_billing_period", value)


@pulumi.input_type
class CustomLineItemChargeDetailsArgs:
    def __init__(__self__, *,
                 type: pulumi.Input['CustomLineItemType'],
                 flat: Optional[pulumi.Input['CustomLineItemFlatChargeDetailsArgs']] = None,
                 line_item_filters: Optional[pulumi.Input[Sequence[pulumi.Input['CustomLineItemLineItemFilterArgs']]]] = None,
                 percentage: Optional[pulumi.Input['CustomLineItemPercentageChargeDetailsArgs']] = None):
        pulumi.set(__self__, "type", type)
        if flat is not None:
            pulumi.set(__self__, "flat", flat)
        if line_item_filters is not None:
            pulumi.set(__self__, "line_item_filters", line_item_filters)
        if percentage is not None:
            pulumi.set(__self__, "percentage", percentage)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['CustomLineItemType']:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['CustomLineItemType']):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def flat(self) -> Optional[pulumi.Input['CustomLineItemFlatChargeDetailsArgs']]:
        return pulumi.get(self, "flat")

    @flat.setter
    def flat(self, value: Optional[pulumi.Input['CustomLineItemFlatChargeDetailsArgs']]):
        pulumi.set(self, "flat", value)

    @property
    @pulumi.getter(name="lineItemFilters")
    def line_item_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CustomLineItemLineItemFilterArgs']]]]:
        return pulumi.get(self, "line_item_filters")

    @line_item_filters.setter
    def line_item_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CustomLineItemLineItemFilterArgs']]]]):
        pulumi.set(self, "line_item_filters", value)

    @property
    @pulumi.getter
    def percentage(self) -> Optional[pulumi.Input['CustomLineItemPercentageChargeDetailsArgs']]:
        return pulumi.get(self, "percentage")

    @percentage.setter
    def percentage(self, value: Optional[pulumi.Input['CustomLineItemPercentageChargeDetailsArgs']]):
        pulumi.set(self, "percentage", value)


@pulumi.input_type
class CustomLineItemFlatChargeDetailsArgs:
    def __init__(__self__, *,
                 charge_value: pulumi.Input[float]):
        pulumi.set(__self__, "charge_value", charge_value)

    @property
    @pulumi.getter(name="chargeValue")
    def charge_value(self) -> pulumi.Input[float]:
        return pulumi.get(self, "charge_value")

    @charge_value.setter
    def charge_value(self, value: pulumi.Input[float]):
        pulumi.set(self, "charge_value", value)


@pulumi.input_type
class CustomLineItemLineItemFilterArgs:
    def __init__(__self__, *,
                 attribute: pulumi.Input['CustomLineItemLineItemFilterAttribute'],
                 match_option: pulumi.Input['CustomLineItemLineItemFilterMatchOption'],
                 values: pulumi.Input[Sequence[pulumi.Input['CustomLineItemLineItemFilterValue']]]):
        pulumi.set(__self__, "attribute", attribute)
        pulumi.set(__self__, "match_option", match_option)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def attribute(self) -> pulumi.Input['CustomLineItemLineItemFilterAttribute']:
        return pulumi.get(self, "attribute")

    @attribute.setter
    def attribute(self, value: pulumi.Input['CustomLineItemLineItemFilterAttribute']):
        pulumi.set(self, "attribute", value)

    @property
    @pulumi.getter(name="matchOption")
    def match_option(self) -> pulumi.Input['CustomLineItemLineItemFilterMatchOption']:
        return pulumi.get(self, "match_option")

    @match_option.setter
    def match_option(self, value: pulumi.Input['CustomLineItemLineItemFilterMatchOption']):
        pulumi.set(self, "match_option", value)

    @property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input['CustomLineItemLineItemFilterValue']]]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input['CustomLineItemLineItemFilterValue']]]):
        pulumi.set(self, "values", value)


@pulumi.input_type
class CustomLineItemPercentageChargeDetailsArgs:
    def __init__(__self__, *,
                 percentage_value: pulumi.Input[float],
                 child_associated_resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        pulumi.set(__self__, "percentage_value", percentage_value)
        if child_associated_resources is not None:
            pulumi.set(__self__, "child_associated_resources", child_associated_resources)

    @property
    @pulumi.getter(name="percentageValue")
    def percentage_value(self) -> pulumi.Input[float]:
        return pulumi.get(self, "percentage_value")

    @percentage_value.setter
    def percentage_value(self, value: pulumi.Input[float]):
        pulumi.set(self, "percentage_value", value)

    @property
    @pulumi.getter(name="childAssociatedResources")
    def child_associated_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "child_associated_resources")

    @child_associated_resources.setter
    def child_associated_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "child_associated_resources", value)


@pulumi.input_type
class PricingRuleFreeTierArgs:
    def __init__(__self__, *,
                 activated: pulumi.Input[bool]):
        """
        The possible customizable free tier configurations.
        """
        pulumi.set(__self__, "activated", activated)

    @property
    @pulumi.getter
    def activated(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "activated")

    @activated.setter
    def activated(self, value: pulumi.Input[bool]):
        pulumi.set(self, "activated", value)


@pulumi.input_type
class TieringPropertiesArgs:
    def __init__(__self__, *,
                 free_tier: Optional[pulumi.Input['PricingRuleFreeTierArgs']] = None):
        """
        The set of tiering configurations for the pricing rule.
        """
        if free_tier is not None:
            pulumi.set(__self__, "free_tier", free_tier)

    @property
    @pulumi.getter(name="freeTier")
    def free_tier(self) -> Optional[pulumi.Input['PricingRuleFreeTierArgs']]:
        return pulumi.get(self, "free_tier")

    @free_tier.setter
    def free_tier(self, value: Optional[pulumi.Input['PricingRuleFreeTierArgs']]):
        pulumi.set(self, "free_tier", value)


