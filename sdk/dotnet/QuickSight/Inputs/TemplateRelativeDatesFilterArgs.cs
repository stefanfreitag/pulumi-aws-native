// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateRelativeDatesFilterArgs : global::Pulumi.ResourceArgs
    {
        [Input("anchorDateConfiguration", required: true)]
        public Input<Inputs.TemplateAnchorDateConfigurationArgs> AnchorDateConfiguration { get; set; } = null!;

        [Input("column", required: true)]
        public Input<Inputs.TemplateColumnIdentifierArgs> Column { get; set; } = null!;

        [Input("excludePeriodConfiguration")]
        public Input<Inputs.TemplateExcludePeriodConfigurationArgs>? ExcludePeriodConfiguration { get; set; }

        [Input("filterId", required: true)]
        public Input<string> FilterId { get; set; } = null!;

        [Input("minimumGranularity")]
        public Input<Pulumi.AwsNative.QuickSight.TemplateTimeGranularity>? MinimumGranularity { get; set; }

        [Input("nullOption", required: true)]
        public Input<Pulumi.AwsNative.QuickSight.TemplateFilterNullOption> NullOption { get; set; } = null!;

        [Input("parameterName")]
        public Input<string>? ParameterName { get; set; }

        [Input("relativeDateType", required: true)]
        public Input<Pulumi.AwsNative.QuickSight.TemplateRelativeDateType> RelativeDateType { get; set; } = null!;

        [Input("relativeDateValue")]
        public Input<double>? RelativeDateValue { get; set; }

        [Input("timeGranularity", required: true)]
        public Input<Pulumi.AwsNative.QuickSight.TemplateTimeGranularity> TimeGranularity { get; set; } = null!;

        public TemplateRelativeDatesFilterArgs()
        {
        }
        public static new TemplateRelativeDatesFilterArgs Empty => new TemplateRelativeDatesFilterArgs();
    }
}
