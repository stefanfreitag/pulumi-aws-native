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
    'ProjectArtifacts',
    'ProjectBatchRestrictions',
    'ProjectBuildBatchConfig',
    'ProjectBuildStatusConfig',
    'ProjectCache',
    'ProjectCloudWatchLogsConfig',
    'ProjectEnvironment',
    'ProjectEnvironmentVariable',
    'ProjectFileSystemLocation',
    'ProjectFilterGroup',
    'ProjectFleet',
    'ProjectGitSubmodulesConfig',
    'ProjectLogsConfig',
    'ProjectRegistryCredential',
    'ProjectS3LogsConfig',
    'ProjectSource',
    'ProjectSourceAuth',
    'ProjectSourceVersion',
    'ProjectTriggers',
    'ProjectVpcConfig',
    'ReportGroupReportExportConfig',
    'ReportGroupS3ReportExportConfig',
]

@pulumi.output_type
class ProjectArtifacts(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "artifactIdentifier":
            suggest = "artifact_identifier"
        elif key == "encryptionDisabled":
            suggest = "encryption_disabled"
        elif key == "namespaceType":
            suggest = "namespace_type"
        elif key == "overrideArtifactName":
            suggest = "override_artifact_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectArtifacts. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectArtifacts.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectArtifacts.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: str,
                 artifact_identifier: Optional[str] = None,
                 encryption_disabled: Optional[bool] = None,
                 location: Optional[str] = None,
                 name: Optional[str] = None,
                 namespace_type: Optional[str] = None,
                 override_artifact_name: Optional[bool] = None,
                 packaging: Optional[str] = None,
                 path: Optional[str] = None):
        pulumi.set(__self__, "type", type)
        if artifact_identifier is not None:
            pulumi.set(__self__, "artifact_identifier", artifact_identifier)
        if encryption_disabled is not None:
            pulumi.set(__self__, "encryption_disabled", encryption_disabled)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace_type is not None:
            pulumi.set(__self__, "namespace_type", namespace_type)
        if override_artifact_name is not None:
            pulumi.set(__self__, "override_artifact_name", override_artifact_name)
        if packaging is not None:
            pulumi.set(__self__, "packaging", packaging)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="artifactIdentifier")
    def artifact_identifier(self) -> Optional[str]:
        return pulumi.get(self, "artifact_identifier")

    @property
    @pulumi.getter(name="encryptionDisabled")
    def encryption_disabled(self) -> Optional[bool]:
        return pulumi.get(self, "encryption_disabled")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namespaceType")
    def namespace_type(self) -> Optional[str]:
        return pulumi.get(self, "namespace_type")

    @property
    @pulumi.getter(name="overrideArtifactName")
    def override_artifact_name(self) -> Optional[bool]:
        return pulumi.get(self, "override_artifact_name")

    @property
    @pulumi.getter
    def packaging(self) -> Optional[str]:
        return pulumi.get(self, "packaging")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        return pulumi.get(self, "path")


@pulumi.output_type
class ProjectBatchRestrictions(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "computeTypesAllowed":
            suggest = "compute_types_allowed"
        elif key == "maximumBuildsAllowed":
            suggest = "maximum_builds_allowed"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectBatchRestrictions. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectBatchRestrictions.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectBatchRestrictions.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 compute_types_allowed: Optional[Sequence[str]] = None,
                 maximum_builds_allowed: Optional[int] = None):
        if compute_types_allowed is not None:
            pulumi.set(__self__, "compute_types_allowed", compute_types_allowed)
        if maximum_builds_allowed is not None:
            pulumi.set(__self__, "maximum_builds_allowed", maximum_builds_allowed)

    @property
    @pulumi.getter(name="computeTypesAllowed")
    def compute_types_allowed(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "compute_types_allowed")

    @property
    @pulumi.getter(name="maximumBuildsAllowed")
    def maximum_builds_allowed(self) -> Optional[int]:
        return pulumi.get(self, "maximum_builds_allowed")


