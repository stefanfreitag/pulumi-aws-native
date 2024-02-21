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

__all__ = [
    'GetLandingZoneResult',
    'AwaitableGetLandingZoneResult',
    'get_landing_zone',
    'get_landing_zone_output',
]

@pulumi.output_type
class GetLandingZoneResult:
    def __init__(__self__, arn=None, drift_status=None, landing_zone_identifier=None, latest_available_version=None, manifest=None, status=None, tags=None, version=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if drift_status and not isinstance(drift_status, str):
            raise TypeError("Expected argument 'drift_status' to be a str")
        pulumi.set(__self__, "drift_status", drift_status)
        if landing_zone_identifier and not isinstance(landing_zone_identifier, str):
            raise TypeError("Expected argument 'landing_zone_identifier' to be a str")
        pulumi.set(__self__, "landing_zone_identifier", landing_zone_identifier)
        if latest_available_version and not isinstance(latest_available_version, str):
            raise TypeError("Expected argument 'latest_available_version' to be a str")
        pulumi.set(__self__, "latest_available_version", latest_available_version)
        if manifest and not isinstance(manifest, dict):
            raise TypeError("Expected argument 'manifest' to be a dict")
        pulumi.set(__self__, "manifest", manifest)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="driftStatus")
    def drift_status(self) -> Optional['LandingZoneDriftStatus']:
        return pulumi.get(self, "drift_status")

    @property
    @pulumi.getter(name="landingZoneIdentifier")
    def landing_zone_identifier(self) -> Optional[str]:
        return pulumi.get(self, "landing_zone_identifier")

    @property
    @pulumi.getter(name="latestAvailableVersion")
    def latest_available_version(self) -> Optional[str]:
        return pulumi.get(self, "latest_available_version")

    @property
    @pulumi.getter
    def manifest(self) -> Optional[Any]:
        """
        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ControlTower::LandingZone` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "manifest")

    @property
    @pulumi.getter
    def status(self) -> Optional['LandingZoneStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.LandingZoneTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        return pulumi.get(self, "version")


class AwaitableGetLandingZoneResult(GetLandingZoneResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLandingZoneResult(
            arn=self.arn,
            drift_status=self.drift_status,
            landing_zone_identifier=self.landing_zone_identifier,
            latest_available_version=self.latest_available_version,
            manifest=self.manifest,
            status=self.status,
            tags=self.tags,
            version=self.version)


def get_landing_zone(landing_zone_identifier: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLandingZoneResult:
    """
    Definition of AWS::ControlTower::LandingZone Resource Type
    """
    __args__ = dict()
    __args__['landingZoneIdentifier'] = landing_zone_identifier
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:controltower:getLandingZone', __args__, opts=opts, typ=GetLandingZoneResult).value

    return AwaitableGetLandingZoneResult(
        arn=pulumi.get(__ret__, 'arn'),
        drift_status=pulumi.get(__ret__, 'drift_status'),
        landing_zone_identifier=pulumi.get(__ret__, 'landing_zone_identifier'),
        latest_available_version=pulumi.get(__ret__, 'latest_available_version'),
        manifest=pulumi.get(__ret__, 'manifest'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_landing_zone)
def get_landing_zone_output(landing_zone_identifier: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLandingZoneResult]:
    """
    Definition of AWS::ControlTower::LandingZone Resource Type
    """
    ...
