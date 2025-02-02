// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateKpiOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("comparison")]
        public Input<Inputs.TemplateComparisonConfigurationArgs>? Comparison { get; set; }

        [Input("primaryValueDisplayType")]
        public Input<Pulumi.AwsNative.QuickSight.TemplatePrimaryValueDisplayType>? PrimaryValueDisplayType { get; set; }

        [Input("primaryValueFontConfiguration")]
        public Input<Inputs.TemplateFontConfigurationArgs>? PrimaryValueFontConfiguration { get; set; }

        [Input("progressBar")]
        public Input<Inputs.TemplateProgressBarOptionsArgs>? ProgressBar { get; set; }

        [Input("secondaryValue")]
        public Input<Inputs.TemplateSecondaryValueOptionsArgs>? SecondaryValue { get; set; }

        [Input("secondaryValueFontConfiguration")]
        public Input<Inputs.TemplateFontConfigurationArgs>? SecondaryValueFontConfiguration { get; set; }

        [Input("sparkline")]
        public Input<Inputs.TemplateKpiSparklineOptionsArgs>? Sparkline { get; set; }

        [Input("trendArrows")]
        public Input<Inputs.TemplateTrendArrowOptionsArgs>? TrendArrows { get; set; }

        [Input("visualLayoutOptions")]
        public Input<Inputs.TemplateKpiVisualLayoutOptionsArgs>? VisualLayoutOptions { get; set; }

        public TemplateKpiOptionsArgs()
        {
        }
        public static new TemplateKpiOptionsArgs Empty => new TemplateKpiOptionsArgs();
    }
}
