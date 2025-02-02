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

__all__ = [
    'GetWebAclResult',
    'AwaitableGetWebAclResult',
    'get_web_acl',
    'get_web_acl_output',
]

@pulumi.output_type
class GetWebAclResult:
    def __init__(__self__, default_action=None, id=None, rules=None):
        if default_action and not isinstance(default_action, dict):
            raise TypeError("Expected argument 'default_action' to be a dict")
        pulumi.set(__self__, "default_action", default_action)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional['outputs.WebAclWafAction']:
        return pulumi.get(self, "default_action")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def rules(self) -> Optional[Sequence['outputs.WebAclActivatedRule']]:
        return pulumi.get(self, "rules")


class AwaitableGetWebAclResult(GetWebAclResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebAclResult(
            default_action=self.default_action,
            id=self.id,
            rules=self.rules)


def get_web_acl(id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebAclResult:
    """
    Resource Type definition for AWS::WAF::WebACL
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:waf:getWebAcl', __args__, opts=opts, typ=GetWebAclResult).value

    return AwaitableGetWebAclResult(
        default_action=pulumi.get(__ret__, 'default_action'),
        id=pulumi.get(__ret__, 'id'),
        rules=pulumi.get(__ret__, 'rules'))


@_utilities.lift_output_func(get_web_acl)
def get_web_acl_output(id: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebAclResult]:
    """
    Resource Type definition for AWS::WAF::WebACL
    """
    ...
