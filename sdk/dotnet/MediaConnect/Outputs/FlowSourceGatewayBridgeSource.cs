// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaConnect.Outputs
{

    /// <summary>
    /// The source configuration for cloud flows receiving a stream from a bridge.
    /// </summary>
    [OutputType]
    public sealed class FlowSourceGatewayBridgeSource
    {
        /// <summary>
        /// The ARN of the bridge feeding this flow.
        /// </summary>
        public readonly string BridgeArn;
        /// <summary>
        /// The name of the VPC interface attachment to use for this bridge source.
        /// </summary>
        public readonly Outputs.FlowSourceVpcInterfaceAttachment? VpcInterfaceAttachment;

        [OutputConstructor]
        private FlowSourceGatewayBridgeSource(
            string bridgeArn,

            Outputs.FlowSourceVpcInterfaceAttachment? vpcInterfaceAttachment)
        {
            BridgeArn = bridgeArn;
            VpcInterfaceAttachment = vpcInterfaceAttachment;
        }
    }
}
