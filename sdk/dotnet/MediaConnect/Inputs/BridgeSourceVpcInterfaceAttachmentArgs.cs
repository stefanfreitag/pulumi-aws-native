// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaConnect.Inputs
{

    /// <summary>
    /// The settings for attaching a VPC interface to an resource.
    /// </summary>
    public sealed class BridgeSourceVpcInterfaceAttachmentArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the VPC interface to use for this resource.
        /// </summary>
        [Input("vpcInterfaceName")]
        public Input<string>? VpcInterfaceName { get; set; }

        public BridgeSourceVpcInterfaceAttachmentArgs()
        {
        }
        public static new BridgeSourceVpcInterfaceAttachmentArgs Empty => new BridgeSourceVpcInterfaceAttachmentArgs();
    }
}
