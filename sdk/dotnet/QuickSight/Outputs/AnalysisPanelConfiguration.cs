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
    public sealed class AnalysisPanelConfiguration
    {
        public readonly string? BackgroundColor;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisVisibility? BackgroundVisibility;
        public readonly string? BorderColor;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisPanelBorderStyle? BorderStyle;
        /// <summary>
        /// String based length that is composed of value and unit in px
        /// </summary>
        public readonly string? BorderThickness;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisVisibility? BorderVisibility;
        /// <summary>
        /// String based length that is composed of value and unit in px
        /// </summary>
        public readonly string? GutterSpacing;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisVisibility? GutterVisibility;
        public readonly Outputs.AnalysisPanelTitleOptions? Title;

        [OutputConstructor]
        private AnalysisPanelConfiguration(
            string? backgroundColor,

            Pulumi.AwsNative.QuickSight.AnalysisVisibility? backgroundVisibility,

            string? borderColor,

            Pulumi.AwsNative.QuickSight.AnalysisPanelBorderStyle? borderStyle,

            string? borderThickness,

            Pulumi.AwsNative.QuickSight.AnalysisVisibility? borderVisibility,

            string? gutterSpacing,

            Pulumi.AwsNative.QuickSight.AnalysisVisibility? gutterVisibility,

            Outputs.AnalysisPanelTitleOptions? title)
        {
            BackgroundColor = backgroundColor;
            BackgroundVisibility = backgroundVisibility;
            BorderColor = borderColor;
            BorderStyle = borderStyle;
            BorderThickness = borderThickness;
            BorderVisibility = borderVisibility;
            GutterSpacing = gutterSpacing;
            GutterVisibility = gutterVisibility;
            Title = title;
        }
    }
}
