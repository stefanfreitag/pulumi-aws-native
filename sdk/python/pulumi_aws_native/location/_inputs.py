# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'MapConfigurationArgs',
    'PlaceIndexDataSourceConfigurationArgs',
]

@pulumi.input_type
class MapConfigurationArgs:
    def __init__(__self__, *,
                 style: pulumi.Input[str]):
        MapConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            style=style,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             style: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("style", style)

    @property
    @pulumi.getter
    def style(self) -> pulumi.Input[str]:
        return pulumi.get(self, "style")

    @style.setter
    def style(self, value: pulumi.Input[str]):
        pulumi.set(self, "style", value)


@pulumi.input_type
class PlaceIndexDataSourceConfigurationArgs:
    def __init__(__self__, *,
                 intended_use: Optional[pulumi.Input['PlaceIndexIntendedUse']] = None):
        PlaceIndexDataSourceConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            intended_use=intended_use,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             intended_use: Optional[pulumi.Input['PlaceIndexIntendedUse']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if intended_use is not None:
            _setter("intended_use", intended_use)

    @property
    @pulumi.getter(name="intendedUse")
    def intended_use(self) -> Optional[pulumi.Input['PlaceIndexIntendedUse']]:
        return pulumi.get(self, "intended_use")

    @intended_use.setter
    def intended_use(self, value: Optional[pulumi.Input['PlaceIndexIntendedUse']]):
        pulumi.set(self, "intended_use", value)


