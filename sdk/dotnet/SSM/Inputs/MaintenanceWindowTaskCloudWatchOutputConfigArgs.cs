// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SSM.Inputs
{

    public sealed class MaintenanceWindowTaskCloudWatchOutputConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("cloudWatchLogGroupName")]
        public Input<string>? CloudWatchLogGroupName { get; set; }

        [Input("cloudWatchOutputEnabled")]
        public Input<bool>? CloudWatchOutputEnabled { get; set; }

        public MaintenanceWindowTaskCloudWatchOutputConfigArgs()
        {
        }
        public static new MaintenanceWindowTaskCloudWatchOutputConfigArgs Empty => new MaintenanceWindowTaskCloudWatchOutputConfigArgs();
    }
}
