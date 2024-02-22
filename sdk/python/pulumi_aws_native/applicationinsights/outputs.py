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
    'ApplicationAlarm',
    'ApplicationAlarmMetric',
    'ApplicationComponentConfiguration',
    'ApplicationComponentMonitoringSetting',
    'ApplicationConfigurationDetails',
    'ApplicationCustomComponent',
    'ApplicationHaClusterPrometheusExporter',
    'ApplicationHanaPrometheusExporter',
    'ApplicationJmxPrometheusExporter',
    'ApplicationLog',
    'ApplicationLogPattern',
    'ApplicationLogPatternSet',
    'ApplicationSubComponentConfigurationDetails',
    'ApplicationSubComponentTypeConfiguration',
    'ApplicationWindowsEvent',
]

@pulumi.output_type
class ApplicationAlarm(dict):
    """
    A CloudWatch alarm to be monitored for the component.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "alarmName":
            suggest = "alarm_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationAlarm. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationAlarm.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationAlarm.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 alarm_name: str,
                 severity: Optional['ApplicationAlarmSeverity'] = None):
        """
        A CloudWatch alarm to be monitored for the component.
        :param str alarm_name: The name of the CloudWatch alarm to be monitored for the component.
        :param 'ApplicationAlarmSeverity' severity: Indicates the degree of outage when the alarm goes off.
        """
        pulumi.set(__self__, "alarm_name", alarm_name)
        if severity is not None:
            pulumi.set(__self__, "severity", severity)

    @property
    @pulumi.getter(name="alarmName")
    def alarm_name(self) -> str:
        """
        The name of the CloudWatch alarm to be monitored for the component.
        """
        return pulumi.get(self, "alarm_name")

    @property
    @pulumi.getter
    def severity(self) -> Optional['ApplicationAlarmSeverity']:
        """
        Indicates the degree of outage when the alarm goes off.
        """
        return pulumi.get(self, "severity")


@pulumi.output_type
class ApplicationAlarmMetric(dict):
    """
    A metric to be monitored for the component.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "alarmMetricName":
            suggest = "alarm_metric_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationAlarmMetric. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationAlarmMetric.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationAlarmMetric.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 alarm_metric_name: str):
        """
        A metric to be monitored for the component.
        :param str alarm_metric_name: The name of the metric to be monitored for the component.
        """
        pulumi.set(__self__, "alarm_metric_name", alarm_metric_name)

    @property
    @pulumi.getter(name="alarmMetricName")
    def alarm_metric_name(self) -> str:
        """
        The name of the metric to be monitored for the component.
        """
        return pulumi.get(self, "alarm_metric_name")


