// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisFirehose.Inputs
{

    public sealed class DeliveryStreamSplunkRetryOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("durationInSeconds")]
        public Input<int>? DurationInSeconds { get; set; }

        public DeliveryStreamSplunkRetryOptionsArgs()
        {
        }
        public static new DeliveryStreamSplunkRetryOptionsArgs Empty => new DeliveryStreamSplunkRetryOptionsArgs();
    }
}