@pulumi.output_type
class ProjectBuildBatchConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "batchReportMode":
            suggest = "batch_report_mode"
        elif key == "combineArtifacts":
            suggest = "combine_artifacts"
        elif key == "serviceRole":
            suggest = "service_role"
        elif key == "timeoutInMins":
            suggest = "timeout_in_mins"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectBuildBatchConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectBuildBatchConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectBuildBatchConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 batch_report_mode: Optional[str] = None,
                 combine_artifacts: Optional[bool] = None,
                 restrictions: Optional['outputs.ProjectBatchRestrictions'] = None,
                 service_role: Optional[str] = None,
                 timeout_in_mins: Optional[int] = None):
        if batch_report_mode is not None:
            pulumi.set(__self__, "batch_report_mode", batch_report_mode)
        if combine_artifacts is not None:
            pulumi.set(__self__, "combine_artifacts", combine_artifacts)
        if restrictions is not None:
            pulumi.set(__self__, "restrictions", restrictions)
        if service_role is not None:
            pulumi.set(__self__, "service_role", service_role)
        if timeout_in_mins is not None:
            pulumi.set(__self__, "timeout_in_mins", timeout_in_mins)

    @property
    @pulumi.getter(name="batchReportMode")
    def batch_report_mode(self) -> Optional[str]:
        return pulumi.get(self, "batch_report_mode")

    @property
    @pulumi.getter(name="combineArtifacts")
    def combine_artifacts(self) -> Optional[bool]:
        return pulumi.get(self, "combine_artifacts")

    @property
    @pulumi.getter
    def restrictions(self) -> Optional['outputs.ProjectBatchRestrictions']:
        return pulumi.get(self, "restrictions")

    @property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> Optional[str]:
        return pulumi.get(self, "service_role")

    @property
    @pulumi.getter(name="timeoutInMins")
    def timeout_in_mins(self) -> Optional[int]:
        return pulumi.get(self, "timeout_in_mins")


@pulumi.output_type
class ProjectBuildStatusConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "targetUrl":
            suggest = "target_url"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectBuildStatusConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectBuildStatusConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectBuildStatusConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 context: Optional[str] = None,
                 target_url: Optional[str] = None):
        if context is not None:
            pulumi.set(__self__, "context", context)
        if target_url is not None:
            pulumi.set(__self__, "target_url", target_url)

    @property
    @pulumi.getter
    def context(self) -> Optional[str]:
        return pulumi.get(self, "context")

    @property
    @pulumi.getter(name="targetUrl")
    def target_url(self) -> Optional[str]:
        return pulumi.get(self, "target_url")


@pulumi.output_type
class ProjectCache(dict):
    def __init__(__self__, *,
                 type: str,
                 location: Optional[str] = None,
                 modes: Optional[Sequence[str]] = None):
        pulumi.set(__self__, "type", type)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if modes is not None:
            pulumi.set(__self__, "modes", modes)

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def modes(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "modes")


@pulumi.output_type
class ProjectCloudWatchLogsConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "groupName":
            suggest = "group_name"
        elif key == "streamName":
            suggest = "stream_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectCloudWatchLogsConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectCloudWatchLogsConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectCloudWatchLogsConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 status: str,
                 group_name: Optional[str] = None,
                 stream_name: Optional[str] = None):
        pulumi.set(__self__, "status", status)
        if group_name is not None:
            pulumi.set(__self__, "group_name", group_name)
        if stream_name is not None:
            pulumi.set(__self__, "stream_name", stream_name)

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[str]:
        return pulumi.get(self, "group_name")

    @property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> Optional[str]:
        return pulumi.get(self, "stream_name")


@pulumi.output_type
class ProjectEnvironment(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "computeType":
            suggest = "compute_type"
        elif key == "environmentVariables":
            suggest = "environment_variables"
        elif key == "imagePullCredentialsType":
            suggest = "image_pull_credentials_type"
        elif key == "privilegedMode":
            suggest = "privileged_mode"
        elif key == "registryCredential":
            suggest = "registry_credential"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectEnvironment. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectEnvironment.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectEnvironment.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 compute_type: str,
                 image: str,
                 type: str,
                 certificate: Optional[str] = None,
                 environment_variables: Optional[Sequence['outputs.ProjectEnvironmentVariable']] = None,
                 fleet: Optional['outputs.ProjectFleet'] = None,
                 image_pull_credentials_type: Optional[str] = None,
                 privileged_mode: Optional[bool] = None,
                 registry_credential: Optional['outputs.ProjectRegistryCredential'] = None):
        pulumi.set(__self__, "compute_type", compute_type)
        pulumi.set(__self__, "image", image)
        pulumi.set(__self__, "type", type)
        if certificate is not None:
            pulumi.set(__self__, "certificate", certificate)
        if environment_variables is not None:
            pulumi.set(__self__, "environment_variables", environment_variables)
        if fleet is not None:
            pulumi.set(__self__, "fleet", fleet)
        if image_pull_credentials_type is not None:
            pulumi.set(__self__, "image_pull_credentials_type", image_pull_credentials_type)
        if privileged_mode is not None:
            pulumi.set(__self__, "privileged_mode", privileged_mode)
        if registry_credential is not None:
            pulumi.set(__self__, "registry_credential", registry_credential)

    @property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> str:
        return pulumi.get(self, "compute_type")

    @property
    @pulumi.getter
    def image(self) -> str:
        return pulumi.get(self, "image")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def certificate(self) -> Optional[str]:
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Sequence['outputs.ProjectEnvironmentVariable']]:
        return pulumi.get(self, "environment_variables")

    @property
    @pulumi.getter
    def fleet(self) -> Optional['outputs.ProjectFleet']:
        return pulumi.get(self, "fleet")

    @property
    @pulumi.getter(name="imagePullCredentialsType")
    def image_pull_credentials_type(self) -> Optional[str]:
        return pulumi.get(self, "image_pull_credentials_type")

    @property
    @pulumi.getter(name="privilegedMode")
    def privileged_mode(self) -> Optional[bool]:
        return pulumi.get(self, "privileged_mode")

    @property
    @pulumi.getter(name="registryCredential")
    def registry_credential(self) -> Optional['outputs.ProjectRegistryCredential']:
        return pulumi.get(self, "registry_credential")


