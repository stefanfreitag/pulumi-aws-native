# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetTypeActivationResult',
    'AwaitableGetTypeActivationResult',
    'get_type_activation',
    'get_type_activation_output',
]

@pulumi.output_type
class GetTypeActivationResult:
    def __init__(__self__, arn=None, public_type_arn=None, publisher_id=None, type_name=None, type_name_alias=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if public_type_arn and not isinstance(public_type_arn, str):
            raise TypeError("Expected argument 'public_type_arn' to be a str")
        pulumi.set(__self__, "public_type_arn", public_type_arn)
        if publisher_id and not isinstance(publisher_id, str):
            raise TypeError("Expected argument 'publisher_id' to be a str")
        pulumi.set(__self__, "publisher_id", publisher_id)
        if type_name and not isinstance(type_name, str):
            raise TypeError("Expected argument 'type_name' to be a str")
        pulumi.set(__self__, "type_name", type_name)
        if type_name_alias and not isinstance(type_name_alias, str):
            raise TypeError("Expected argument 'type_name_alias' to be a str")
        pulumi.set(__self__, "type_name_alias", type_name_alias)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the extension.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="publicTypeArn")
    def public_type_arn(self) -> Optional[str]:
        """
        The Amazon Resource Number (ARN) assigned to the public extension upon publication
        """
        return pulumi.get(self, "public_type_arn")

    @property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> Optional[str]:
        """
        The publisher id assigned by CloudFormation for publishing in this region.
        """
        return pulumi.get(self, "publisher_id")

    @property
    @pulumi.getter(name="typeName")
    def type_name(self) -> Optional[str]:
        """
        The name of the type being registered.

        We recommend that type names adhere to the following pattern: company_or_organization::service::type.
        """
        return pulumi.get(self, "type_name")

    @property
    @pulumi.getter(name="typeNameAlias")
    def type_name_alias(self) -> Optional[str]:
        """
        An alias to assign to the public extension in this account and region. If you specify an alias for the extension, you must then use the alias to refer to the extension in your templates.
        """
        return pulumi.get(self, "type_name_alias")


class AwaitableGetTypeActivationResult(GetTypeActivationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTypeActivationResult(
            arn=self.arn,
            public_type_arn=self.public_type_arn,
            publisher_id=self.publisher_id,
            type_name=self.type_name,
            type_name_alias=self.type_name_alias)


def get_type_activation(arn: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTypeActivationResult:
    """
    Enable a resource that has been published in the CloudFormation Registry.


    :param str arn: The Amazon Resource Name (ARN) of the extension.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cloudformation:getTypeActivation', __args__, opts=opts, typ=GetTypeActivationResult).value

    return AwaitableGetTypeActivationResult(
        arn=pulumi.get(__ret__, 'arn'),
        public_type_arn=pulumi.get(__ret__, 'public_type_arn'),
        publisher_id=pulumi.get(__ret__, 'publisher_id'),
        type_name=pulumi.get(__ret__, 'type_name'),
        type_name_alias=pulumi.get(__ret__, 'type_name_alias'))


@_utilities.lift_output_func(get_type_activation)
def get_type_activation_output(arn: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTypeActivationResult]:
    """
    Enable a resource that has been published in the CloudFormation Registry.


    :param str arn: The Amazon Resource Name (ARN) of the extension.
    """
    ...