@pulumi.output_type
class ApplicationComponentConfiguration(dict):
    """
    The configuration settings of the component.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "configurationDetails":
            suggest = "configuration_details"
        elif key == "subComponentTypeConfigurations":
            suggest = "sub_component_type_configurations"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationComponentConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationComponentConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationComponentConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 configuration_details: Optional['outputs.ApplicationConfigurationDetails'] = None,
                 sub_component_type_configurations: Optional[Sequence['outputs.ApplicationSubComponentTypeConfiguration']] = None):
        """
        The configuration settings of the component.
        :param 'ApplicationConfigurationDetails' configuration_details: The configuration settings
        :param Sequence['ApplicationSubComponentTypeConfiguration'] sub_component_type_configurations: Sub component configurations of the component.
        """
        if configuration_details is not None:
            pulumi.set(__self__, "configuration_details", configuration_details)
        if sub_component_type_configurations is not None:
            pulumi.set(__self__, "sub_component_type_configurations", sub_component_type_configurations)

    @property
    @pulumi.getter(name="configurationDetails")
    def configuration_details(self) -> Optional['outputs.ApplicationConfigurationDetails']:
        """
        The configuration settings
        """
        return pulumi.get(self, "configuration_details")

    @property
    @pulumi.getter(name="subComponentTypeConfigurations")
    def sub_component_type_configurations(self) -> Optional[Sequence['outputs.ApplicationSubComponentTypeConfiguration']]:
        """
        Sub component configurations of the component.
        """
        return pulumi.get(self, "sub_component_type_configurations")


@pulumi.output_type
class ApplicationComponentMonitoringSetting(dict):
    """
    The monitoring setting of the component.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "componentConfigurationMode":
            suggest = "component_configuration_mode"
        elif key == "componentArn":
            suggest = "component_arn"
        elif key == "componentName":
            suggest = "component_name"
        elif key == "customComponentConfiguration":
            suggest = "custom_component_configuration"
        elif key == "defaultOverwriteComponentConfiguration":
            suggest = "default_overwrite_component_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationComponentMonitoringSetting. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationComponentMonitoringSetting.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationComponentMonitoringSetting.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 component_configuration_mode: 'ApplicationComponentMonitoringSettingComponentConfigurationMode',
                 tier: str,
                 component_arn: Optional[str] = None,
                 component_name: Optional[str] = None,
                 custom_component_configuration: Optional['outputs.ApplicationComponentConfiguration'] = None,
                 default_overwrite_component_configuration: Optional['outputs.ApplicationComponentConfiguration'] = None):
        """
        The monitoring setting of the component.
        :param 'ApplicationComponentMonitoringSettingComponentConfigurationMode' component_configuration_mode: The component monitoring configuration mode.
        :param str tier: The tier of the application component.
        :param str component_arn: The ARN of the compnonent.
        :param str component_name: The name of the component.
        :param 'ApplicationComponentConfiguration' custom_component_configuration: The monitoring configuration of the component.
        :param 'ApplicationComponentConfiguration' default_overwrite_component_configuration: The overwritten settings on default component monitoring configuration.
        """
        pulumi.set(__self__, "component_configuration_mode", component_configuration_mode)
        pulumi.set(__self__, "tier", tier)
        if component_arn is not None:
            pulumi.set(__self__, "component_arn", component_arn)
        if component_name is not None:
            pulumi.set(__self__, "component_name", component_name)
        if custom_component_configuration is not None:
            pulumi.set(__self__, "custom_component_configuration", custom_component_configuration)
        if default_overwrite_component_configuration is not None:
            pulumi.set(__self__, "default_overwrite_component_configuration", default_overwrite_component_configuration)

    @property
    @pulumi.getter(name="componentConfigurationMode")
    def component_configuration_mode(self) -> 'ApplicationComponentMonitoringSettingComponentConfigurationMode':
        """
        The component monitoring configuration mode.
        """
        return pulumi.get(self, "component_configuration_mode")

    @property
    @pulumi.getter
    def tier(self) -> str:
        """
        The tier of the application component.
        """
        return pulumi.get(self, "tier")

    @property
    @pulumi.getter(name="componentArn")
    def component_arn(self) -> Optional[str]:
        """
        The ARN of the compnonent.
        """
        return pulumi.get(self, "component_arn")

    @property
    @pulumi.getter(name="componentName")
    def component_name(self) -> Optional[str]:
        """
        The name of the component.
        """
        return pulumi.get(self, "component_name")

    @property
    @pulumi.getter(name="customComponentConfiguration")
    def custom_component_configuration(self) -> Optional['outputs.ApplicationComponentConfiguration']:
        """
        The monitoring configuration of the component.
        """
        return pulumi.get(self, "custom_component_configuration")

    @property
    @pulumi.getter(name="defaultOverwriteComponentConfiguration")
    def default_overwrite_component_configuration(self) -> Optional['outputs.ApplicationComponentConfiguration']:
        """
        The overwritten settings on default component monitoring configuration.
        """
        return pulumi.get(self, "default_overwrite_component_configuration")


