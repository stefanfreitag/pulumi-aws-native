// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardWhatIfRangeScenarioArgs : global::Pulumi.ResourceArgs
    {
        [Input("endDate", required: true)]
        public Input<string> EndDate { get; set; } = null!;

        [Input("startDate", required: true)]
        public Input<string> StartDate { get; set; } = null!;

        [Input("value", required: true)]
        public Input<double> Value { get; set; } = null!;

        public DashboardWhatIfRangeScenarioArgs()
        {
        }
        public static new DashboardWhatIfRangeScenarioArgs Empty => new DashboardWhatIfRangeScenarioArgs();
    }
}
