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
    'BillingGroupAccountGrouping',
    'BillingGroupComputationPreference',
    'BillingGroupTag',
    'CustomLineItemBillingPeriodRange',
    'CustomLineItemChargeDetails',
    'CustomLineItemFlatChargeDetails',
    'CustomLineItemLineItemFilter',
    'CustomLineItemPercentageChargeDetails',
    'CustomLineItemTag',
    'PricingPlanTag',
    'PricingRuleFreeTier',
    'PricingRuleTag',
    'TieringProperties',
]

@pulumi.output_type
class BillingGroupAccountGrouping(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "linkedAccountIds":
            suggest = "linked_account_ids"
        elif key == "autoAssociate":
            suggest = "auto_associate"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BillingGroupAccountGrouping. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BillingGroupAccountGrouping.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BillingGroupAccountGrouping.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 linked_account_ids: Sequence[str],
                 auto_associate: Optional[bool] = None):
        BillingGroupAccountGrouping._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            linked_account_ids=linked_account_ids,
            auto_associate=auto_associate,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             linked_account_ids: Sequence[str],
             auto_associate: Optional[bool] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("linked_account_ids", linked_account_ids)
        if auto_associate is not None:
            _setter("auto_associate", auto_associate)

    @property
    @pulumi.getter(name="linkedAccountIds")
    def linked_account_ids(self) -> Sequence[str]:
        return pulumi.get(self, "linked_account_ids")

    @property
    @pulumi.getter(name="autoAssociate")
    def auto_associate(self) -> Optional[bool]:
        return pulumi.get(self, "auto_associate")