@pulumi.output_type
class ApplicationConfigurationDetails(dict):
    """
    The configuration settings.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "alarmMetrics":
            suggest = "alarm_metrics"
        elif key == "haClusterPrometheusExporter":
            suggest = "ha_cluster_prometheus_exporter"
        elif key == "hanaPrometheusExporter":
            suggest = "hana_prometheus_exporter"
        elif key == "jmxPrometheusExporter":
            suggest = "jmx_prometheus_exporter"
        elif key == "windowsEvents":
            suggest = "windows_events"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationConfigurationDetails. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationConfigurationDetails.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationConfigurationDetails.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 alarm_metrics: Optional[Sequence['outputs.ApplicationAlarmMetric']] = None,
                 alarms: Optional[Sequence['outputs.ApplicationAlarm']] = None,
                 ha_cluster_prometheus_exporter: Optional['outputs.ApplicationHaClusterPrometheusExporter'] = None,
                 hana_prometheus_exporter: Optional['outputs.ApplicationHanaPrometheusExporter'] = None,
                 jmx_prometheus_exporter: Optional['outputs.ApplicationJmxPrometheusExporter'] = None,
                 logs: Optional[Sequence['outputs.ApplicationLog']] = None,
                 windows_events: Optional[Sequence['outputs.ApplicationWindowsEvent']] = None):
        """
        The configuration settings.
        :param Sequence['ApplicationAlarmMetric'] alarm_metrics: A list of metrics to monitor for the component.
        :param Sequence['ApplicationAlarm'] alarms: A list of alarms to monitor for the component.
        :param 'ApplicationHaClusterPrometheusExporter' ha_cluster_prometheus_exporter: The HA cluster Prometheus Exporter settings.
        :param 'ApplicationHanaPrometheusExporter' hana_prometheus_exporter: The HANA DB Prometheus Exporter settings.
        :param 'ApplicationJmxPrometheusExporter' jmx_prometheus_exporter: The JMX Prometheus Exporter settings.
        :param Sequence['ApplicationLog'] logs: A list of logs to monitor for the component.
        :param Sequence['ApplicationWindowsEvent'] windows_events: A list of Windows Events to log.
        """
        if alarm_metrics is not None:
            pulumi.set(__self__, "alarm_metrics", alarm_metrics)
        if alarms is not None:
            pulumi.set(__self__, "alarms", alarms)
        if ha_cluster_prometheus_exporter is not None:
            pulumi.set(__self__, "ha_cluster_prometheus_exporter", ha_cluster_prometheus_exporter)
        if hana_prometheus_exporter is not None:
            pulumi.set(__self__, "hana_prometheus_exporter", hana_prometheus_exporter)
        if jmx_prometheus_exporter is not None:
            pulumi.set(__self__, "jmx_prometheus_exporter", jmx_prometheus_exporter)
        if logs is not None:
            pulumi.set(__self__, "logs", logs)
        if windows_events is not None:
            pulumi.set(__self__, "windows_events", windows_events)

    @property
    @pulumi.getter(name="alarmMetrics")
    def alarm_metrics(self) -> Optional[Sequence['outputs.ApplicationAlarmMetric']]:
        """
        A list of metrics to monitor for the component.
        """
        return pulumi.get(self, "alarm_metrics")

    @property
    @pulumi.getter
    def alarms(self) -> Optional[Sequence['outputs.ApplicationAlarm']]:
        """
        A list of alarms to monitor for the component.
        """
        return pulumi.get(self, "alarms")

    @property
    @pulumi.getter(name="haClusterPrometheusExporter")
    def ha_cluster_prometheus_exporter(self) -> Optional['outputs.ApplicationHaClusterPrometheusExporter']:
        """
        The HA cluster Prometheus Exporter settings.
        """
        return pulumi.get(self, "ha_cluster_prometheus_exporter")

    @property
    @pulumi.getter(name="hanaPrometheusExporter")
    def hana_prometheus_exporter(self) -> Optional['outputs.ApplicationHanaPrometheusExporter']:
        """
        The HANA DB Prometheus Exporter settings.
        """
        return pulumi.get(self, "hana_prometheus_exporter")

    @property
    @pulumi.getter(name="jmxPrometheusExporter")
    def jmx_prometheus_exporter(self) -> Optional['outputs.ApplicationJmxPrometheusExporter']:
        """
        The JMX Prometheus Exporter settings.
        """
        return pulumi.get(self, "jmx_prometheus_exporter")

    @property
    @pulumi.getter
    def logs(self) -> Optional[Sequence['outputs.ApplicationLog']]:
        """
        A list of logs to monitor for the component.
        """
        return pulumi.get(self, "logs")

    @property
    @pulumi.getter(name="windowsEvents")
    def windows_events(self) -> Optional[Sequence['outputs.ApplicationWindowsEvent']]:
        """
        A list of Windows Events to log.
        """
        return pulumi.get(self, "windows_events")


@pulumi.output_type
class ApplicationCustomComponent(dict):
    """
    The custom grouped component.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "componentName":
            suggest = "component_name"
        elif key == "resourceList":
            suggest = "resource_list"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationCustomComponent. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationCustomComponent.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationCustomComponent.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 component_name: str,
                 resource_list: Sequence[str]):
        """
        The custom grouped component.
        :param str component_name: The name of the component.
        :param Sequence[str] resource_list: The list of resource ARNs that belong to the component.
        """
        pulumi.set(__self__, "component_name", component_name)
        pulumi.set(__self__, "resource_list", resource_list)

    @property
    @pulumi.getter(name="componentName")
    def component_name(self) -> str:
        """
        The name of the component.
        """
        return pulumi.get(self, "component_name")

    @property
    @pulumi.getter(name="resourceList")
    def resource_list(self) -> Sequence[str]:
        """
        The list of resource ARNs that belong to the component.
        """
        return pulumi.get(self, "resource_list")


