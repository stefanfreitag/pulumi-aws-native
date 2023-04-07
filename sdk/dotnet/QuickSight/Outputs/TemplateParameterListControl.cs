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
    public sealed class TemplateParameterListControl
    {
        public readonly Outputs.TemplateCascadingControlConfiguration? CascadingControlConfiguration;
        public readonly Outputs.TemplateListControlDisplayOptions? DisplayOptions;
        public readonly string ParameterControlId;
        public readonly Outputs.TemplateParameterSelectableValues? SelectableValues;
        public readonly string SourceParameterName;
        public readonly string Title;
        public readonly Pulumi.AwsNative.QuickSight.TemplateSheetControlListType? Type;

        [OutputConstructor]
        private TemplateParameterListControl(
            Outputs.TemplateCascadingControlConfiguration? cascadingControlConfiguration,

            Outputs.TemplateListControlDisplayOptions? displayOptions,

            string parameterControlId,

            Outputs.TemplateParameterSelectableValues? selectableValues,

            string sourceParameterName,

            string title,

            Pulumi.AwsNative.QuickSight.TemplateSheetControlListType? type)
        {
            CascadingControlConfiguration = cascadingControlConfiguration;
            DisplayOptions = displayOptions;
            ParameterControlId = parameterControlId;
            SelectableValues = selectableValues;
            SourceParameterName = sourceParameterName;
            Title = title;
            Type = type;
        }
    }
}
