// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class AnalysisArcAxisConfiguration
    {
        public readonly Outputs.AnalysisArcAxisDisplayRange? Range;
        public readonly double? ReserveRange;

        [OutputConstructor]
        private AnalysisArcAxisConfiguration(
            Outputs.AnalysisArcAxisDisplayRange? range,

            double? reserveRange)
        {
            Range = range;
            ReserveRange = reserveRange;
        }
    }
}