@pulumi.output_type
class ApplicationHaClusterPrometheusExporter(dict):
    """
    The HA cluster Prometheus Exporter settings.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "prometheusPort":
            suggest = "prometheus_port"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationHaClusterPrometheusExporter. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationHaClusterPrometheusExporter.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationHaClusterPrometheusExporter.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 prometheus_port: Optional[str] = None):
        """
        The HA cluster Prometheus Exporter settings.
        :param str prometheus_port: Prometheus exporter port.
        """
        if prometheus_port is not None:
            pulumi.set(__self__, "prometheus_port", prometheus_port)

    @property
    @pulumi.getter(name="prometheusPort")
    def prometheus_port(self) -> Optional[str]:
        """
        Prometheus exporter port.
        """
        return pulumi.get(self, "prometheus_port")


@pulumi.output_type
class ApplicationHanaPrometheusExporter(dict):
    """
    The HANA DB Prometheus Exporter settings.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "agreeToInstallHanadbClient":
            suggest = "agree_to_install_hanadb_client"
        elif key == "hanaPort":
            suggest = "hana_port"
        elif key == "hanaSecretName":
            suggest = "hana_secret_name"
        elif key == "prometheusPort":
            suggest = "prometheus_port"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationHanaPrometheusExporter. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationHanaPrometheusExporter.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationHanaPrometheusExporter.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 agree_to_install_hanadb_client: bool,
                 hana_port: str,
                 hana_secret_name: str,
                 hanasid: str,
                 prometheus_port: Optional[str] = None):
        """
        The HANA DB Prometheus Exporter settings.
        :param bool agree_to_install_hanadb_client: A flag which indicates agreeing to install SAP HANA DB client.
        :param str hana_port: The HANA DB port.
        :param str hana_secret_name: The secret name which manages the HANA DB credentials e.g. {
                 "username": "<>",
                 "password": "<>"
               }.
        :param str hanasid: HANA DB SID.
        :param str prometheus_port: Prometheus exporter port.
        """
        pulumi.set(__self__, "agree_to_install_hanadb_client", agree_to_install_hanadb_client)
        pulumi.set(__self__, "hana_port", hana_port)
        pulumi.set(__self__, "hana_secret_name", hana_secret_name)
        pulumi.set(__self__, "hanasid", hanasid)
        if prometheus_port is not None:
            pulumi.set(__self__, "prometheus_port", prometheus_port)

    @property
    @pulumi.getter(name="agreeToInstallHanadbClient")
    def agree_to_install_hanadb_client(self) -> bool:
        """
        A flag which indicates agreeing to install SAP HANA DB client.
        """
        return pulumi.get(self, "agree_to_install_hanadb_client")

    @property
    @pulumi.getter(name="hanaPort")
    def hana_port(self) -> str:
        """
        The HANA DB port.
        """
        return pulumi.get(self, "hana_port")

    @property
    @pulumi.getter(name="hanaSecretName")
    def hana_secret_name(self) -> str:
        """
        The secret name which manages the HANA DB credentials e.g. {
          "username": "<>",
          "password": "<>"
        }.
        """
        return pulumi.get(self, "hana_secret_name")

    @property
    @pulumi.getter
    def hanasid(self) -> str:
        """
        HANA DB SID.
        """
        return pulumi.get(self, "hanasid")

    @property
    @pulumi.getter(name="prometheusPort")
    def prometheus_port(self) -> Optional[str]:
        """
        Prometheus exporter port.
        """
        return pulumi.get(self, "prometheus_port")


