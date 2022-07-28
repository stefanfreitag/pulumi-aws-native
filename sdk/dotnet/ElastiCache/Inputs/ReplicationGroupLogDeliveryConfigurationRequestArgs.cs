// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElastiCache.Inputs
{

    public sealed class ReplicationGroupLogDeliveryConfigurationRequestArgs : global::Pulumi.ResourceArgs
    {
        [Input("destinationDetails", required: true)]
        public Input<Inputs.ReplicationGroupDestinationDetailsArgs> DestinationDetails { get; set; } = null!;

        [Input("destinationType", required: true)]
        public Input<string> DestinationType { get; set; } = null!;

        [Input("logFormat", required: true)]
        public Input<string> LogFormat { get; set; } = null!;

        [Input("logType", required: true)]
        public Input<string> LogType { get; set; } = null!;

        public ReplicationGroupLogDeliveryConfigurationRequestArgs()
        {
        }
        public static new ReplicationGroupLogDeliveryConfigurationRequestArgs Empty => new ReplicationGroupLogDeliveryConfigurationRequestArgs();
    }
}
