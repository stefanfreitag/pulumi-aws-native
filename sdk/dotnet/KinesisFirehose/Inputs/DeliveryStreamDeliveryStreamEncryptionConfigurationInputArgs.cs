// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisFirehose.Inputs
{

    public sealed class DeliveryStreamDeliveryStreamEncryptionConfigurationInputArgs : Pulumi.ResourceArgs
    {
        [Input("keyARN")]
        public Input<string>? KeyARN { get; set; }

        [Input("keyType", required: true)]
        public Input<Pulumi.AwsNative.KinesisFirehose.DeliveryStreamDeliveryStreamEncryptionConfigurationInputKeyType> KeyType { get; set; } = null!;

        public DeliveryStreamDeliveryStreamEncryptionConfigurationInputArgs()
        {
        }
    }
}
