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
    public sealed class TemplateLineChartDefaultSeriesSettings
    {
        public readonly Pulumi.AwsNative.QuickSight.TemplateAxisBinding? AxisBinding;
        public readonly Outputs.TemplateLineChartLineStyleSettings? LineStyleSettings;
        public readonly Outputs.TemplateLineChartMarkerStyleSettings? MarkerStyleSettings;

        [OutputConstructor]
        private TemplateLineChartDefaultSeriesSettings(
            Pulumi.AwsNative.QuickSight.TemplateAxisBinding? axisBinding,

            Outputs.TemplateLineChartLineStyleSettings? lineStyleSettings,

            Outputs.TemplateLineChartMarkerStyleSettings? markerStyleSettings)
        {
            AxisBinding = axisBinding;
            LineStyleSettings = lineStyleSettings;
            MarkerStyleSettings = markerStyleSettings;
        }
    }
}
