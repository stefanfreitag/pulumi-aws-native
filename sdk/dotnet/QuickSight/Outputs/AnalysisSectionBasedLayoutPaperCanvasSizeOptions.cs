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
    public sealed class AnalysisSectionBasedLayoutPaperCanvasSizeOptions
    {
        public readonly Outputs.AnalysisSpacing? PaperMargin;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisPaperOrientation? PaperOrientation;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisPaperSize? PaperSize;

        [OutputConstructor]
        private AnalysisSectionBasedLayoutPaperCanvasSizeOptions(
            Outputs.AnalysisSpacing? paperMargin,

            Pulumi.AwsNative.QuickSight.AnalysisPaperOrientation? paperOrientation,

            Pulumi.AwsNative.QuickSight.AnalysisPaperSize? paperSize)
        {
            PaperMargin = paperMargin;
            PaperOrientation = paperOrientation;
            PaperSize = paperSize;
        }
    }
}