@pulumi.output_type
class ProjectEnvironmentVariable(dict):
    def __init__(__self__, *,
                 name: str,
                 value: str,
                 type: Optional[str] = None):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")


@pulumi.output_type
class ProjectFileSystemLocation(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "mountPoint":
            suggest = "mount_point"
        elif key == "mountOptions":
            suggest = "mount_options"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectFileSystemLocation. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectFileSystemLocation.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectFileSystemLocation.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 identifier: str,
                 location: str,
                 mount_point: str,
                 type: str,
                 mount_options: Optional[str] = None):
        pulumi.set(__self__, "identifier", identifier)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "mount_point", mount_point)
        pulumi.set(__self__, "type", type)
        if mount_options is not None:
            pulumi.set(__self__, "mount_options", mount_options)

    @property
    @pulumi.getter
    def identifier(self) -> str:
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def location(self) -> str:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mountPoint")
    def mount_point(self) -> str:
        return pulumi.get(self, "mount_point")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[str]:
        return pulumi.get(self, "mount_options")


@pulumi.output_type
class ProjectFilterGroup(dict):
    def __init__(__self__):
        pass


@pulumi.output_type
class ProjectFleet(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fleetArn":
            suggest = "fleet_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectFleet. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectFleet.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectFleet.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 fleet_arn: Optional[str] = None):
        if fleet_arn is not None:
            pulumi.set(__self__, "fleet_arn", fleet_arn)

    @property
    @pulumi.getter(name="fleetArn")
    def fleet_arn(self) -> Optional[str]:
        return pulumi.get(self, "fleet_arn")


@pulumi.output_type
class ProjectGitSubmodulesConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fetchSubmodules":
            suggest = "fetch_submodules"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectGitSubmodulesConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectGitSubmodulesConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectGitSubmodulesConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 fetch_submodules: bool):
        pulumi.set(__self__, "fetch_submodules", fetch_submodules)

    @property
    @pulumi.getter(name="fetchSubmodules")
    def fetch_submodules(self) -> bool:
        return pulumi.get(self, "fetch_submodules")


@pulumi.output_type
class ProjectLogsConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cloudWatchLogs":
            suggest = "cloud_watch_logs"
        elif key == "s3Logs":
            suggest = "s3_logs"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectLogsConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectLogsConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectLogsConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cloud_watch_logs: Optional['outputs.ProjectCloudWatchLogsConfig'] = None,
                 s3_logs: Optional['outputs.ProjectS3LogsConfig'] = None):
        if cloud_watch_logs is not None:
            pulumi.set(__self__, "cloud_watch_logs", cloud_watch_logs)
        if s3_logs is not None:
            pulumi.set(__self__, "s3_logs", s3_logs)

    @property
    @pulumi.getter(name="cloudWatchLogs")
    def cloud_watch_logs(self) -> Optional['outputs.ProjectCloudWatchLogsConfig']:
        return pulumi.get(self, "cloud_watch_logs")

    @property
    @pulumi.getter(name="s3Logs")
    def s3_logs(self) -> Optional['outputs.ProjectS3LogsConfig']:
        return pulumi.get(self, "s3_logs")


@pulumi.output_type
class ProjectRegistryCredential(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "credentialProvider":
            suggest = "credential_provider"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectRegistryCredential. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectRegistryCredential.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectRegistryCredential.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 credential: str,
                 credential_provider: str):
        pulumi.set(__self__, "credential", credential)
        pulumi.set(__self__, "credential_provider", credential_provider)

    @property
    @pulumi.getter
    def credential(self) -> str:
        return pulumi.get(self, "credential")

    @property
    @pulumi.getter(name="credentialProvider")
    def credential_provider(self) -> str:
        return pulumi.get(self, "credential_provider")


