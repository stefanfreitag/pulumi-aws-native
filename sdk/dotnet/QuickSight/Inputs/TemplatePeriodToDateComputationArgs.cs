// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplatePeriodToDateComputationArgs : global::Pulumi.ResourceArgs
    {
        [Input("computationId", required: true)]
        public Input<string> ComputationId { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("periodTimeGranularity")]
        public Input<Pulumi.AwsNative.QuickSight.TemplateTimeGranularity>? PeriodTimeGranularity { get; set; }

        [Input("time")]
        public Input<Inputs.TemplateDimensionFieldArgs>? Time { get; set; }

        [Input("value")]
        public Input<Inputs.TemplateMeasureFieldArgs>? Value { get; set; }

        public TemplatePeriodToDateComputationArgs()
        {
        }
        public static new TemplatePeriodToDateComputationArgs Empty => new TemplatePeriodToDateComputationArgs();
    }
}
