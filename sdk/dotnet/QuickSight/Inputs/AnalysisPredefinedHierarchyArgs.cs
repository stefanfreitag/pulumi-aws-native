// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisPredefinedHierarchyArgs : global::Pulumi.ResourceArgs
    {
        [Input("columns", required: true)]
        private InputList<Inputs.AnalysisColumnIdentifierArgs>? _columns;
        public InputList<Inputs.AnalysisColumnIdentifierArgs> Columns
        {
            get => _columns ?? (_columns = new InputList<Inputs.AnalysisColumnIdentifierArgs>());
            set => _columns = value;
        }

        [Input("drillDownFilters")]
        private InputList<Inputs.AnalysisDrillDownFilterArgs>? _drillDownFilters;
        public InputList<Inputs.AnalysisDrillDownFilterArgs> DrillDownFilters
        {
            get => _drillDownFilters ?? (_drillDownFilters = new InputList<Inputs.AnalysisDrillDownFilterArgs>());
            set => _drillDownFilters = value;
        }

        [Input("hierarchyId", required: true)]
        public Input<string> HierarchyId { get; set; } = null!;

        public AnalysisPredefinedHierarchyArgs()
        {
        }
        public static new AnalysisPredefinedHierarchyArgs Empty => new AnalysisPredefinedHierarchyArgs();
    }
}
