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
    public sealed class DashboardPivotTableFieldWells
    {
        public readonly Outputs.DashboardPivotTableAggregatedFieldWells? PivotTableAggregatedFieldWells;

        [OutputConstructor]
        private DashboardPivotTableFieldWells(Outputs.DashboardPivotTableAggregatedFieldWells? pivotTableAggregatedFieldWells)
        {
            PivotTableAggregatedFieldWells = pivotTableAggregatedFieldWells;
        }
    }
}
