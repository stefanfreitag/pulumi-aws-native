// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.InternetMonitor
{
    public static class GetMonitor
    {
        /// <summary>
        /// Represents a monitor, which defines the monitoring boundaries for measurements that Internet Monitor publishes information about for an application
        /// </summary>
        public static Task<GetMonitorResult> InvokeAsync(GetMonitorArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetMonitorResult>("aws-native:internetmonitor:getMonitor", args ?? new GetMonitorArgs(), options.WithDefaults());

        /// <summary>
        /// Represents a monitor, which defines the monitoring boundaries for measurements that Internet Monitor publishes information about for an application
        /// </summary>
        public static Output<GetMonitorResult> Invoke(GetMonitorInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetMonitorResult>("aws-native:internetmonitor:getMonitor", args ?? new GetMonitorInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetMonitorArgs : global::Pulumi.InvokeArgs
    {
        [Input("monitorName", required: true)]
        public string MonitorName { get; set; } = null!;

        public GetMonitorArgs()
        {
        }
        public static new GetMonitorArgs Empty => new GetMonitorArgs();
    }

    public sealed class GetMonitorInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("monitorName", required: true)]
        public Input<string> MonitorName { get; set; } = null!;

        public GetMonitorInvokeArgs()
        {
        }
        public static new GetMonitorInvokeArgs Empty => new GetMonitorInvokeArgs();
    }


    [OutputType]
    public sealed class GetMonitorResult
    {
        public readonly string? CreatedAt;
        public readonly Outputs.MonitorHealthEventsConfig? HealthEventsConfig;
        public readonly Outputs.MonitorInternetMeasurementsLogDelivery? InternetMeasurementsLogDelivery;
        public readonly int? MaxCityNetworksToMonitor;
        public readonly string? ModifiedAt;
        public readonly string? MonitorArn;
        public readonly Pulumi.AwsNative.InternetMonitor.MonitorProcessingStatusCode? ProcessingStatus;
        public readonly string? ProcessingStatusInfo;
        public readonly ImmutableArray<string> Resources;
        public readonly Pulumi.AwsNative.InternetMonitor.MonitorConfigState? Status;
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;
        public readonly int? TrafficPercentageToMonitor;

        [OutputConstructor]
        private GetMonitorResult(
            string? createdAt,

            Outputs.MonitorHealthEventsConfig? healthEventsConfig,

            Outputs.MonitorInternetMeasurementsLogDelivery? internetMeasurementsLogDelivery,

            int? maxCityNetworksToMonitor,

            string? modifiedAt,

            string? monitorArn,

            Pulumi.AwsNative.InternetMonitor.MonitorProcessingStatusCode? processingStatus,

            string? processingStatusInfo,

            ImmutableArray<string> resources,

            Pulumi.AwsNative.InternetMonitor.MonitorConfigState? status,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags,

            int? trafficPercentageToMonitor)
        {
            CreatedAt = createdAt;
            HealthEventsConfig = healthEventsConfig;
            InternetMeasurementsLogDelivery = internetMeasurementsLogDelivery;
            MaxCityNetworksToMonitor = maxCityNetworksToMonitor;
            ModifiedAt = modifiedAt;
            MonitorArn = monitorArn;
            ProcessingStatus = processingStatus;
            ProcessingStatusInfo = processingStatusInfo;
            Resources = resources;
            Status = status;
            Tags = tags;
            TrafficPercentageToMonitor = trafficPercentageToMonitor;
        }
    }
}
