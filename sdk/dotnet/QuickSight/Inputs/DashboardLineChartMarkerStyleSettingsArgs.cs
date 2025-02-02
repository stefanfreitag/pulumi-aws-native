// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardLineChartMarkerStyleSettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("markerColor")]
        public Input<string>? MarkerColor { get; set; }

        [Input("markerShape")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardLineChartMarkerShape>? MarkerShape { get; set; }

        /// <summary>
        /// String based length that is composed of value and unit in px
        /// </summary>
        [Input("markerSize")]
        public Input<string>? MarkerSize { get; set; }

        [Input("markerVisibility")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardVisibility>? MarkerVisibility { get; set; }

        public DashboardLineChartMarkerStyleSettingsArgs()
        {
        }
        public static new DashboardLineChartMarkerStyleSettingsArgs Empty => new DashboardLineChartMarkerStyleSettingsArgs();
    }
}
