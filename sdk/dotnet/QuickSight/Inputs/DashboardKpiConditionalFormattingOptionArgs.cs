// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardKpiConditionalFormattingOptionArgs : global::Pulumi.ResourceArgs
    {
        [Input("actualValue")]
        public Input<Inputs.DashboardKpiActualValueConditionalFormattingArgs>? ActualValue { get; set; }

        [Input("comparisonValue")]
        public Input<Inputs.DashboardKpiComparisonValueConditionalFormattingArgs>? ComparisonValue { get; set; }

        [Input("primaryValue")]
        public Input<Inputs.DashboardKpiPrimaryValueConditionalFormattingArgs>? PrimaryValue { get; set; }

        [Input("progressBar")]
        public Input<Inputs.DashboardKpiProgressBarConditionalFormattingArgs>? ProgressBar { get; set; }

        public DashboardKpiConditionalFormattingOptionArgs()
        {
        }
        public static new DashboardKpiConditionalFormattingOptionArgs Empty => new DashboardKpiConditionalFormattingOptionArgs();
    }
}
