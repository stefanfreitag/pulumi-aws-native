// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaPackage.Inputs
{

    /// <summary>
    /// A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    /// </summary>
    public sealed class PackagingConfigurationDashPackageArgs : Pulumi.ResourceArgs
    {
        [Input("dashManifests", required: true)]
        private InputList<Inputs.PackagingConfigurationDashManifestArgs>? _dashManifests;

        /// <summary>
        /// A list of DASH manifest configurations.
        /// </summary>
        public InputList<Inputs.PackagingConfigurationDashManifestArgs> DashManifests
        {
            get => _dashManifests ?? (_dashManifests = new InputList<Inputs.PackagingConfigurationDashManifestArgs>());
            set => _dashManifests = value;
        }

        [Input("encryption")]
        public Input<Inputs.PackagingConfigurationDashEncryptionArgs>? Encryption { get; set; }

        /// <summary>
        /// When includeEncoderConfigurationInSegments is set to true, MediaPackage places your encoder's Sequence Parameter Set (SPS), Picture Parameter Set (PPS), and Video Parameter Set (VPS) metadata in every video segment instead of in the init fragment. This lets you use different SPS/PPS/VPS settings for your assets during content playback.
        /// </summary>
        [Input("includeEncoderConfigurationInSegments")]
        public Input<bool>? IncludeEncoderConfigurationInSegments { get; set; }

        [Input("periodTriggers")]
        private InputList<string>? _periodTriggers;

        /// <summary>
        /// A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains "ADS", new periods will be created where the Asset contains SCTE-35 ad markers.
        /// </summary>
        public InputList<string> PeriodTriggers
        {
            get => _periodTriggers ?? (_periodTriggers = new InputList<string>());
            set => _periodTriggers = value;
        }

        [Input("segmentDurationSeconds")]
        public Input<int>? SegmentDurationSeconds { get; set; }

        /// <summary>
        /// Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.
        /// </summary>
        [Input("segmentTemplateFormat")]
        public Input<Pulumi.AwsNative.MediaPackage.PackagingConfigurationDashPackageSegmentTemplateFormat>? SegmentTemplateFormat { get; set; }

        public PackagingConfigurationDashPackageArgs()
        {
        }
    }
}
