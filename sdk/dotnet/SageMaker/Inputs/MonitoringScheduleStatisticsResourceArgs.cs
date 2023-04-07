// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    /// <summary>
    /// The baseline statistics resource for a monitoring job.
    /// </summary>
    public sealed class MonitoringScheduleStatisticsResourceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Amazon S3 URI for the baseline statistics file in Amazon S3 that the current monitoring job should be validated against.
        /// </summary>
        [Input("s3Uri")]
        public Input<string>? S3Uri { get; set; }

        public MonitoringScheduleStatisticsResourceArgs()
        {
        }
        public static new MonitoringScheduleStatisticsResourceArgs Empty => new MonitoringScheduleStatisticsResourceArgs();
    }
}
