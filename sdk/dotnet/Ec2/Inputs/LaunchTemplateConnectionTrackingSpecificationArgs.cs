// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Inputs
{

    /// <summary>
    /// Allows customer to specify Connection Tracking options
    /// </summary>
    public sealed class LaunchTemplateConnectionTrackingSpecificationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Integer value for TCP Established Timeout
        /// </summary>
        [Input("tcpEstablishedTimeout")]
        public Input<int>? TcpEstablishedTimeout { get; set; }

        /// <summary>
        /// Integer value for UDP Stream Timeout
        /// </summary>
        [Input("udpStreamTimeout")]
        public Input<int>? UdpStreamTimeout { get; set; }

        /// <summary>
        /// Integer value for UDP Timeout
        /// </summary>
        [Input("udpTimeout")]
        public Input<int>? UdpTimeout { get; set; }

        public LaunchTemplateConnectionTrackingSpecificationArgs()
        {
        }
        public static new LaunchTemplateConnectionTrackingSpecificationArgs Empty => new LaunchTemplateConnectionTrackingSpecificationArgs();
    }
}
