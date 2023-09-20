// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaPackageV2.Inputs
{

    /// <summary>
    /// &lt;p&gt;The segment configuration, including the segment name, duration, and other configuration values.&lt;/p&gt;
    /// </summary>
    public sealed class OriginEndpointSegmentArgs : global::Pulumi.ResourceArgs
    {
        [Input("encryption")]
        public Input<Inputs.OriginEndpointEncryptionArgs>? Encryption { get; set; }

        /// <summary>
        /// &lt;p&gt;When selected, the stream set includes an additional I-frame only stream, along with the other tracks. If false, this extra stream is not included. MediaPackage generates an I-frame only stream from the first rendition in the manifest. The service inserts EXT-I-FRAMES-ONLY tags in the output manifest, and then generates and includes an I-frames only playlist in the stream. This playlist permits player functionality like fast forward and rewind.&lt;/p&gt;
        /// </summary>
        [Input("includeIframeOnlyStreams")]
        public Input<bool>? IncludeIframeOnlyStreams { get; set; }

        [Input("scte")]
        public Input<Inputs.OriginEndpointScteArgs>? Scte { get; set; }

        /// <summary>
        /// &lt;p&gt;The duration (in seconds) of each segment. Enter a value equal to, or a multiple of, the input segment duration. If the value that you enter is different from the input segment duration, MediaPackage rounds segments to the nearest multiple of the input segment duration.&lt;/p&gt;
        /// </summary>
        [Input("segmentDurationSeconds")]
        public Input<int>? SegmentDurationSeconds { get; set; }

        /// <summary>
        /// &lt;p&gt;The name that describes the segment. The name is the base name of the segment used in all content manifests inside of the endpoint. You can't use spaces in the name.&lt;/p&gt;
        /// </summary>
        [Input("segmentName")]
        public Input<string>? SegmentName { get; set; }

        /// <summary>
        /// &lt;p&gt;By default, MediaPackage excludes all digital video broadcasting (DVB) subtitles from the output. When selected, MediaPackage passes through DVB subtitles into the output.&lt;/p&gt;
        /// </summary>
        [Input("tsIncludeDvbSubtitles")]
        public Input<bool>? TsIncludeDvbSubtitles { get; set; }

        /// <summary>
        /// &lt;p&gt;When selected, MediaPackage bundles all audio tracks in a rendition group. All other tracks in the stream can be used with any audio rendition from the group.&lt;/p&gt;
        /// </summary>
        [Input("tsUseAudioRenditionGroup")]
        public Input<bool>? TsUseAudioRenditionGroup { get; set; }

        public OriginEndpointSegmentArgs()
        {
        }
        public static new OriginEndpointSegmentArgs Empty => new OriginEndpointSegmentArgs();
    }
}
