// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardGaugeChartConditionalFormattingOptionArgs : global::Pulumi.ResourceArgs
    {
        [Input("arc")]
        public Input<Inputs.DashboardGaugeChartArcConditionalFormattingArgs>? Arc { get; set; }

        [Input("primaryValue")]
        public Input<Inputs.DashboardGaugeChartPrimaryValueConditionalFormattingArgs>? PrimaryValue { get; set; }

        public DashboardGaugeChartConditionalFormattingOptionArgs()
        {
        }
        public static new DashboardGaugeChartConditionalFormattingOptionArgs Empty => new DashboardGaugeChartConditionalFormattingOptionArgs();
    }
}
