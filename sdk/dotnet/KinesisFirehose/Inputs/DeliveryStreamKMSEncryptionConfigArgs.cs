// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisFirehose.Inputs
{

    public sealed class DeliveryStreamKMSEncryptionConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("aWSKMSKeyARN", required: true)]
        public Input<string> AWSKMSKeyARN { get; set; } = null!;

        public DeliveryStreamKMSEncryptionConfigArgs()
        {
        }
        public static new DeliveryStreamKMSEncryptionConfigArgs Empty => new DeliveryStreamKMSEncryptionConfigArgs();
    }
}