@pulumi.output_type
class ProjectS3LogsConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "encryptionDisabled":
            suggest = "encryption_disabled"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectS3LogsConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectS3LogsConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectS3LogsConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 status: str,
                 encryption_disabled: Optional[bool] = None,
                 location: Optional[str] = None):
        pulumi.set(__self__, "status", status)
        if encryption_disabled is not None:
            pulumi.set(__self__, "encryption_disabled", encryption_disabled)
        if location is not None:
            pulumi.set(__self__, "location", location)

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="encryptionDisabled")
    def encryption_disabled(self) -> Optional[bool]:
        return pulumi.get(self, "encryption_disabled")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        return pulumi.get(self, "location")


@pulumi.output_type
class ProjectSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "buildSpec":
            suggest = "build_spec"
        elif key == "buildStatusConfig":
            suggest = "build_status_config"
        elif key == "gitCloneDepth":
            suggest = "git_clone_depth"
        elif key == "gitSubmodulesConfig":
            suggest = "git_submodules_config"
        elif key == "insecureSsl":
            suggest = "insecure_ssl"
        elif key == "reportBuildStatus":
            suggest = "report_build_status"
        elif key == "sourceIdentifier":
            suggest = "source_identifier"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: str,
                 auth: Optional['outputs.ProjectSourceAuth'] = None,
                 build_spec: Optional[str] = None,
                 build_status_config: Optional['outputs.ProjectBuildStatusConfig'] = None,
                 git_clone_depth: Optional[int] = None,
                 git_submodules_config: Optional['outputs.ProjectGitSubmodulesConfig'] = None,
                 insecure_ssl: Optional[bool] = None,
                 location: Optional[str] = None,
                 report_build_status: Optional[bool] = None,
                 source_identifier: Optional[str] = None):
        pulumi.set(__self__, "type", type)
        if auth is not None:
            pulumi.set(__self__, "auth", auth)
        if build_spec is not None:
            pulumi.set(__self__, "build_spec", build_spec)
        if build_status_config is not None:
            pulumi.set(__self__, "build_status_config", build_status_config)
        if git_clone_depth is not None:
            pulumi.set(__self__, "git_clone_depth", git_clone_depth)
        if git_submodules_config is not None:
            pulumi.set(__self__, "git_submodules_config", git_submodules_config)
        if insecure_ssl is not None:
            pulumi.set(__self__, "insecure_ssl", insecure_ssl)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if report_build_status is not None:
            pulumi.set(__self__, "report_build_status", report_build_status)
        if source_identifier is not None:
            pulumi.set(__self__, "source_identifier", source_identifier)

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def auth(self) -> Optional['outputs.ProjectSourceAuth']:
        return pulumi.get(self, "auth")

    @property
    @pulumi.getter(name="buildSpec")
    def build_spec(self) -> Optional[str]:
        return pulumi.get(self, "build_spec")

    @property
    @pulumi.getter(name="buildStatusConfig")
    def build_status_config(self) -> Optional['outputs.ProjectBuildStatusConfig']:
        return pulumi.get(self, "build_status_config")

    @property
    @pulumi.getter(name="gitCloneDepth")
    def git_clone_depth(self) -> Optional[int]:
        return pulumi.get(self, "git_clone_depth")

    @property
    @pulumi.getter(name="gitSubmodulesConfig")
    def git_submodules_config(self) -> Optional['outputs.ProjectGitSubmodulesConfig']:
        return pulumi.get(self, "git_submodules_config")

    @property
    @pulumi.getter(name="insecureSsl")
    def insecure_ssl(self) -> Optional[bool]:
        return pulumi.get(self, "insecure_ssl")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="reportBuildStatus")
    def report_build_status(self) -> Optional[bool]:
        return pulumi.get(self, "report_build_status")

    @property
    @pulumi.getter(name="sourceIdentifier")
    def source_identifier(self) -> Optional[str]:
        return pulumi.get(self, "source_identifier")


@pulumi.output_type
class ProjectSourceAuth(dict):
    def __init__(__self__, *,
                 type: str,
                 resource: Optional[str] = None):
        pulumi.set(__self__, "type", type)
        if resource is not None:
            pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def resource(self) -> Optional[str]:
        return pulumi.get(self, "resource")