@pulumi.output_type
class ApplicationJmxPrometheusExporter(dict):
    """
    The JMX Prometheus Exporter settings.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "hostPort":
            suggest = "host_port"
        elif key == "prometheusPort":
            suggest = "prometheus_port"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationJmxPrometheusExporter. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationJmxPrometheusExporter.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationJmxPrometheusExporter.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 host_port: Optional[str] = None,
                 jmxurl: Optional[str] = None,
                 prometheus_port: Optional[str] = None):
        """
        The JMX Prometheus Exporter settings.
        :param str host_port: Java agent host port
        :param str jmxurl: JMX service URL.
        :param str prometheus_port: Prometheus exporter port.
        """
        if host_port is not None:
            pulumi.set(__self__, "host_port", host_port)
        if jmxurl is not None:
            pulumi.set(__self__, "jmxurl", jmxurl)
        if prometheus_port is not None:
            pulumi.set(__self__, "prometheus_port", prometheus_port)

    @property
    @pulumi.getter(name="hostPort")
    def host_port(self) -> Optional[str]:
        """
        Java agent host port
        """
        return pulumi.get(self, "host_port")

    @property
    @pulumi.getter
    def jmxurl(self) -> Optional[str]:
        """
        JMX service URL.
        """
        return pulumi.get(self, "jmxurl")

    @property
    @pulumi.getter(name="prometheusPort")
    def prometheus_port(self) -> Optional[str]:
        """
        Prometheus exporter port.
        """
        return pulumi.get(self, "prometheus_port")


@pulumi.output_type
class ApplicationLog(dict):
    """
    A log to be monitored for the component.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "logType":
            suggest = "log_type"
        elif key == "logGroupName":
            suggest = "log_group_name"
        elif key == "logPath":
            suggest = "log_path"
        elif key == "patternSet":
            suggest = "pattern_set"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationLog. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationLog.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationLog.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 log_type: str,
                 encoding: Optional['ApplicationLogEncoding'] = None,
                 log_group_name: Optional[str] = None,
                 log_path: Optional[str] = None,
                 pattern_set: Optional[str] = None):
        """
        A log to be monitored for the component.
        :param str log_type: The log type decides the log patterns against which Application Insights analyzes the log.
        :param 'ApplicationLogEncoding' encoding: The type of encoding of the logs to be monitored.
        :param str log_group_name: The CloudWatch log group name to be associated to the monitored log.
        :param str log_path: The path of the logs to be monitored.
        :param str pattern_set: The name of the log pattern set.
        """
        pulumi.set(__self__, "log_type", log_type)
        if encoding is not None:
            pulumi.set(__self__, "encoding", encoding)
        if log_group_name is not None:
            pulumi.set(__self__, "log_group_name", log_group_name)
        if log_path is not None:
            pulumi.set(__self__, "log_path", log_path)
        if pattern_set is not None:
            pulumi.set(__self__, "pattern_set", pattern_set)

    @property
    @pulumi.getter(name="logType")
    def log_type(self) -> str:
        """
        The log type decides the log patterns against which Application Insights analyzes the log.
        """
        return pulumi.get(self, "log_type")

    @property
    @pulumi.getter
    def encoding(self) -> Optional['ApplicationLogEncoding']:
        """
        The type of encoding of the logs to be monitored.
        """
        return pulumi.get(self, "encoding")

    @property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[str]:
        """
        The CloudWatch log group name to be associated to the monitored log.
        """
        return pulumi.get(self, "log_group_name")

    @property
    @pulumi.getter(name="logPath")
    def log_path(self) -> Optional[str]:
        """
        The path of the logs to be monitored.
        """
        return pulumi.get(self, "log_path")

    @property
    @pulumi.getter(name="patternSet")
    def pattern_set(self) -> Optional[str]:
        """
        The name of the log pattern set.
        """
        return pulumi.get(self, "pattern_set")


