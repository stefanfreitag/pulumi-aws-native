// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaTailor.Inputs
{

    /// <summary>
    /// &lt;p&gt;HLS playlist configuration parameters.&lt;/p&gt;
    /// </summary>
    public sealed class ChannelHlsPlaylistSettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("adMarkupType")]
        private InputList<Pulumi.AwsNative.MediaTailor.ChannelAdMarkupType>? _adMarkupType;

        /// <summary>
        /// &lt;p&gt;Determines the type of SCTE 35 tags to use in ad markup. Specify &lt;code&gt;DATERANGE&lt;/code&gt; to use &lt;code&gt;DATERANGE&lt;/code&gt; tags (for live or VOD content). Specify &lt;code&gt;SCTE35_ENHANCED&lt;/code&gt; to use &lt;code&gt;EXT-X-CUE-OUT&lt;/code&gt; and &lt;code&gt;EXT-X-CUE-IN&lt;/code&gt; tags (for VOD content only).&lt;/p&gt;
        /// </summary>
        public InputList<Pulumi.AwsNative.MediaTailor.ChannelAdMarkupType> AdMarkupType
        {
            get => _adMarkupType ?? (_adMarkupType = new InputList<Pulumi.AwsNative.MediaTailor.ChannelAdMarkupType>());
            set => _adMarkupType = value;
        }

        /// <summary>
        /// &lt;p&gt;The total duration (in seconds) of each manifest. Minimum value: &lt;code&gt;30&lt;/code&gt; seconds. Maximum value: &lt;code&gt;3600&lt;/code&gt; seconds.&lt;/p&gt;
        /// </summary>
        [Input("manifestWindowSeconds")]
        public Input<double>? ManifestWindowSeconds { get; set; }

        public ChannelHlsPlaylistSettingsArgs()
        {
        }
        public static new ChannelHlsPlaylistSettingsArgs Empty => new ChannelHlsPlaylistSettingsArgs();
    }
}
