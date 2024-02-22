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
    'GetRulesetResult',
    'AwaitableGetRulesetResult',
    'get_ruleset',
    'get_ruleset_output',
]

@pulumi.output_type
class GetRulesetResult:
    def __init__(__self__, description=None, rules=None, tags=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the Ruleset
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def rules(self) -> Optional[Sequence['outputs.RulesetRule']]:
        """
        List of the data quality rules in the ruleset
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        return pulumi.get(self, "tags")


class AwaitableGetRulesetResult(GetRulesetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRulesetResult(
            description=self.description,
            rules=self.rules,
            tags=self.tags)


def get_ruleset(name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRulesetResult:
    """
    Resource schema for AWS::DataBrew::Ruleset.


    :param str name: Name of the Ruleset
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:databrew:getRuleset', __args__, opts=opts, typ=GetRulesetResult).value

    return AwaitableGetRulesetResult(
        description=pulumi.get(__ret__, 'description'),
        rules=pulumi.get(__ret__, 'rules'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_ruleset)
def get_ruleset_output(name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRulesetResult]:
    """
    Resource schema for AWS::DataBrew::Ruleset.


    :param str name: Name of the Ruleset
    """
    ...
