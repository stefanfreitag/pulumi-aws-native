// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElastiCache.Inputs
{

    public sealed class ReplicationGroupDestinationDetailsArgs : global::Pulumi.ResourceArgs
    {
        [Input("cloudWatchLogsDetails")]
        public Input<Inputs.ReplicationGroupCloudWatchLogsDestinationDetailsArgs>? CloudWatchLogsDetails { get; set; }

        [Input("kinesisFirehoseDetails")]
        public Input<Inputs.ReplicationGroupKinesisFirehoseDestinationDetailsArgs>? KinesisFirehoseDetails { get; set; }

        public ReplicationGroupDestinationDetailsArgs()
        {
        }
        public static new ReplicationGroupDestinationDetailsArgs Empty => new ReplicationGroupDestinationDetailsArgs();
    }
}
