// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisBarChartFieldWellsArgs : global::Pulumi.ResourceArgs
    {
        [Input("barChartAggregatedFieldWells")]
        public Input<Inputs.AnalysisBarChartAggregatedFieldWellsArgs>? BarChartAggregatedFieldWells { get; set; }

        public AnalysisBarChartFieldWellsArgs()
        {
        }
        public static new AnalysisBarChartFieldWellsArgs Empty => new AnalysisBarChartFieldWellsArgs();
    }
}