@pulumi.output_type
class ApplicationLogPattern(dict):
    """
    The log pattern.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "patternName":
            suggest = "pattern_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationLogPattern. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationLogPattern.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationLogPattern.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 pattern: str,
                 pattern_name: str,
                 rank: int):
        """
        The log pattern.
        :param str pattern: The log pattern.
        :param str pattern_name: The name of the log pattern.
        :param int rank: Rank of the log pattern.
        """
        pulumi.set(__self__, "pattern", pattern)
        pulumi.set(__self__, "pattern_name", pattern_name)
        pulumi.set(__self__, "rank", rank)

    @property
    @pulumi.getter
    def pattern(self) -> str:
        """
        The log pattern.
        """
        return pulumi.get(self, "pattern")

    @property
    @pulumi.getter(name="patternName")
    def pattern_name(self) -> str:
        """
        The name of the log pattern.
        """
        return pulumi.get(self, "pattern_name")

    @property
    @pulumi.getter
    def rank(self) -> int:
        """
        Rank of the log pattern.
        """
        return pulumi.get(self, "rank")


@pulumi.output_type
class ApplicationLogPatternSet(dict):
    """
    The log pattern set.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "logPatterns":
            suggest = "log_patterns"
        elif key == "patternSetName":
            suggest = "pattern_set_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationLogPatternSet. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationLogPatternSet.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationLogPatternSet.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 log_patterns: Sequence['outputs.ApplicationLogPattern'],
                 pattern_set_name: str):
        """
        The log pattern set.
        :param Sequence['ApplicationLogPattern'] log_patterns: The log patterns of a set.
        :param str pattern_set_name: The name of the log pattern set.
        """
        pulumi.set(__self__, "log_patterns", log_patterns)
        pulumi.set(__self__, "pattern_set_name", pattern_set_name)

    @property
    @pulumi.getter(name="logPatterns")
    def log_patterns(self) -> Sequence['outputs.ApplicationLogPattern']:
        """
        The log patterns of a set.
        """
        return pulumi.get(self, "log_patterns")

    @property
    @pulumi.getter(name="patternSetName")
    def pattern_set_name(self) -> str:
        """
        The name of the log pattern set.
        """
        return pulumi.get(self, "pattern_set_name")


