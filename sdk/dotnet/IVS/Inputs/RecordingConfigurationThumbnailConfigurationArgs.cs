// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IVS.Inputs
{

    /// <summary>
    /// Recording Thumbnail Configuration.
    /// </summary>
    public sealed class RecordingConfigurationThumbnailConfigurationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Thumbnail Recording Mode, which determines whether thumbnails are recorded at an interval or are disabled.
        /// </summary>
        [Input("recordingMode", required: true)]
        public Input<Pulumi.AwsNative.IVS.RecordingConfigurationThumbnailConfigurationRecordingMode> RecordingMode { get; set; } = null!;

        /// <summary>
        /// Thumbnail recording Target Interval Seconds defines the interval at which thumbnails are recorded. This field is required if RecordingMode is INTERVAL.
        /// </summary>
        [Input("targetIntervalSeconds")]
        public Input<int>? TargetIntervalSeconds { get; set; }

        public RecordingConfigurationThumbnailConfigurationArgs()
        {
        }
        public static new RecordingConfigurationThumbnailConfigurationArgs Empty => new RecordingConfigurationThumbnailConfigurationArgs();
    }
}
