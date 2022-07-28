// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTEvents.Inputs
{

    /// <summary>
    /// A structure that contains value information. For more information, see [AssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetPropertyValue.html) in the *AWS IoT SiteWise API Reference*.
    /// </summary>
    public sealed class AlarmModelAssetPropertyValueArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The quality of the asset property value. The value must be `GOOD`, `BAD`, or `UNCERTAIN`. You can also specify an expression.
        /// </summary>
        [Input("quality")]
        public Input<string>? Quality { get; set; }

        [Input("timestamp")]
        public Input<Inputs.AlarmModelAssetPropertyTimestampArgs>? Timestamp { get; set; }

        [Input("value", required: true)]
        public Input<Inputs.AlarmModelAssetPropertyVariantArgs> Value { get; set; } = null!;

        public AlarmModelAssetPropertyValueArgs()
        {
        }
        public static new AlarmModelAssetPropertyValueArgs Empty => new AlarmModelAssetPropertyValueArgs();
    }
}
