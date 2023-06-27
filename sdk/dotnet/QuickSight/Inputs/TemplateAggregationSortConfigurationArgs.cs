// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateAggregationSortConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("aggregationFunction")]
        public Input<Inputs.TemplateAggregationFunctionArgs>? AggregationFunction { get; set; }

        [Input("column", required: true)]
        public Input<Inputs.TemplateColumnIdentifierArgs> Column { get; set; } = null!;

        [Input("sortDirection", required: true)]
        public Input<Pulumi.AwsNative.QuickSight.TemplateSortDirection> SortDirection { get; set; } = null!;

        public TemplateAggregationSortConfigurationArgs()
        {
        }
        public static new TemplateAggregationSortConfigurationArgs Empty => new TemplateAggregationSortConfigurationArgs();
    }
}
