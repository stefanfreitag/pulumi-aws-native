// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardDefaultInteractiveLayoutConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("freeForm")]
        public Input<Inputs.DashboardDefaultFreeFormLayoutConfigurationArgs>? FreeForm { get; set; }

        [Input("grid")]
        public Input<Inputs.DashboardDefaultGridLayoutConfigurationArgs>? Grid { get; set; }

        public DashboardDefaultInteractiveLayoutConfigurationArgs()
        {
        }
        public static new DashboardDefaultInteractiveLayoutConfigurationArgs Empty => new DashboardDefaultInteractiveLayoutConfigurationArgs();
    }
}
