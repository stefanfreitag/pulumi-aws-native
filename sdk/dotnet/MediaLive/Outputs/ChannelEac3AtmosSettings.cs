// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaLive.Outputs
{

    [OutputType]
    public sealed class ChannelEac3AtmosSettings
    {
        public readonly double? Bitrate;
        public readonly string? CodingMode;
        public readonly int? Dialnorm;
        public readonly string? DrcLine;
        public readonly string? DrcRf;
        public readonly double? HeightTrim;
        public readonly double? SurroundTrim;

        [OutputConstructor]
        private ChannelEac3AtmosSettings(
            double? bitrate,

            string? codingMode,

            int? dialnorm,

            string? drcLine,

            string? drcRf,

            double? heightTrim,

            double? surroundTrim)
        {
            Bitrate = bitrate;
            CodingMode = codingMode;
            Dialnorm = dialnorm;
            DrcLine = drcLine;
            DrcRf = drcRf;
            HeightTrim = heightTrim;
            SurroundTrim = surroundTrim;
        }
    }
}
