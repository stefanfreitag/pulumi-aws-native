// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTSiteWise.Inputs
{

    /// <summary>
    /// Contains a tumbling window, which is a repeating fixed-sized, non-overlapping, and contiguous time interval. This window is used in metric and aggregation computations.
    /// </summary>
    public sealed class AssetModelTumblingWindowArgs : global::Pulumi.ResourceArgs
    {
        [Input("interval", required: true)]
        public Input<string> Interval { get; set; } = null!;

        [Input("offset")]
        public Input<string>? Offset { get; set; }

        public AssetModelTumblingWindowArgs()
        {
        }
        public static new AssetModelTumblingWindowArgs Empty => new AssetModelTumblingWindowArgs();
    }
}