@pulumi.output_type
class ApplicationSubComponentConfigurationDetails(dict):
    """
    The configuration settings of sub components.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "alarmMetrics":
            suggest = "alarm_metrics"
        elif key == "windowsEvents":
            suggest = "windows_events"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationSubComponentConfigurationDetails. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationSubComponentConfigurationDetails.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationSubComponentConfigurationDetails.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 alarm_metrics: Optional[Sequence['outputs.ApplicationAlarmMetric']] = None,
                 logs: Optional[Sequence['outputs.ApplicationLog']] = None,
                 windows_events: Optional[Sequence['outputs.ApplicationWindowsEvent']] = None):
        """
        The configuration settings of sub components.
        :param Sequence['ApplicationAlarmMetric'] alarm_metrics: A list of metrics to monitor for the component.
        :param Sequence['ApplicationLog'] logs: A list of logs to monitor for the component.
        :param Sequence['ApplicationWindowsEvent'] windows_events: A list of Windows Events to log.
        """
        if alarm_metrics is not None:
            pulumi.set(__self__, "alarm_metrics", alarm_metrics)
        if logs is not None:
            pulumi.set(__self__, "logs", logs)
        if windows_events is not None:
            pulumi.set(__self__, "windows_events", windows_events)

    @property
    @pulumi.getter(name="alarmMetrics")
    def alarm_metrics(self) -> Optional[Sequence['outputs.ApplicationAlarmMetric']]:
        """
        A list of metrics to monitor for the component.
        """
        return pulumi.get(self, "alarm_metrics")

    @property
    @pulumi.getter
    def logs(self) -> Optional[Sequence['outputs.ApplicationLog']]:
        """
        A list of logs to monitor for the component.
        """
        return pulumi.get(self, "logs")

    @property
    @pulumi.getter(name="windowsEvents")
    def windows_events(self) -> Optional[Sequence['outputs.ApplicationWindowsEvent']]:
        """
        A list of Windows Events to log.
        """
        return pulumi.get(self, "windows_events")


@pulumi.output_type
class ApplicationSubComponentTypeConfiguration(dict):
    """
    One type sub component configurations for the component.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subComponentConfigurationDetails":
            suggest = "sub_component_configuration_details"
        elif key == "subComponentType":
            suggest = "sub_component_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationSubComponentTypeConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationSubComponentTypeConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationSubComponentTypeConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 sub_component_configuration_details: 'outputs.ApplicationSubComponentConfigurationDetails',
                 sub_component_type: 'ApplicationSubComponentTypeConfigurationSubComponentType'):
        """
        One type sub component configurations for the component.
        :param 'ApplicationSubComponentConfigurationDetails' sub_component_configuration_details: The configuration settings of sub components.
        :param 'ApplicationSubComponentTypeConfigurationSubComponentType' sub_component_type: The sub component type.
        """
        pulumi.set(__self__, "sub_component_configuration_details", sub_component_configuration_details)
        pulumi.set(__self__, "sub_component_type", sub_component_type)

    @property
    @pulumi.getter(name="subComponentConfigurationDetails")
    def sub_component_configuration_details(self) -> 'outputs.ApplicationSubComponentConfigurationDetails':
        """
        The configuration settings of sub components.
        """
        return pulumi.get(self, "sub_component_configuration_details")

    @property
    @pulumi.getter(name="subComponentType")
    def sub_component_type(self) -> 'ApplicationSubComponentTypeConfigurationSubComponentType':
        """
        The sub component type.
        """
        return pulumi.get(self, "sub_component_type")


@pulumi.output_type
class ApplicationWindowsEvent(dict):
    """
    A Windows Event to be monitored for the component.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "eventLevels":
            suggest = "event_levels"
        elif key == "eventName":
            suggest = "event_name"
        elif key == "logGroupName":
            suggest = "log_group_name"
        elif key == "patternSet":
            suggest = "pattern_set"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationWindowsEvent. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationWindowsEvent.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationWindowsEvent.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 event_levels: Sequence['ApplicationEventLevel'],
                 event_name: str,
                 log_group_name: str,
                 pattern_set: Optional[str] = None):
        """
        A Windows Event to be monitored for the component.
        :param Sequence['ApplicationEventLevel'] event_levels: The levels of event to log. 
        :param str event_name: The type of Windows Events to log.
        :param str log_group_name: The CloudWatch log group name to be associated to the monitored log.
        :param str pattern_set: The name of the log pattern set.
        """
        pulumi.set(__self__, "event_levels", event_levels)
        pulumi.set(__self__, "event_name", event_name)
        pulumi.set(__self__, "log_group_name", log_group_name)
        if pattern_set is not None:
            pulumi.set(__self__, "pattern_set", pattern_set)

    @property
    @pulumi.getter(name="eventLevels")
    def event_levels(self) -> Sequence['ApplicationEventLevel']:
        """
        The levels of event to log. 
        """
        return pulumi.get(self, "event_levels")

    @property
    @pulumi.getter(name="eventName")
    def event_name(self) -> str:
        """
        The type of Windows Events to log.
        """
        return pulumi.get(self, "event_name")

    @property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> str:
        """
        The CloudWatch log group name to be associated to the monitored log.
        """
        return pulumi.get(self, "log_group_name")

    @property
    @pulumi.getter(name="patternSet")
    def pattern_set(self) -> Optional[str]:
        """
        The name of the log pattern set.
        """
        return pulumi.get(self, "pattern_set")


