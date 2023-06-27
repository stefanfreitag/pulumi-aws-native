// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplatePredefinedHierarchyArgs : global::Pulumi.ResourceArgs
    {
        [Input("columns", required: true)]
        private InputList<Inputs.TemplateColumnIdentifierArgs>? _columns;
        public InputList<Inputs.TemplateColumnIdentifierArgs> Columns
        {
            get => _columns ?? (_columns = new InputList<Inputs.TemplateColumnIdentifierArgs>());
            set => _columns = value;
        }

        [Input("drillDownFilters")]
        private InputList<Inputs.TemplateDrillDownFilterArgs>? _drillDownFilters;
        public InputList<Inputs.TemplateDrillDownFilterArgs> DrillDownFilters
        {
            get => _drillDownFilters ?? (_drillDownFilters = new InputList<Inputs.TemplateDrillDownFilterArgs>());
            set => _drillDownFilters = value;
        }

        [Input("hierarchyId", required: true)]
        public Input<string> HierarchyId { get; set; } = null!;

        public TemplatePredefinedHierarchyArgs()
        {
        }
        public static new TemplatePredefinedHierarchyArgs Empty => new TemplatePredefinedHierarchyArgs();
    }
}
