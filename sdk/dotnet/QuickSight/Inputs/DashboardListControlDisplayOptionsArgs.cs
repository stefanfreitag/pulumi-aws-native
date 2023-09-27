// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardListControlDisplayOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("infoIconLabelOptions")]
        public Input<Inputs.DashboardSheetControlInfoIconLabelOptionsArgs>? InfoIconLabelOptions { get; set; }

        [Input("searchOptions")]
        public Input<Inputs.DashboardListControlSearchOptionsArgs>? SearchOptions { get; set; }

        [Input("selectAllOptions")]
        public Input<Inputs.DashboardListControlSelectAllOptionsArgs>? SelectAllOptions { get; set; }

        [Input("titleOptions")]
        public Input<Inputs.DashboardLabelOptionsArgs>? TitleOptions { get; set; }

        public DashboardListControlDisplayOptionsArgs()
        {
        }
        public static new DashboardListControlDisplayOptionsArgs Empty => new DashboardListControlDisplayOptionsArgs();
    }
}
