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
    /// The output of the bridge.
    /// </summary>
    public sealed class BridgeOutputArgs : global::Pulumi.ResourceArgs
    {
        [Input("networkOutput")]
        public Input<Inputs.BridgeNetworkOutputArgs>? NetworkOutput { get; set; }

        public BridgeOutputArgs()
        {
        }
        public static new BridgeOutputArgs Empty => new BridgeOutputArgs();
    }
}
