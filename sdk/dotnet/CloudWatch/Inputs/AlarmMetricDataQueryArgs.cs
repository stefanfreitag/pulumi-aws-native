// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudWatch.Inputs
{

    public sealed class AlarmMetricDataQueryArgs : global::Pulumi.ResourceArgs
    {
        [Input("accountId")]
        public Input<string>? AccountId { get; set; }

        [Input("expression")]
        public Input<string>? Expression { get; set; }

        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        [Input("label")]
        public Input<string>? Label { get; set; }

        [Input("metricStat")]
        public Input<Inputs.AlarmMetricStatArgs>? MetricStat { get; set; }

        [Input("period")]
        public Input<int>? Period { get; set; }

        [Input("returnData")]
        public Input<bool>? ReturnData { get; set; }

        public AlarmMetricDataQueryArgs()
        {
        }
        public static new AlarmMetricDataQueryArgs Empty => new AlarmMetricDataQueryArgs();
    }
}
