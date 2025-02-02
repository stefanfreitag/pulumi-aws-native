// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AmazonMq.Inputs
{

    public sealed class BrokerEncryptionOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        [Input("useAwsOwnedKey", required: true)]
        public Input<bool> UseAwsOwnedKey { get; set; } = null!;

        public BrokerEncryptionOptionsArgs()
        {
        }
        public static new BrokerEncryptionOptionsArgs Empty => new BrokerEncryptionOptionsArgs();
    }
}
