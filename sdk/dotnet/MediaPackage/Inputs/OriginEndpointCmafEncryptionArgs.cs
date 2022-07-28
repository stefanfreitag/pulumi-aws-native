// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaPackage.Inputs
{

    /// <summary>
    /// A Common Media Application Format (CMAF) encryption configuration.
    /// </summary>
    public sealed class OriginEndpointCmafEncryptionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// An optional 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting blocks. If you don't specify a value, then MediaPackage creates the constant initialization vector (IV).
        /// </summary>
        [Input("constantInitializationVector")]
        public Input<string>? ConstantInitializationVector { get; set; }

        /// <summary>
        /// Time (in seconds) between each encryption key rotation.
        /// </summary>
        [Input("keyRotationIntervalSeconds")]
        public Input<int>? KeyRotationIntervalSeconds { get; set; }

        [Input("spekeKeyProvider", required: true)]
        public Input<Inputs.OriginEndpointSpekeKeyProviderArgs> SpekeKeyProvider { get; set; } = null!;

        public OriginEndpointCmafEncryptionArgs()
        {
        }
        public static new OriginEndpointCmafEncryptionArgs Empty => new OriginEndpointCmafEncryptionArgs();
    }
}