@pulumi.output_type
class ProjectSourceVersion(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "sourceIdentifier":
            suggest = "source_identifier"
        elif key == "sourceVersion":
            suggest = "source_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectSourceVersion. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectSourceVersion.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectSourceVersion.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 source_identifier: str,
                 source_version: Optional[str] = None):
        pulumi.set(__self__, "source_identifier", source_identifier)
        if source_version is not None:
            pulumi.set(__self__, "source_version", source_version)

    @property
    @pulumi.getter(name="sourceIdentifier")
    def source_identifier(self) -> str:
        return pulumi.get(self, "source_identifier")

    @property
    @pulumi.getter(name="sourceVersion")
    def source_version(self) -> Optional[str]:
        return pulumi.get(self, "source_version")


@pulumi.output_type
class ProjectTriggers(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "buildType":
            suggest = "build_type"
        elif key == "filterGroups":
            suggest = "filter_groups"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectTriggers. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectTriggers.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectTriggers.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 build_type: Optional[str] = None,
                 filter_groups: Optional[Sequence['outputs.ProjectFilterGroup']] = None,
                 webhook: Optional[bool] = None):
        if build_type is not None:
            pulumi.set(__self__, "build_type", build_type)
        if filter_groups is not None:
            pulumi.set(__self__, "filter_groups", filter_groups)
        if webhook is not None:
            pulumi.set(__self__, "webhook", webhook)

    @property
    @pulumi.getter(name="buildType")
    def build_type(self) -> Optional[str]:
        return pulumi.get(self, "build_type")

    @property
    @pulumi.getter(name="filterGroups")
    def filter_groups(self) -> Optional[Sequence['outputs.ProjectFilterGroup']]:
        return pulumi.get(self, "filter_groups")

    @property
    @pulumi.getter
    def webhook(self) -> Optional[bool]:
        return pulumi.get(self, "webhook")


@pulumi.output_type
class ProjectVpcConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "securityGroupIds":
            suggest = "security_group_ids"
        elif key == "vpcId":
            suggest = "vpc_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectVpcConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectVpcConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectVpcConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 security_group_ids: Optional[Sequence[str]] = None,
                 subnets: Optional[Sequence[str]] = None,
                 vpc_id: Optional[str] = None):
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if subnets is not None:
            pulumi.set(__self__, "subnets", subnets)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "subnets")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[str]:
        return pulumi.get(self, "vpc_id")


@pulumi.output_type
class ReportGroupReportExportConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "exportConfigType":
            suggest = "export_config_type"
        elif key == "s3Destination":
            suggest = "s3_destination"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ReportGroupReportExportConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ReportGroupReportExportConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ReportGroupReportExportConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 export_config_type: str,
                 s3_destination: Optional['outputs.ReportGroupS3ReportExportConfig'] = None):
        pulumi.set(__self__, "export_config_type", export_config_type)
        if s3_destination is not None:
            pulumi.set(__self__, "s3_destination", s3_destination)

    @property
    @pulumi.getter(name="exportConfigType")
    def export_config_type(self) -> str:
        return pulumi.get(self, "export_config_type")

    @property
    @pulumi.getter(name="s3Destination")
    def s3_destination(self) -> Optional['outputs.ReportGroupS3ReportExportConfig']:
        return pulumi.get(self, "s3_destination")


@pulumi.output_type
class ReportGroupS3ReportExportConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bucketOwner":
            suggest = "bucket_owner"
        elif key == "encryptionDisabled":
            suggest = "encryption_disabled"
        elif key == "encryptionKey":
            suggest = "encryption_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ReportGroupS3ReportExportConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ReportGroupS3ReportExportConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ReportGroupS3ReportExportConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bucket: str,
                 bucket_owner: Optional[str] = None,
                 encryption_disabled: Optional[bool] = None,
                 encryption_key: Optional[str] = None,
                 packaging: Optional[str] = None,
                 path: Optional[str] = None):
        pulumi.set(__self__, "bucket", bucket)
        if bucket_owner is not None:
            pulumi.set(__self__, "bucket_owner", bucket_owner)
        if encryption_disabled is not None:
            pulumi.set(__self__, "encryption_disabled", encryption_disabled)
        if encryption_key is not None:
            pulumi.set(__self__, "encryption_key", encryption_key)
        if packaging is not None:
            pulumi.set(__self__, "packaging", packaging)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter
    def bucket(self) -> str:
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="bucketOwner")
    def bucket_owner(self) -> Optional[str]:
        return pulumi.get(self, "bucket_owner")

    @property
    @pulumi.getter(name="encryptionDisabled")
    def encryption_disabled(self) -> Optional[bool]:
        return pulumi.get(self, "encryption_disabled")

    @property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[str]:
        return pulumi.get(self, "encryption_key")

    @property
    @pulumi.getter
    def packaging(self) -> Optional[str]:
        return pulumi.get(self, "packaging")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        return pulumi.get(self, "path")


