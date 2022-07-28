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
    /// The asset property's definition, alias, and notification state.
    /// </summary>
    public sealed class AssetPropertyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The property alias that identifies the property.
        /// </summary>
        [Input("alias")]
        public Input<string>? Alias { get; set; }

        /// <summary>
        /// Customer provided ID for property.
        /// </summary>
        [Input("logicalId", required: true)]
        public Input<string> LogicalId { get; set; } = null!;

        /// <summary>
        /// The MQTT notification state (ENABLED or DISABLED) for this asset property.
        /// </summary>
        [Input("notificationState")]
        public Input<Pulumi.AwsNative.IoTSiteWise.AssetPropertyNotificationState>? NotificationState { get; set; }

        public AssetPropertyArgs()
        {
        }
        public static new AssetPropertyArgs Empty => new AssetPropertyArgs();
    }
}
