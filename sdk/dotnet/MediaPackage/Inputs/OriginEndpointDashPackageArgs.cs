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
    public sealed class OriginEndpointDashPackageArgs : global::Pulumi.ResourceArgs
    {
        [Input("adTriggers")]
        private InputList<Pulumi.AwsNative.MediaPackage.OriginEndpointDashPackageAdTriggersItem>? _adTriggers;

        /// <summary>
        /// A list of SCTE-35 message types that are treated as ad markers in the output.  If empty, no ad markers are output.  Specify multiple items to create ad markers for all of the included message types.
        /// </summary>
        public InputList<Pulumi.AwsNative.MediaPackage.OriginEndpointDashPackageAdTriggersItem> AdTriggers
        {
            get => _adTriggers ?? (_adTriggers = new InputList<Pulumi.AwsNative.MediaPackage.OriginEndpointDashPackageAdTriggersItem>());
            set => _adTriggers = value;
        }

        [Input("adsOnDeliveryRestrictions")]
        public Input<Pulumi.AwsNative.MediaPackage.OriginEndpointAdsOnDeliveryRestrictions>? AdsOnDeliveryRestrictions { get; set; }

        [Input("encryption")]
        public Input<Inputs.OriginEndpointDashEncryptionArgs>? Encryption { get; set; }

        /// <summary>
        /// When enabled, an I-Frame only stream will be included in the output.
        /// </summary>
        [Input("includeIframeOnlyStream")]
        public Input<bool>? IncludeIframeOnlyStream { get; set; }

        /// <summary>
        /// Determines the position of some tags in the Media Presentation Description (MPD).  When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation.  When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.
        /// </summary>
        [Input("manifestLayout")]
        public Input<Pulumi.AwsNative.MediaPackage.OriginEndpointDashPackageManifestLayout>? ManifestLayout { get; set; }

        /// <summary>
        /// Time window (in seconds) contained in each manifest.
        /// </summary>
        [Input("manifestWindowSeconds")]
        public Input<int>? ManifestWindowSeconds { get; set; }

        /// <summary>
        /// Minimum duration (in seconds) that a player will buffer media before starting the presentation.
        /// </summary>
        [Input("minBufferTimeSeconds")]
        public Input<int>? MinBufferTimeSeconds { get; set; }

        /// <summary>
        /// Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).
        /// </summary>
        [Input("minUpdatePeriodSeconds")]
        public Input<int>? MinUpdatePeriodSeconds { get; set; }

        [Input("periodTriggers")]
        private InputList<Pulumi.AwsNative.MediaPackage.OriginEndpointDashPackagePeriodTriggersItem>? _periodTriggers;

        /// <summary>
        /// A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains "ADS", new periods will be created where the Channel source contains SCTE-35 ad markers.
        /// </summary>
        public InputList<Pulumi.AwsNative.MediaPackage.OriginEndpointDashPackagePeriodTriggersItem> PeriodTriggers
        {
            get => _periodTriggers ?? (_periodTriggers = new InputList<Pulumi.AwsNative.MediaPackage.OriginEndpointDashPackagePeriodTriggersItem>());
            set => _periodTriggers = value;
        }

        /// <summary>
        /// The Dynamic Adaptive Streaming over HTTP (DASH) profile type.  When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
        /// </summary>
        [Input("profile")]
        public Input<Pulumi.AwsNative.MediaPackage.OriginEndpointDashPackageProfile>? Profile { get; set; }

        /// <summary>
        /// Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
        /// </summary>
        [Input("segmentDurationSeconds")]
        public Input<int>? SegmentDurationSeconds { get; set; }

        /// <summary>
        /// Determines the type of SegmentTemplate included in the Media Presentation Description (MPD).  When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs.  When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.
        /// </summary>
        [Input("segmentTemplateFormat")]
        public Input<Pulumi.AwsNative.MediaPackage.OriginEndpointDashPackageSegmentTemplateFormat>? SegmentTemplateFormat { get; set; }

        [Input("streamSelection")]
        public Input<Inputs.OriginEndpointStreamSelectionArgs>? StreamSelection { get; set; }

        /// <summary>
        /// Duration (in seconds) to delay live content before presentation.
        /// </summary>
        [Input("suggestedPresentationDelaySeconds")]
        public Input<int>? SuggestedPresentationDelaySeconds { get; set; }

        /// <summary>
        /// Determines the type of UTCTiming included in the Media Presentation Description (MPD)
        /// </summary>
        [Input("utcTiming")]
        public Input<Pulumi.AwsNative.MediaPackage.OriginEndpointDashPackageUtcTiming>? UtcTiming { get; set; }

        /// <summary>
        /// Specifies the value attribute of the UTCTiming field when utcTiming is set to HTTP-ISO, HTTP-HEAD or HTTP-XSDATE
        /// </summary>
        [Input("utcTimingUri")]
        public Input<string>? UtcTimingUri { get; set; }

        public OriginEndpointDashPackageArgs()
        {
        }
        public static new OriginEndpointDashPackageArgs Empty => new OriginEndpointDashPackageArgs();
    }
}
