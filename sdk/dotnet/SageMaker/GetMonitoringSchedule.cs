// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker
{
    public static class GetMonitoringSchedule
    {
        /// <summary>
        /// Resource Type definition for AWS::SageMaker::MonitoringSchedule
        /// </summary>
        public static Task<GetMonitoringScheduleResult> InvokeAsync(GetMonitoringScheduleArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetMonitoringScheduleResult>("aws-native:sagemaker:getMonitoringSchedule", args ?? new GetMonitoringScheduleArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::SageMaker::MonitoringSchedule
        /// </summary>
        public static Output<GetMonitoringScheduleResult> Invoke(GetMonitoringScheduleInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetMonitoringScheduleResult>("aws-native:sagemaker:getMonitoringSchedule", args ?? new GetMonitoringScheduleInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetMonitoringScheduleArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the monitoring schedule.
        /// </summary>
        [Input("monitoringScheduleArn", required: true)]
        public string MonitoringScheduleArn { get; set; } = null!;

        public GetMonitoringScheduleArgs()
        {
        }
        public static new GetMonitoringScheduleArgs Empty => new GetMonitoringScheduleArgs();
    }

    public sealed class GetMonitoringScheduleInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the monitoring schedule.
        /// </summary>
        [Input("monitoringScheduleArn", required: true)]
        public Input<string> MonitoringScheduleArn { get; set; } = null!;

        public GetMonitoringScheduleInvokeArgs()
        {
        }
        public static new GetMonitoringScheduleInvokeArgs Empty => new GetMonitoringScheduleInvokeArgs();
    }


    [OutputType]
    public sealed class GetMonitoringScheduleResult
    {
        /// <summary>
        /// The time at which the schedule was created.
        /// </summary>
        public readonly string? CreationTime;
        public readonly string? EndpointName;
        /// <summary>
        /// Contains the reason a monitoring job failed, if it failed.
        /// </summary>
        public readonly string? FailureReason;
        /// <summary>
        /// A timestamp that indicates the last time the monitoring job was modified.
        /// </summary>
        public readonly string? LastModifiedTime;
        /// <summary>
        /// Describes metadata on the last execution to run, if there was one.
        /// </summary>
        public readonly Outputs.MonitoringScheduleMonitoringExecutionSummary? LastMonitoringExecutionSummary;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the monitoring schedule.
        /// </summary>
        public readonly string? MonitoringScheduleArn;
        public readonly Outputs.MonitoringScheduleConfig? MonitoringScheduleConfig;
        /// <summary>
        /// The status of a schedule job.
        /// </summary>
        public readonly Pulumi.AwsNative.SageMaker.MonitoringScheduleStatus? MonitoringScheduleStatus;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.MonitoringScheduleTag> Tags;

        [OutputConstructor]
        private GetMonitoringScheduleResult(
            string? creationTime,

            string? endpointName,

            string? failureReason,

            string? lastModifiedTime,

            Outputs.MonitoringScheduleMonitoringExecutionSummary? lastMonitoringExecutionSummary,

            string? monitoringScheduleArn,

            Outputs.MonitoringScheduleConfig? monitoringScheduleConfig,

            Pulumi.AwsNative.SageMaker.MonitoringScheduleStatus? monitoringScheduleStatus,

            ImmutableArray<Outputs.MonitoringScheduleTag> tags)
        {
            CreationTime = creationTime;
            EndpointName = endpointName;
            FailureReason = failureReason;
            LastModifiedTime = lastModifiedTime;
            LastMonitoringExecutionSummary = lastMonitoringExecutionSummary;
            MonitoringScheduleArn = monitoringScheduleArn;
            MonitoringScheduleConfig = monitoringScheduleConfig;
            MonitoringScheduleStatus = monitoringScheduleStatus;
            Tags = tags;
        }
    }
}
