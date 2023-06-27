// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2.Outputs
{

    /// <summary>
    /// Sends Verified Access logs to Kinesis.
    /// </summary>
    [OutputType]
    public sealed class VerifiedAccessInstanceVerifiedAccessLogsKinesisDataFirehoseProperties
    {
        /// <summary>
        /// The ID of the delivery stream.
        /// </summary>
        public readonly string? DeliveryStream;
        /// <summary>
        /// Indicates whether logging is enabled.
        /// </summary>
        public readonly bool? Enabled;

        [OutputConstructor]
        private VerifiedAccessInstanceVerifiedAccessLogsKinesisDataFirehoseProperties(
            string? deliveryStream,

            bool? enabled)
        {
            DeliveryStream = deliveryStream;
            Enabled = enabled;
        }
    }
}
