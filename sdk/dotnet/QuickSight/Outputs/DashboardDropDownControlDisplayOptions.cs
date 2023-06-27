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
    public sealed class DashboardDropDownControlDisplayOptions
    {
        public readonly Outputs.DashboardListControlSelectAllOptions? SelectAllOptions;
        public readonly Outputs.DashboardLabelOptions? TitleOptions;

        [OutputConstructor]
        private DashboardDropDownControlDisplayOptions(
            Outputs.DashboardListControlSelectAllOptions? selectAllOptions,

            Outputs.DashboardLabelOptions? titleOptions)
        {
            SelectAllOptions = selectAllOptions;
            TitleOptions = titleOptions;
        }
    }
}
