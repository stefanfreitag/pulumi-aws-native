// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Outputs
{

    /// <summary>
    /// Summary of information about monitoring job
    /// </summary>
    [OutputType]
    public sealed class MonitoringScheduleMonitoringExecutionSummary
    {
        /// <summary>
        /// The time at which the monitoring job was created.
        /// </summary>
        public readonly string CreationTime;
        public readonly string? EndpointName;
        /// <summary>
        /// Contains the reason a monitoring job failed, if it failed.
        /// </summary>
        public readonly string? FailureReason;
        /// <summary>
        /// A timestamp that indicates the last time the monitoring job was modified.
        /// </summary>
        public readonly string LastModifiedTime;
        /// <summary>
        /// The status of the monitoring job.
        /// </summary>
        public readonly Pulumi.AwsNative.SageMaker.MonitoringScheduleMonitoringExecutionSummaryMonitoringExecutionStatus MonitoringExecutionStatus;
        public readonly string MonitoringScheduleName;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the monitoring job.
        /// </summary>
        public readonly string? ProcessingJobArn;
        /// <summary>
        /// The time the monitoring job was scheduled.
        /// </summary>
        public readonly string ScheduledTime;

        [OutputConstructor]
        private MonitoringScheduleMonitoringExecutionSummary(
            string creationTime,

            string? endpointName,

            string? failureReason,

            string lastModifiedTime,

            Pulumi.AwsNative.SageMaker.MonitoringScheduleMonitoringExecutionSummaryMonitoringExecutionStatus monitoringExecutionStatus,

            string monitoringScheduleName,

            string? processingJobArn,

            string scheduledTime)
        {
            CreationTime = creationTime;
            EndpointName = endpointName;
            FailureReason = failureReason;
            LastModifiedTime = lastModifiedTime;
            MonitoringExecutionStatus = monitoringExecutionStatus;
            MonitoringScheduleName = monitoringScheduleName;
            ProcessingJobArn = processingJobArn;
            ScheduledTime = scheduledTime;
        }
    }
}
