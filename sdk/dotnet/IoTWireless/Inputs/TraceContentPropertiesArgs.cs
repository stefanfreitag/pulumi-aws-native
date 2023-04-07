// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTWireless.Inputs
{

    /// <summary>
    /// Trace content for your wireless gateway and wireless device resources
    /// </summary>
    public sealed class TraceContentPropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("logLevel")]
        public Input<Pulumi.AwsNative.IoTWireless.NetworkAnalyzerConfigurationLogLevel>? LogLevel { get; set; }

        [Input("wirelessDeviceFrameInfo")]
        public Input<Pulumi.AwsNative.IoTWireless.NetworkAnalyzerConfigurationWirelessDeviceFrameInfo>? WirelessDeviceFrameInfo { get; set; }

        public TraceContentPropertiesArgs()
        {
        }
        public static new TraceContentPropertiesArgs Empty => new TraceContentPropertiesArgs();
    }
}