@pulumi.output_type
class BillingGroupComputationPreference(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "pricingPlanArn":
            suggest = "pricing_plan_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BillingGroupComputationPreference. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BillingGroupComputationPreference.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BillingGroupComputationPreference.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 pricing_plan_arn: str):
        """
        :param str pricing_plan_arn: ARN of the attached pricing plan
        """
        BillingGroupComputationPreference._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            pricing_plan_arn=pricing_plan_arn,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             pricing_plan_arn: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("pricing_plan_arn", pricing_plan_arn)

    @property
    @pulumi.getter(name="pricingPlanArn")
    def pricing_plan_arn(self) -> str:
        """
        ARN of the attached pricing plan
        """
        return pulumi.get(self, "pricing_plan_arn")


@pulumi.output_type
class BillingGroupTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        BillingGroupTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class CustomLineItemBillingPeriodRange(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "exclusiveEndBillingPeriod":
            suggest = "exclusive_end_billing_period"
        elif key == "inclusiveStartBillingPeriod":
            suggest = "inclusive_start_billing_period"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CustomLineItemBillingPeriodRange. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CustomLineItemBillingPeriodRange.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CustomLineItemBillingPeriodRange.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 exclusive_end_billing_period: Optional[str] = None,
                 inclusive_start_billing_period: Optional[str] = None):
        CustomLineItemBillingPeriodRange._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            exclusive_end_billing_period=exclusive_end_billing_period,
            inclusive_start_billing_period=inclusive_start_billing_period,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             exclusive_end_billing_period: Optional[str] = None,
             inclusive_start_billing_period: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if exclusive_end_billing_period is not None:
            _setter("exclusive_end_billing_period", exclusive_end_billing_period)
        if inclusive_start_billing_period is not None:
            _setter("inclusive_start_billing_period", inclusive_start_billing_period)

    @property
    @pulumi.getter(name="exclusiveEndBillingPeriod")
    def exclusive_end_billing_period(self) -> Optional[str]:
        return pulumi.get(self, "exclusive_end_billing_period")

    @property
    @pulumi.getter(name="inclusiveStartBillingPeriod")
    def inclusive_start_billing_period(self) -> Optional[str]:
        return pulumi.get(self, "inclusive_start_billing_period")


@pulumi.output_type
class CustomLineItemChargeDetails(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "lineItemFilters":
            suggest = "line_item_filters"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CustomLineItemChargeDetails. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CustomLineItemChargeDetails.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CustomLineItemChargeDetails.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: 'CustomLineItemType',
                 flat: Optional['outputs.CustomLineItemFlatChargeDetails'] = None,
                 line_item_filters: Optional[Sequence['outputs.CustomLineItemLineItemFilter']] = None,
                 percentage: Optional['outputs.CustomLineItemPercentageChargeDetails'] = None):
        CustomLineItemChargeDetails._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            type=type,
            flat=flat,
            line_item_filters=line_item_filters,
            percentage=percentage,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             type: 'CustomLineItemType',
             flat: Optional['outputs.CustomLineItemFlatChargeDetails'] = None,
             line_item_filters: Optional[Sequence['outputs.CustomLineItemLineItemFilter']] = None,
             percentage: Optional['outputs.CustomLineItemPercentageChargeDetails'] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("type", type)
        if flat is not None:
            _setter("flat", flat)
        if line_item_filters is not None:
            _setter("line_item_filters", line_item_filters)
        if percentage is not None:
            _setter("percentage", percentage)

    @property
    @pulumi.getter
    def type(self) -> 'CustomLineItemType':
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def flat(self) -> Optional['outputs.CustomLineItemFlatChargeDetails']:
        return pulumi.get(self, "flat")

    @property
    @pulumi.getter(name="lineItemFilters")
    def line_item_filters(self) -> Optional[Sequence['outputs.CustomLineItemLineItemFilter']]:
        return pulumi.get(self, "line_item_filters")

    @property
    @pulumi.getter
    def percentage(self) -> Optional['outputs.CustomLineItemPercentageChargeDetails']:
        return pulumi.get(self, "percentage")


@pulumi.output_type
class CustomLineItemFlatChargeDetails(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "chargeValue":
            suggest = "charge_value"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CustomLineItemFlatChargeDetails. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CustomLineItemFlatChargeDetails.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CustomLineItemFlatChargeDetails.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 charge_value: float):
        CustomLineItemFlatChargeDetails._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            charge_value=charge_value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             charge_value: float,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("charge_value", charge_value)

    @property
    @pulumi.getter(name="chargeValue")
    def charge_value(self) -> float:
        return pulumi.get(self, "charge_value")


@pulumi.output_type
class CustomLineItemLineItemFilter(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "matchOption":
            suggest = "match_option"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CustomLineItemLineItemFilter. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CustomLineItemLineItemFilter.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CustomLineItemLineItemFilter.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 attribute: 'CustomLineItemLineItemFilterAttribute',
                 match_option: 'CustomLineItemLineItemFilterMatchOption',
                 values: Sequence['CustomLineItemLineItemFilterValue']):
        CustomLineItemLineItemFilter._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            attribute=attribute,
            match_option=match_option,
            values=values,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             attribute: 'CustomLineItemLineItemFilterAttribute',
             match_option: 'CustomLineItemLineItemFilterMatchOption',
             values: Sequence['CustomLineItemLineItemFilterValue'],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("attribute", attribute)
        _setter("match_option", match_option)
        _setter("values", values)

    @property
    @pulumi.getter
    def attribute(self) -> 'CustomLineItemLineItemFilterAttribute':
        return pulumi.get(self, "attribute")

    @property
    @pulumi.getter(name="matchOption")
    def match_option(self) -> 'CustomLineItemLineItemFilterMatchOption':
        return pulumi.get(self, "match_option")

    @property
    @pulumi.getter
    def values(self) -> Sequence['CustomLineItemLineItemFilterValue']:
        return pulumi.get(self, "values")


@pulumi.output_type
class CustomLineItemPercentageChargeDetails(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "percentageValue":
            suggest = "percentage_value"
        elif key == "childAssociatedResources":
            suggest = "child_associated_resources"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CustomLineItemPercentageChargeDetails. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CustomLineItemPercentageChargeDetails.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CustomLineItemPercentageChargeDetails.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 percentage_value: float,
                 child_associated_resources: Optional[Sequence[str]] = None):
        CustomLineItemPercentageChargeDetails._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            percentage_value=percentage_value,
            child_associated_resources=child_associated_resources,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             percentage_value: float,
             child_associated_resources: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("percentage_value", percentage_value)
        if child_associated_resources is not None:
            _setter("child_associated_resources", child_associated_resources)

    @property
    @pulumi.getter(name="percentageValue")
    def percentage_value(self) -> float:
        return pulumi.get(self, "percentage_value")

    @property
    @pulumi.getter(name="childAssociatedResources")
    def child_associated_resources(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "child_associated_resources")


@pulumi.output_type
class CustomLineItemTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        CustomLineItemTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class PricingPlanTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        PricingPlanTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class PricingRuleFreeTier(dict):
    """
    The possible customizable free tier configurations.
    """
    def __init__(__self__, *,
                 activated: bool):
        """
        The possible customizable free tier configurations.
        """
        PricingRuleFreeTier._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            activated=activated,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             activated: bool,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("activated", activated)

    @property
    @pulumi.getter
    def activated(self) -> bool:
        return pulumi.get(self, "activated")


@pulumi.output_type
class PricingRuleTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        PricingRuleTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class TieringProperties(dict):
    """
    The set of tiering configurations for the pricing rule.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "freeTier":
            suggest = "free_tier"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TieringProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TieringProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TieringProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 free_tier: Optional['outputs.PricingRuleFreeTier'] = None):
        """
        The set of tiering configurations for the pricing rule.
        """
        TieringProperties._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            free_tier=free_tier,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             free_tier: Optional['outputs.PricingRuleFreeTier'] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if free_tier is not None:
            _setter("free_tier", free_tier)

    @property
    @pulumi.getter(name="freeTier")
    def free_tier(self) -> Optional['outputs.PricingRuleFreeTier']:
        return pulumi.get(self, "free_tier")


