// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardDefaultFreeFormLayoutConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("canvasSizeOptions", required: true)]
        public Input<Inputs.DashboardFreeFormLayoutCanvasSizeOptionsArgs> CanvasSizeOptions { get; set; } = null!;

        public DashboardDefaultFreeFormLayoutConfigurationArgs()
        {
        }
        public static new DashboardDefaultFreeFormLayoutConfigurationArgs Empty => new DashboardDefaultFreeFormLayoutConfigurationArgs();
    }
}
