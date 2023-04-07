// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaLive.Inputs
{

    public sealed class ChannelH264SettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("adaptiveQuantization")]
        public Input<string>? AdaptiveQuantization { get; set; }

        [Input("afdSignaling")]
        public Input<string>? AfdSignaling { get; set; }

        [Input("bitrate")]
        public Input<int>? Bitrate { get; set; }

        [Input("bufFillPct")]
        public Input<int>? BufFillPct { get; set; }

        [Input("bufSize")]
        public Input<int>? BufSize { get; set; }

        [Input("colorMetadata")]
        public Input<string>? ColorMetadata { get; set; }

        [Input("colorSpaceSettings")]
        public Input<Inputs.ChannelH264ColorSpaceSettingsArgs>? ColorSpaceSettings { get; set; }

        [Input("entropyEncoding")]
        public Input<string>? EntropyEncoding { get; set; }

        [Input("filterSettings")]
        public Input<Inputs.ChannelH264FilterSettingsArgs>? FilterSettings { get; set; }

        [Input("fixedAfd")]
        public Input<string>? FixedAfd { get; set; }

        [Input("flickerAq")]
        public Input<string>? FlickerAq { get; set; }

        [Input("forceFieldPictures")]
        public Input<string>? ForceFieldPictures { get; set; }

        [Input("framerateControl")]
        public Input<string>? FramerateControl { get; set; }

        [Input("framerateDenominator")]
        public Input<int>? FramerateDenominator { get; set; }

        [Input("framerateNumerator")]
        public Input<int>? FramerateNumerator { get; set; }

        [Input("gopBReference")]
        public Input<string>? GopBReference { get; set; }

        [Input("gopClosedCadence")]
        public Input<int>? GopClosedCadence { get; set; }

        [Input("gopNumBFrames")]
        public Input<int>? GopNumBFrames { get; set; }

        [Input("gopSize")]
        public Input<double>? GopSize { get; set; }

        [Input("gopSizeUnits")]
        public Input<string>? GopSizeUnits { get; set; }

        [Input("level")]
        public Input<string>? Level { get; set; }

        [Input("lookAheadRateControl")]
        public Input<string>? LookAheadRateControl { get; set; }

        [Input("maxBitrate")]
        public Input<int>? MaxBitrate { get; set; }

        [Input("minIInterval")]
        public Input<int>? MinIInterval { get; set; }

        [Input("numRefFrames")]
        public Input<int>? NumRefFrames { get; set; }

        [Input("parControl")]
        public Input<string>? ParControl { get; set; }

        [Input("parDenominator")]
        public Input<int>? ParDenominator { get; set; }

        [Input("parNumerator")]
        public Input<int>? ParNumerator { get; set; }

        [Input("profile")]
        public Input<string>? Profile { get; set; }

        [Input("qualityLevel")]
        public Input<string>? QualityLevel { get; set; }

        [Input("qvbrQualityLevel")]
        public Input<int>? QvbrQualityLevel { get; set; }

        [Input("rateControlMode")]
        public Input<string>? RateControlMode { get; set; }

        [Input("scanType")]
        public Input<string>? ScanType { get; set; }

        [Input("sceneChangeDetect")]
        public Input<string>? SceneChangeDetect { get; set; }

        [Input("slices")]
        public Input<int>? Slices { get; set; }

        [Input("softness")]
        public Input<int>? Softness { get; set; }

        [Input("spatialAq")]
        public Input<string>? SpatialAq { get; set; }

        [Input("subgopLength")]
        public Input<string>? SubgopLength { get; set; }

        [Input("syntax")]
        public Input<string>? Syntax { get; set; }

        [Input("temporalAq")]
        public Input<string>? TemporalAq { get; set; }

        [Input("timecodeInsertion")]
        public Input<string>? TimecodeInsertion { get; set; }

        public ChannelH264SettingsArgs()
        {
        }
        public static new ChannelH264SettingsArgs Empty => new ChannelH264SettingsArgs();
    }
}
