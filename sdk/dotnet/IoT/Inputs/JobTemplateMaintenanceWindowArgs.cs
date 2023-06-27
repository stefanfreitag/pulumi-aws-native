// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT.Inputs
{

    /// <summary>
    /// Specifies a start time and duration for a scheduled Job.
    /// </summary>
    public sealed class JobTemplateMaintenanceWindowArgs : global::Pulumi.ResourceArgs
    {
        [Input("durationInMinutes")]
        public Input<int>? DurationInMinutes { get; set; }

        [Input("startTime")]
        public Input<string>? StartTime { get; set; }

        public JobTemplateMaintenanceWindowArgs()
        {
        }
        public static new JobTemplateMaintenanceWindowArgs Empty => new JobTemplateMaintenanceWindowArgs();
    }
}
